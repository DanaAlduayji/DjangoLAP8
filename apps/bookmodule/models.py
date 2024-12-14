from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=50)  # Book title, up to 50 characters
    author = models.CharField(max_length=50)  # Author name, up to 50 characters
    price = models.FloatField(default=0.0)  # Price of the book, default is 0.0
    edition = models.SmallIntegerField(default=1)  # Edition number, default is 1

class Address(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
