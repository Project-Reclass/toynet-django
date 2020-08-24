from rest_framework import serializers 
from emulator.models import MiniNet, Module, Submodule

class MiniNetSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = MiniNet
            fields = ['networkConfig','id']

class ModuleSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Module
            fields = ["name","id"]

class SubmoduleSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Submodule
            fields = ['name','id']
