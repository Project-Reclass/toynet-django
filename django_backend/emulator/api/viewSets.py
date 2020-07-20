from rest_framework import viewsets  
from .serializers import MiniNetSerializer
from emulator.models import MiniNet 

class MiniNetViewset(viewsets.ModelViewSet):
    serializer_class = MiniNetSerializer
    queryset = MiniNet.objects.all()