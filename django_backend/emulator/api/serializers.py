from rest_framework import serializers 
from emulator.models import MiniNet 

class MiniNetSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = MiniNet
            fields = ['networkConfig','id']

