from pon.api.views import KotaViewSet, KulinerViewSet, PenginapanViewSet, ItemKamarViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'kota', KotaViewSet, basename='kota')
router.register(r'kuliner', KulinerViewSet, basename='kuliner')
router.register(r'penginapan', PenginapanViewSet, basename="penginaapan")
router.register(r'kamar', ItemKamarViewSet, basename="kamar")

urlpatterns = router.urls