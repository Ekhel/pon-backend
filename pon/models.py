from django.db import models
from django.conf import settings

class Kota(models.Model):
    id_kota = models.AutoField(primary_key=True)
    nama_kota = models.CharField(max_length=50)

    class Meta:
        ordering = ('id_kota',)

    def __str__(self):
        return self.nama_kota

    
class Kategori_kuliner(models.Model):
    id_kk = models.AutoField(primary_key=True)
    kategori = models.CharField(max_length=50)

    class Meta:
        ordering = ('id_kk',)

    def __str__(self):
        return self.kategori

    
class Kuliner(models.Model):
    id_kuliner = models.AutoField(primary_key=True)
    kategori = models.ForeignKey(Kategori_kuliner, on_delete=models.CASCADE)
    kota = models.ForeignKey(Kota, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    latitude = models.CharField(max_length=128)
    longitude = models.CharField(max_length=128)
    jam_buka = models.TimeField(auto_now_add=False)
    jam_tutup = models.TimeField(auto_now_add=False)
    alamat = models.CharField(max_length=250)
    deskripsi = models.TextField()

    class Meta:
        ordering = ('id_kuliner',)

    def __str__(self):
        return self.title


class Item_Kuliner(models.Model):
    id_item = models.AutoField(primary_key=True)
    kuliner = models.ForeignKey(Kuliner, on_delete=models.CASCADE)
    item = models.CharField(max_length=250)
    harga = models.DecimalField(max_digits=12, decimal_places=0)
    available = models.BooleanField(default=True)
    slug = models.SlugField(max_length=250, blank=True)
    class Meta:
        ordering = ('id_item',)

    def __str__(self):
        return self.item


class Kategori_penginapan(models.Model):
    id_kp = models.AutoField(primary_key=True)
    kp = models.CharField(max_length=50)

    class Meta:
        ordering = ('id_kp',)

    def __str__(self):
        return self.kp

    
class Penginapan(models.Model):
    id_penginapan = models.AutoField(primary_key=True)
    kategori = models.ForeignKey(Kategori_penginapan, on_delete=models.CASCADE)
    kota = models.ForeignKey(Kota, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, blank=True)
    latitude = models.CharField(max_length=128)
    longitude = models.CharField(max_length=128)
    alamat = models.CharField(max_length=250)
    deskripsi = models.TextField()

    class Meta:
        ordering = ('id_penginapan',)

    def __str__(self):
        return self.title


class Fasilitas(models.Model):
    id_fasilitas = models.AutoField(primary_key=True)
    item_fasilitas = models.CharField(max_length=100)

    def __str__(self):
        return self.item_fasilitas

class ItemKamar(models.Model):
    id_kamar = models.AutoField(primary_key=True)
    penginapan = models.ForeignKey(Penginapan, on_delete=models.CASCADE)
    jenis = models.CharField(max_length=150)
    type_ranjang = models.CharField(max_length=100)
    fasilitas = models.ManyToManyField('Fasilitas')
    harga = models.DecimalField(max_digits=12, decimal_places=0)
    available = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('id_kamar',)

    def __str__(self):
        return self.jenis
    


