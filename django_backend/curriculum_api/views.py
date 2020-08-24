from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .api.serializers import ModuleSerializer, SubmoduleSerializer
from .models import Module, Submodule


@api_view(['GET'])
def getModules(request):
    modules = Module.objects.all()
    serializer = ModuleSerializer(modules,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getModule(request,pk):
    module = Module.objects.get(id=pk)
    serializer = ModuleSerializer(module)
    return Response(serializer.data)

@api_view(['POST'])
def updateModule(request,pk):
    module = Module.objects.get(id=pk)
    serializer = ModuleSerializer(instance=module,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def createModule(request):
    serializer = ModuleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteModule(request,pk):
    module = Module.objects.get(id=pk)
    module.delete()
    return Response('module deleted!')




@api_view(['GET'])
def getSubModules(request):
    submodules = Submodule.objects.all()
    serializer = SubmoduleSerializer(submodules,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSubModule(request,pk):
    submodule = Submodule.objects.get(id=pk)
    serializer = SubmoduleSerializer(submodule)
    return Response(serializer.data)

@api_view(['POST'])
def updateSubModule(request,pk):
    submodule = Submodule.objects.get(id=pk)
    serializer = SubmoduleSerializer(instance=submodule,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def createSubModule(request):
    serializer = SubmoduleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteSubModule(request,pk):
    submodule = Submodule.objects.get(id=pk)
    submodule.delete()
    return Response('module deleted!')



# Create your views here.
