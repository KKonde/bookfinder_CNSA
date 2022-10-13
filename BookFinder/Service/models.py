from django.db import models

# Create your models here.
class BookData(models.Model):
    book_title = models.CharField(null=False, blank=True, max_length=100)
    # 책 제목
    book_publisher = models.CharField(null=True, blank=True, max_length=30)
    # 책 출판사
    book_ISBN = models.CharField(null=True, blank=True, max_length=50)
    # 책 ISBN
    book_claim = models.CharField(null=True, max_length=50)
    # 책 청구기호
    book_image = models.ImageField(upload_to='files/', null=True)
    # 책장의 책 사진 파일

    def __str__(self):
        return self.book_title