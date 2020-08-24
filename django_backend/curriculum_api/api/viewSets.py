from rest_framework import viewsets  
from .serializers import MiniNetSerializer, ModuleSerializer, SubmoduleSerializer
from emulator.models import MiniNet, Module, Submodule

class MiniNetViewset(viewsets.ModelViewSet):
    serializer_class = MiniNetSerializer
    queryset = MiniNet.objects.all()

class ModuleViewset(viewsets.ModelViewSet):
    serializer_class = ModuleSerializer
    queryset = Module.objects.all()

class SubmoduleViewset(viewsets.ModelViewSet):
    serializer_class = SubmoduleSerializer
    queryset = Submodule.objects.all()