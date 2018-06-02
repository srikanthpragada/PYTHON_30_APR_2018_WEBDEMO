from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from .models import Book
from . import database


def welcome(request):
    return render(request, 'welcome.html')


def getbook(request, id):
    book = database.get_book(id)
    if book is None:
        return HttpResponseNotFound()  # Response with 404 status code to client
    else:
        return JsonResponse({"title": book.title, "price": book.price , "author" : book.author})


def ajax(request):
    return render(request, 'ajax_demo.html')


def get_message(request):
    return HttpResponse("Winners never quit. Quitters never win!")


def list_books(request):
    books = [Book("Java Complete Reference", 800),
             Book("Programming in C", 300),
             Book("Python Essentials Guide", 900)]

    return render(request, 'list_books.html',
                  {"books": books,
                   "avg": sum(map(lambda b: b.price, books)) // len(books)
                   }
                  )


def discount(request):
    if 'amount' in request.POST:
        amount = int(request.POST["amount"])
        discount = amount * 0.10
        return render(request, 'discount.html',
                      {'amount': amount, 'discount': discount})
    else:
        return render(request, 'discount.html')
