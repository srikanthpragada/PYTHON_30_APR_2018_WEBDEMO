from django.shortcuts import render
from django.http import HttpResponse,  HttpResponseRedirect
from datetime import datetime,timedelta

def selectcity(request):
    return render(request,'selectcity.html')

def savecity(request):
    city = request.POST["city"]
    resp = HttpResponseRedirect("/books/showmovies")
    resp.set_cookie("city", city, expires= datetime.now() + timedelta(days = 5))
    return resp

def showmovies(request):
    if not 'city'  in  request.COOKIES:
        return HttpResponseRedirect("/books/selectcity")
    else:
        city = request.COOKIES['city']
        movies = {
                   "vizag" : ['Movie1', 'Movie2', 'Movie3'],
                   "chennai": ['Movie11', 'Movie12', 'Movie13'],
                   "hyd": ['Movie33', 'Movie44'],
                   "bang": ['Movie9', 'Movie10'],
                 }
        return render(request,'showmovies.html',
                       { 'city' : city, 'movies' :  movies[city]})




