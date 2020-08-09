from rest_framework import serializers
from toynet.models import ToyNetConfig, ToyNetSession

class ToyNetConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ToyNetConfig
        fields = '__all__'

class ToyNetSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = ToyNetSession
        fields = '__all__'