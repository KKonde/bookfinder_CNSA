# Generated by Django 2.2.6 on 2019-11-01 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0002_auto_20191102_0212'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookdata',
            name='book_x_position',
        ),
        migrations.RemoveField(
            model_name='bookdata',
            name='book_y_position',
        ),
    ]