from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ToyNetConfigSerializer, ToyNetSessionSerializer

from .models import ToyNetConfig, ToyNetSession

import json

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        #'Create': '/config/create',
        'Retrieve': '/config/show/<str:pk>',
        #'Update': '/config/update/<str:pk>',
        #'Delete': '/config/delete/<str:pk>',
        'Create': '/session/create',
        'Retrieve': '/session/show/<str:pk>',
        #'Update': '/session/update/<str:pk>',
        #'Delete': '/session/delete/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def showToyNetConfig(request, pk):
    toynet = ToyNetConfig.objects.get(pk=pk)
    serializer = ToyNetConfigSerializer(toynet)
    return Response(serializer.data)

@api_view(['POST'])
def createToyNetSession(request):
    reqJson = json.loads(request.body.decode('utf-8'))
    toynetconfig_id  = int(reqJson['toynet_id'])
    user_id = int(reqJson['user_id'])

    toynet = ToyNetConfig.objects.get(pk=toynetconfig_id)
    toynetsession = ToyNetSession.objects.create(
        toynetconfig=toynet,
        topology=toynet.topology,
        user_id=user_id
    )
    return Response({"message": "Created new ToyNet session", "data": toynetsession.id})

@api_view(['GET'])
def showToyNetSession(request, pk):
    toynet = ToyNetSession.objects.get(pk=pk)
    serializer = ToyNetSessionSerializer(toynet)
    return Response(serializer.data)

