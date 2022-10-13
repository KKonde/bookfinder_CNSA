from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

import os
import json

from .forms import BookForm
from .models import BookData
from .find import book_Find, book_Match


# Create your views here.
# 1 검색
# 2 웹 캠 사진 저장
# 3 책의 사진과 매칭
# 4 결과값 출력 및 db 수정

def search(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = BookData.objects.get(book_title=request.POST['bookName'])
            new = book_Find(book.book_image)

            if new == "None":
                return JsonResponse({"fail":"fail"})

            return JsonResponse(new)

    return JsonResponse({"fail":"fail"})

def match(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            books = BookData.objects.all()
            i = book_Match(books, request.POST['book'])
            if i == -1:
                return HttpResponse("fail")

            return JsonResponse({"title":books[i].book_title,
                                 "publisher":books[i].book_publisher,
                                 "ISBN":books[i].book_ISBN,
                                 "claim":books[i].book_claim})

    return HttpResponse("fail")