from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from .models import Book
from . import database
import requests


def welcome(request):
    return render(request, 'welcome.html')


def countries(request):
    return render(request, 'countries.html')


def searchCountries(request, cname):
    resp = requests.get("https://restcountries.eu/rest/v2/name/" + cname)
    if resp.status_code == 200:
        countries = []
        for c in resp.json():
            country = {'name': c['name'], 'code': c['alpha3Code']}
            countries.append(country)
        return JsonResponse(countries, safe=False)
    else:
        return HttpResponseNotFound()


def countryinfo(request, code):
    resp = requests.get("https://restcountries.eu/rest/v2/alpha/" + code)
    if resp.status_code == 200:
        return render(request, 'countryinfo.html', {'country': resp.json()})
    else:
        return HttpResponseNotFound()


def getbook(request, id):
    book = database.get_book(id)
    if book is None:
        return HttpResponseNotFound()  # Response with 404 status code to client
    else:
        return JsonResponse({"title": book.title, "price": book.price, "author": book.author})


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
