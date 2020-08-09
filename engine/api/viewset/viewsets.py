from rest_framework import viewsets  
from toynet.serializer import ToyNetConfigSerializer, ToyNetSessionSerializer
from toynet.models import ToyNetSession, ToyNetConfig

class ToyNetConfigViewset(viewsets.ModelViewSet):
    serializer_class = ToyNetConfigSerializer
    queryset = ToyNetConfig.objects.all()

class ToyNetSessionViewset(viewsets.ModelViewSet):
    serializer_class = ToyNetSessionSerializer
    queryset = ToyNetSession.objects.all()
