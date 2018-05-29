from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import sqlite3
from . models import DbBook
from . forms import AddBookForm


def list_books(request):
    try:
        con = sqlite3.connect(r"e:\classroom\python\demo.db")
        cur = con.cursor()
        cur.execute("select * from books order by title")
        return render(request, 'db/db_list_books.html',
                      {"books": cur.fetchall()})
    except Exception as ex:
        print(ex)
        return HttpResponseRedirect("/books/error/")
    finally:
        con.close()


def error(request):
    return render(request, 'db/error.html')


def show_details(request, id):
    try:
        con = sqlite3.connect(r"e:\classroom\python\demo.db")
        cur = con.cursor()
        cur.execute("select * from books where bookid = ?", id)
        row = cur.fetchone()
        print("Row  is : " , row)
        b = DbBook( row[0], row[1],row[2],row[3])
        return render(request, 'db/db_book_details.html', {"book": b})
    except Exception as ex:
        print(ex)
        return render(request, 'db/db_book_details.html', {"book": None })
    finally:
        con.close()


def add_book(request):
    f = AddBookForm()
    return render(request,'db/db_add_book.html', { 'form' : f})