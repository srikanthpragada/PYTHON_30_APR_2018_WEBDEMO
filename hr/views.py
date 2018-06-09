from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponseNotFound
from django.views.generic import ListView, TemplateView, View
from . forms import AddJobForm, EditJobForm
from . models import Job

class ListJobView(ListView):
    model = Job
    template_name = 'listjobs.html'


class SearchJobsView(View):
    template_name = 'searchjobs.html'
    def get(self,request):
        return render(request, self.template_name)

    def post(self,request):
        title = request.POST["title"]
        jobs = Job.objects.filter( jobtitle__contains = title)
        return render(request, self.template_name, { 'title' : title, 'jobs' : jobs})


class JobView(View):
    template_name = 'addjob.html'

    def get(self, request):
        f = AddJobForm()
        return render(request, self.template_name, {'form': f})

    def post(self, request):
        f = AddJobForm(request.POST)
        if f.is_valid():
            f.save()
            message = "Added Job Successfully!"
        else:
            message = "Validation Error!"

        return render(request, self.template_name, {'form': f , 'message' : message})


class DeleteJobView(View):

    def get(self,request,jobid):
        try:
            job = Job.objects.get(jobid=jobid)
            job.delete()
            return HttpResponseRedirect('/hr/searchjobs')
        except:
            return HttpResponseNotFound()


class EditJobView(View):
    template_name = "editjob.html"

    def get(self,request,jobid):
        try:
            job = Job.objects.get(jobid=jobid)
            f = EditJobForm(instance=job)
            return render(request, self.template_name, {'form': f})
        except:
            return HttpResponseNotFound()