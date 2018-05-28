from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import sqlite3


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
    return HttpResponse("Showing details of book : " + id)