from django.db import models


# Create your models here.

class Book:
    def __init__(self, title, price):
        self.title = title
        self.price = price
