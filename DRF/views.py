from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


@api_view(['GET'])
def AppView(request):
    api_list = {
        'List': '/list/',
        'Create': '/create/',
        'Update': '/update/<str:pk>/',
        'Detail': '/detail/<str:pk>/',
        'Delete': '/delete/<str:pk>/'
    }
    return Response(api_list)


@api_view(['GET', 'POST'])
def List(request):
    if request.method == 'GET':
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)
    else:
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def Update(request, pk):
    if request.method == 'GET':
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book, many=False)
        return Response(serializer.data)

    else:
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(instance=book, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['DELETE'])
def Delete(request, pk):
    book_delete = Book.objects.get(id=pk)
    book_delete.delete()
    return Response('Book Successfully delete')
