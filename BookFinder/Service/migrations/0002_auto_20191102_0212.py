# Generated by Django 2.2.6 on 2019-11-01 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookdata',
            name='book_image_in_shelf',
        ),
        migrations.AddField(
            model_name='bookdata',
            name='book_image',
            field=models.ImageField(null=True, upload_to='files/'),
        ),
    ]
