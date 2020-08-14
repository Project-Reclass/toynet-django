from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ToyNetConfigSerializer, ToyNetSessionSerializer

from .models import ToyNetConfig, ToyNetSession

import json
import os

@api_view(['POST'])
def createToyNetSession(request):
    reqJson = json.loads(request.body.decode('utf-8'))
    toynetconfig_id  = int(reqJson['toynet_id'])
    user_id = int(reqJson['user_id'])

    toynetconfig = ToyNetConfig.objects.get(pk=toynetconfig_id)
    toynetsession = ToyNetSession.objects.create(
        toynetconfig=toynetconfig,
        topology=toynetconfig.topology,
        user_id=user_id
    )

    return Response({
        'message': 'SUCCESS', #change?
        'session_id': toynetsession.id,
        'topology': toynetsession.topology,
    })

@api_view(['GET'])
def showToyNetSession(request, pk):
    toynetsession = ToyNetSession.objects.get(pk=pk)
    return Response({
        'topology': toynetsession.topology,
    })

@api_view(['GET'])
def visualizeToyNetSession(request, pk):
    toynetsession = ToyNetSession.objects.get(pk=pk)

    # generate image in visualizations/ as <sessionid>-<timestamp>.png

    try:
        currentDir = os.path.dirname(__file__)
        relativeImageFilePath = "visualizations/sample.png"
        with open(os.path.join(currentDir, relativeImageFilePath), "rb") as f:
            return HttpResponse(f.read(), content_type="image/png")
    except IOError:
        return Response('There was an error')

@api_view(['POST'])
def modifyToyNetSession(request, pk):
    reqJson = json.loads(request.body.decode('utf-8'))
    command = reqJson['command']

    # store new modification event

    toynetsession = ToyNetSession.objects.get(pk=pk)

    # modify topology to based on command
    # commit topology

    return Response({
        'message': 'updated topology coming soon for ' + command,
        'topology': toynetsession.topology,
    })
