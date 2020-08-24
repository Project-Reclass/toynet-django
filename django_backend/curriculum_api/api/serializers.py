from rest_framework import serializers 
from curriculum_api.models import Module, Submodule

class ModuleSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Module
            fields = ['name','id']

class SubmoduleSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Submodule
            fields = ["name","id"]
