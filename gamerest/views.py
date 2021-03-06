from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from gameapp.models import Team
from .serializers import TeamSerializer


@api_view(['GET'])
def Api(request):
    api_list = {
        'List': '/list/',
        'Create': '/create/',
        'Update': '/update/<str:pk>/',
        'Delete': '/delete/<str:pk>/'
    }
    return Response(api_list)


@api_view(['GET', 'POST'])
def List(request):
    if request.method == 'GET':
        team = Team.objects.all()
        serializer = TeamSerializer(team, many=True)
        return Response(serializer.data)
    else:
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


@api_view(['PUT', 'GET', 'DELETE'])
def Update(request, pk):
    if request.method == 'PUT':
        team = Team.objects.get(id=pk)
        serializer = TeamSerializer(instance=team, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    elif request.method == 'GET':
        team = Team.objects.get(id=pk)
        serializer = TeamSerializer(team, many=False)
        return Response(serializer.data)
    else:
        team = Team.objects.get(id=pk)
        team.delete()
        return Response('Item delete successfully!')
