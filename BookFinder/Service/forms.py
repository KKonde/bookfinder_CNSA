from django import forms

from .models import BookData

class BookForm(forms.ModelForm):
    class Meta:
        model = BookData
        fields = ('book_title', 'book_publisher',
                  'book_ISBN', 'book_claim',
                  'book_image')