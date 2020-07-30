from rest_framework import viewsets  
from mininet.serializer import MininetInstanceSerializer
from mininet.models import MininetInstance 

class MininetInstanceViewset(viewsets.ModelViewSet):
    serializer_class = MininetInstanceSerializer
    queryset = MininetInstance.objects.all()
    