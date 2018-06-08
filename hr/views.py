from django.shortcuts import render
from . forms import AddJobForm
# Create your views here.

def addjob(request):
    if  request.method == "GET":
        f = AddJobForm()
    else:  # POST request
        f = AddJobForm( request.POST)
        if f.is_valid():
            f.save()

    return render(request, 'addjob.html', {'form': f})