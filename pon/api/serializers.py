from rest_framework import serializers
from pon.models import Kota, Kategori_kuliner, Kuliner, Penginapan, ItemKamar

class KotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kota
        fields = (
            'id_kota',
            'nama_kota'
        )

class KulinerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kuliner
        fields = (
            'id_kuliner',
            'kategori',
            'kota',
            'title',
            'latitude',
            'longitude',
            'jam_buka',
            'jam_tutup',
            'alamat',
            'deskripsi'
        )

class PenginapanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Penginapan
        fields = (
            'id_penginapan',
            'kategori',
            'kota',
            'title',
            'slug',
            'latitude',
            'longitude',
            'alamat',
            'deskripsi'
        )

class ItemKamarSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemKamar
        fields = (
            'id_kamar',
            'penginapan',
            'jenis',
            'type_ranjang',
            'fasilitas',
            'harga',
            'available'
        )