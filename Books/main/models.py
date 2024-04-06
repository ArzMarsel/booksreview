from django.db import models


class Author(models.Model):
    name = models.CharField('Name:', max_length=30)
    biography = models.TextField('Biography:')


class Book(models.Model):
    title = models.CharField('Title:', max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Author:')
    description = models.TextField('Description:')
    date_of_pub = models.DateField('Date of publication:')


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Book:')
    rating = models.IntegerField('Rating:')
    text = models.TextField('Text:')