from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    #path('addjob/', views.addjob),
    path('addjob/', views.JobView.as_view()),
    path("listjobs/", views.ListJobView.as_view()),
    path("searchjobs/", views.SearchJobsView.as_view()),
    path("about/", TemplateView.as_view( template_name='about.html')),
    re_path("deletejob/(\w+)", views.DeleteJobView.as_view()),
    re_path("editjob/(\w+)", views.EditJobView.as_view()),
]
