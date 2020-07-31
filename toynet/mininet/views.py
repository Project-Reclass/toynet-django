from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import MininetInstanceSerializer

from .models import MininetInstance

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        #'Create': '/create/',
        'Retrieve All': '/showall',
        'Retrieve One': '/<str:pk>',
        #'Update': '/update/<str:pk>',
        #'Delete': '/close/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def mininetShowall(request):
    mininet = MininetInstance.objects.all()
    serializer = MininetInstanceSerializer(mininet, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def mininetShow(request, pk):
    mininet = MininetInstance.objects.get(pk=pk)
    serializer = MininetInstanceSerializer(mininet)
    return Response(serializer.data)
