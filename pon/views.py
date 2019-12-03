from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView
from .models import (
    Kota, 
    Kuliner, 
    Kategori_kuliner,
    Item_Kuliner,
    Kategori_penginapan,
    Penginapan,
    ItemKamar
)

def login(request):
    return render(request,'auth/login.html')

@login_required
def dashboard(request):
    return render(request, 'layout/dashboard.html')

class KotaView(ListView):
    template_name = 'layout/r-kota.html';
    model = Kota

# Kuliner

class KatergoriKulinerView(ListView):
    template_name = 'layout/r-kategori-kuliner.html';
    model = Kategori_kuliner

class KulinerView(ListView):
    template_name = 'layout/r-kuliner.html';
    model = Kuliner

class ItemKulinerView(ListView):
    template_name = 'layout/r-item-kuliner.html';
    model = Item_Kuliner

# End Kuliner

# Penginapan
class KategoriPenginapanView(ListView):
    template_name = 'layout/r-kategori-penginapan.html';
    model = Kategori_penginapan

class PenginapanView(ListView):
    template_name = 'layout/r-penginapan.html';
    model = Penginapan

class ItemKamarView(ListView):
    template_name ='layout/r-item-kamar.html';
    model = ItemKamar


