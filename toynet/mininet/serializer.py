from rest_framework import serializers
from mininet.models import MininetInstance

class MininetInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model  = MininetInstance
        fields = '__all__'