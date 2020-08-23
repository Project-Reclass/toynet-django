from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializer import ToyNetConfigSerializer, ToyNetSessionSerializer
from .models import ToyNetConfig, ToyNetSession

from .emulator import xmlParser as parser

from .emulator.command.commandParser import parseModificationCommand

from .emulator.toydiagram.diagramTree import DiagramGraph
from .emulator.toydiagram.network import ToyNetDiagram, ToySubnet
from .emulator.toydiagram.nodes.switch import Switch
from .emulator.toydiagram.nodes.host import Host
from .emulator.toydiagram.nodes.router import Router

import json
import os
from xml.etree import ElementTree as ET

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
    filename = 'emulator/visualizations/pusheen'

    topology:parser.ToyTopoConfig = parser.parseXML(toynetsession.topology)

    print('__INFO___ Generating Diagram Graph from Configurations')
    graph = DiagramGraph(topology)
    print('__INFO___ Generating Diagram Tree from Diagram Graph')
    diagramTree = graph.getDiagramTree()

    nodes = dict()
    with ToyNetDiagram('ToyNet Demo Network', 'toynet/' + filename, show=False):
        # devices
        for deviceName in diagramTree.routers:
            nodes[deviceName] = Router(deviceName)

        for (i, subnet) in enumerate(diagramTree.subnets):
            with ToySubnet("subnet" + str(i)):
                for deviceName in subnet.switches:
                        nodes[deviceName] = Switch(deviceName)
                for deviceName in subnet.hosts:
                        nodes[deviceName] = Host(deviceName)

        # cables
        for (n1, n2) in diagramTree.primaryLinks:
            nodes[n1] >> nodes[n2]

        for (n1, n2) in diagramTree.secondaryLinks:
            nodes[n1] >> nodes[n2]

    try:
        currentDir = os.path.dirname(__file__)
        relativeImageFilePath = filename + '.png'
        with open(os.path.join(currentDir, relativeImageFilePath), "rb") as f:
            return HttpResponse(f.read(), content_type="image/png")
    except IOError:
        return Response('There was an error')

@api_view(['PUT'])
def modifyToyNetSession(request, pk):
    reqJson = json.loads(request.body.decode('utf-8'))
    command = reqJson['command']

    # store new modification event

    toynetsession = ToyNetSession.objects.get(pk=pk)
    xmlTopology:ET = ET.fromstring(toynetsession.topology)


    xmlTopology = parseModificationCommand(command, xmlTopology)
    xmlString = topology=ET.tostring(xmlTopology, encoding='utf-8').decode('utf-8')

    ToyNetSession.objects.select_for_update().filter(pk=pk).update(topology=xmlString)

    return Response({
        'message': 'updated topology coming soon for ' + command,
        'topology': toynetsession.topology,
    })
