from pon.models import Kota, Kuliner, Penginapan, ItemKamar
from rest_framework import viewsets
from .serializers import (
    KotaSerializer, 
    KulinerSerializer, 
    PenginapanSerializer,
    ItemKamarSerializer,
)

class KotaViewSet(viewsets.ModelViewSet):
    serializer_class = KotaSerializer
    queryset = Kota.objects.all()

class KulinerViewSet(viewsets.ModelViewSet):
    serializer_class = KulinerSerializer
    queryset = Kuliner.objects.all()

class PenginapanViewSet(viewsets.ModelViewSet):
    serializer_class = PenginapanSerializer
    queryset = Penginapan.objects.all()

class ItemKamarViewSet(viewsets.ModelViewSet):
    serializer_class = ItemKamarSerializer
    queryset = ItemKamar.objects.all()