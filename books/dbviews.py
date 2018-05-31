from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import DbBook
from .forms import AddBookForm
from . import database


def list_books(request):
    books = database.get_all_books()
    if books is None:
        return HttpResponseRedirect('db/error')
    else:
        return render(request, 'db/db_list_books.html', {"books": books})


def error(request):
    return render(request, 'db/error.html')


def show_details(request, id):
    book = database.get_book(id)
    return render(request, 'db/db_book_details.html', {"book": book})


def delete_book(request, id):
    # delete book
    print("Deleting book ", id)
    done = database.delete_book(id)
    if done:
        return HttpResponseRedirect('/books/dblist')
    else:
        return HttpResponseRedirect('/books/error')


def add_book(request):
    if 'title' in request.POST:
        f = AddBookForm(request.POST)  # Bound form
        message = ""
        if f.is_valid():
            title = f.cleaned_data["title"]
            author = f.cleaned_data["author"]
            price = f.cleaned_data["price"]
            done = database.add_book(title, author, price)
            if done:
                message = "Added Book Successfully!"
            else:
                message = "Sorry! Could not add book!"
        else:
            print("Validation error")
            message = "Sorry! Invalid input. Please try again!"

        return render(request, 'db/db_add_book.html',
                      {'form': f, 'message': message})
    else:
        f = AddBookForm()
        return render(request, 'db/db_add_book.html', {'form': f})
