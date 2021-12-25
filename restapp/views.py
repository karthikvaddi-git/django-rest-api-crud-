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

@api_view(['GET','POST'])
def studentjson(request):
    if request.method == 'GET':
        studentobj = student.objects.all()
        serialobj = studentserializer(studentobj, many=True)
        return Response(serialobj.data)
    elif request.method == 'POST':
        serializer = studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def students_details(request,pk):
    try:
        studentobj = student.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = studentserializer(studentobj)
        return Response(serializers.data)

    elif request.method == 'PUT':
        serializers = studentserializer(studentobj,request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        studentobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




