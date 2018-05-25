from django.http import HttpResponse
import datetime


def hello(request):
    # print(type(request))
    return HttpResponse("<h1>Hello Django </h1>")


def now(request):
    ct = datetime.datetime.now()
    return HttpResponse("<h1 style='color:red'>%s</h1>" % (str(ct)))
