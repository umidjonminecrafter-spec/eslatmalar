from django.shortcuts import render
from rest_framework import viewsets

from.models import *
# Create your views here.
from rest_framework.response import Response

from .serializers import EslatmalarSerializer, KartochkaSerializer


class EslatmalarViewSet(viewsets.ModelViewSet):
    queryset = Eslatmalar.objects.all()
    serializer_class = EslatmalarSerializer

class KartochkaViewSet(viewsets.ModelViewSet):
    queryset = Kartochka.objects.all()
    serializer_class = KartochkaSerializer
