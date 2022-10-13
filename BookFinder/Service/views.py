from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse, HttpResponseForbidden,JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

import os
import json

from .forms import BookForm
from .models import BookData
from .find import book_Find


# Create your views here.
# 1 검색
# 2 웹 캠 사진 저장
# 3 책의 사진과 매칭
# 4 결과값 출력 및 db 수정

def search(request, book):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = BookData.object.get(book_title=request.POST['bookName'])
            book_Find(book.book_image)

            return JsonResponse({'image' : book_Find(book.book_image)})


    return JsonResponse({'image': book_Find(book.book_image)})