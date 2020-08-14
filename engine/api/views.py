from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'POST Create ToyNet (toynet_id, user_id)': 'toynet/session/create',
        'GET Visualize ToyNet Topology': 'toynet/session/visualize/<str:pk>',
        'GET Retrieve ToyNet Topology': 'toynet/session/show/<str:pk>',
        'POST Modify ToyNet Topology (command)': 'toynet/session/modify/<str:pk>',
    }
    return Response(api_urls)
