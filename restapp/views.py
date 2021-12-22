from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import studentserializer
from .models import student
# Create your views here.
@api_view(['GET'])
def home(request):
    apiurls={
        "get":'task/get',
        "put":'task/put',
        "delete":'task/delete'
    }
    return Response(apiurls)

@api_view(['GET'])
def studentjson(request):
    studentobj=student.objects.all()
    serialobj=studentserializer(studentobj,many=True)
    return Response(serialobj.data)

