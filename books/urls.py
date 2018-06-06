from django.urls import path, re_path
from . import views, dbviews, state_views

urlpatterns = [
    path("welcome/", views.welcome),
    path("list/", views.list_books),
    path("discount/", views.discount),
    path("dblist/", dbviews.list_books),
    re_path("details/([0-9]+)/", dbviews.show_details),
    path("error/", dbviews.error),
    path("addbook/", dbviews.add_book),
    re_path("deletebook/([0-9]+)/", dbviews.delete_book),
    path("ajax/", views.ajax ),
    path("message/", views.get_message ),
    re_path("getbook/([0-9]+)/", views.getbook),
    path("countries/", views.countries ),
    re_path(r"searchcountries/([\w]+)/", views.searchCountries),
    re_path(r"countryinfo/([\w]+)/", views.countryinfo),
    re_path(r"countryinfo/([\w]+)/", views.countryinfo),
    path("selectcity/", state_views.selectcity),
    path("savecity/", state_views.savecity),
    path("showmovies/", state_views.showmovies),

]
