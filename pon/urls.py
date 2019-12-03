from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . views import (
    KotaView,
    KatergoriKulinerView,
    KulinerView,
    ItemKulinerView,
    KategoriPenginapanView,
    PenginapanView,
    ItemKamarView,
)

from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('login', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('kota', login_required(KotaView.as_view()), name='kota'),
    path('kategori_kuliner', login_required(KatergoriKulinerView.as_view()), name='kategori_kuliner'),
    path('kuliner', login_required(KulinerView.as_view()), name='kuliner'),
    path('item_kuliner', login_required(ItemKulinerView.as_view()), name='item_kuliner'),
    path('kategori_penginapan', login_required(KategoriPenginapanView.as_view()), name='kategori_penginapan'),
    path('penginapan', login_required(PenginapanView.as_view()), name='penginapan'),
    path('item_kamar', login_required(ItemKamarView.as_view()), name='item_kamar'),
]