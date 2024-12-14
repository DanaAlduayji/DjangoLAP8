from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)  # Book title, up to 50 characters
    author = models.CharField(max_length=50)  # Author name, up to 50 characters
    price = models.FloatField(default=0.0)  # Price of the book, default is 0.0
    edition = models.SmallIntegerField(default=1)  # Edition number, default is 1

