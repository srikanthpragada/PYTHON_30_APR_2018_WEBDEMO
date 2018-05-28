from django.urls import path, re_path
from . import views, dbviews

urlpatterns = [
    path("welcome/", views.welcome),
    path("list/", views.list_books),
    path("discount/", views.discount),
    path("dblist/", dbviews.list_books),
    re_path("details/([0-9]+)/", dbviews.show_details),
    path("error/", dbviews.error),

]
