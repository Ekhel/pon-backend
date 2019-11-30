import graphene
from graphene_django.types import DjangoObjectType
from pon.models import Kategori_kuliner, Kuliner

class KategoriType(DjangoObjectType):
    class Meta:
        model = Kategori_kuliner


class KulinerType(DjangoObjectType):
    class Meta:
        model = Kuliner


class Query(object):
    all_kategori = graphene.List(KategoriType)
    all_kuliner = graphene.List(KulinerType)

    def resolve_all_kategori(self, info, **kwargs):
        return Kategori_kuliner.objects.all()

    def resolve_all_kuliner(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Kuliner.objects.select_related('kategori').all()