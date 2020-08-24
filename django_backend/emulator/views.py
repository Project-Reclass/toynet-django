from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from emulator.api.serializers import ModuleSerializer
from .models import MiniNet, Module, Submodule
# Create your views here.

@api_view(['GET'])
def getModules(request):
    modules = Module.objects.all()
    serializer = ModuleSerializer(modules)
    return Response(serializer.data)

@api_view(['POST'])
def createModule(request):
    serializer = ModuleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
