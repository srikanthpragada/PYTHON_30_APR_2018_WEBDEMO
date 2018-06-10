from django.urls import path, re_path
from django.views.generic import TemplateView

from . import rest_views
from . import views

urlpatterns = [
    #path('addjob/', views.addjob),
    path('addjob/', views.JobView.as_view()),
    path("listjobs/", views.ListJobView.as_view()),
    path("searchjobs/", views.SearchJobsView.as_view()),
    path("about/", TemplateView.as_view( template_name='about.html')),
    re_path("deletejob/(\w+)", views.DeleteJobView.as_view()),
    re_path("editjob/(\w+)", views.EditJobView.as_view()),
    path("updatejob/", views.UpdateJobView.as_view()),
    path('jobclient/', rest_views.client),
    path('jobs/', rest_views.jobs),
    re_path('job/(\w+)/', rest_views.processjob),
]
