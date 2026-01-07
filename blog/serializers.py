from rest_framework.serializers import Serializer, ModelSerializer,ValidationError
from blog.models import *
from .models import *
from rest_framework import serializers

class EslatmalarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eslatmalar
        fields = '__all__'


class KartochkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kartochka
        fields = '__all__'