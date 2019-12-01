from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from . views import (
    KotaView,
    KulinerView,
    PenginapanView,
)

from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('login', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('kota', login_required(KotaView.as_view()), name='kota'),
    path('kuliner', login_required(KulinerView.as_view()), name='kuliner'),
    path('penginapan', login_required(PenginapanView.as_view()), name='penginapan'),
]