from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import MininetInstanceSerializer

from .models import MininetInstance

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Create': '/create/',
        'View': '/show/<str:pk>',
        'Update': '/update/<str:pk>',
        'Close': '/close/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def mininetShow(request):
    mininet = MininetInstance.objects.all()
    serializer = MininetInstanceSerializer(mininet, many=False)
    return Response(serializer.data)
