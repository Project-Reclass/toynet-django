from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ToyNetSessionSerializer

from .models import ToyNetConfig, ToyNetSession

import json

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Create': '/session/create',
        #'Retrieve All': '/session/showall',
        'Retrieve One': '/session/show/<str:pk>',
        'Update': '/session/update/<str:pk>',
        #'Delete': '/session/delete/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def showToyNetSession(request, pk):
    toynet = ToyNetSession.objects.get(pk=pk)
    serializer = ToyNetSessionSerializer(toynet)
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
