from django.db import models

# Create your models here.

class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price

class DbBook:
    def __init__(self, id,title, author,price):
        self.id = id
        self.title = title
        self.author = author
        self.price = price
