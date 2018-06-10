from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Job
from .serializers import JobSerializer
from django.shortcuts import  render


def client(request):
    return render(request,'jobclient.html')

@api_view(['GET','POST'])
def jobs(request):
    if request.method== "GET":
        serializer = JobSerializer(Job.objects.all(), many=True)
        return Response(serializer.data)
    else:   # Post
        try:
            job = JobSerializer(data=request.data)
            if job.is_valid():
                job.save()
                print("Saved Employee")
                return Response(job.data, status=status.HTTP_201_CREATED)
            else:
                print("Data is invalid")
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET','DELETE','PUT'])
def processjob(request, jobid):
    if request.method == 'GET':
        try:
            job = Job.objects.get(pk=jobid)
            serializer = JobSerializer(job)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == "DELETE":
        try:
            job = Job.objects.get(pk=jobid)
            job.delete()
            return Response(status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:  # PUT
        try:
            job_in_db = Job.objects.get(pk=jobid)
            newjob = JobSerializer(job_in_db, data=request.data, partial=True)
            if newjob.is_valid():
                newjob.save()   # update
                return Response(status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


