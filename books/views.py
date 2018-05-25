from django.shortcuts import render
from django.http import HttpResponse
from . models import Book

def welcome(request):
    return render(request, 'welcome.html')


def list_books(request):
    books = [ Book("Java Complete Reference",800),
              Book("Programming in C", 300),
              Book("Python Essentials Guide", 900) ]

    return render(request, 'list_books.html' ,
                   {"books" : books ,
                    "count" : len(books),
                    "avg" : sum(map(lambda b: b.price, books)) // len(books)
                   }
                  )