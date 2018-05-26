from django.urls import path
from . import views

urlpatterns = [
    path("welcome/", views.welcome),
    path("list/", views.list_books),
    path("discount/", views.discount),
]
