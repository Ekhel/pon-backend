from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView
from .models import Kota, Kuliner, Penginapan

def login(request):
    return render(request,'auth/login.html')

@login_required
def dashboard(request):
    return render(request, 'layout/dashboard.html')

class KotaView(ListView):
    template_name = 'layout/r-kota.html';
    model = Kota

class KulinerView(ListView):
    template_name = 'layout/r-kuliner.html';
    model = Kuliner

class PenginapanView(ListView):
    template_name = 'layout/r-penginapan.html';
    model = Penginapan


