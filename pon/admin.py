from django.contrib import admin
from django.db.models import Count
from pon.models import (
    Kota, 
    Kategori_kuliner, 
    Kuliner, 
    Item_Kuliner,
    Kategori_penginapan,
    Penginapan,
    ItemKamar,
    Fasilitas
)
from django_summernote.admin import SummernoteModelAdmin

class PageKota(admin.ModelAdmin):
    list_display = ('id_kota','nama_kota')
    search_fields = ('id_kota','nama_kota')
    list_per_page = 10

class PageKategoriKuliner(admin.ModelAdmin):
    list_display = ('id_kk','kategori')
    search_fields = ('id_kk','kategori')
    list_per_page = 10

class ItemInline(admin.StackedInline):
    model = Item_Kuliner
    fields = ('item', 'harga', 'available')
    extra = 1
    classes = ('collapse', )

class PageKuliner(SummernoteModelAdmin):
    list_display = ('kategori','title','kota','jam_buka','jam_tutup','alamat','jumlah_item')
    search_fields = ('id_kuliner','title')
    list_filter = ('kategori', 'kota', )
    list_per_page = 10
    summernote_fields = ('deskripsi',)
    inlines = (ItemInline, )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(items_count=Count('item_kuliner'))
        return queryset
    
    def jumlah_item(self, kuliner):
        return kuliner.items_count


class PageItemKuliner(admin.ModelAdmin):
    list_display = ('item','kuliner','harga','available')
    search_fields = ('item','kuliner','harga','available')
    list_filter = ('available',)
    prepopulated_fields = {'slug': ('item', )}
    actions = ('set_item_available_true', )
    list_editable = ('available', )
    list_per_page = 10

    def set_item_available_true(self, request, queryset):
        count = queryset.update(available=True)
        self.message_user(request, '{} Item Sudah di Set TERSEDIA'.format(count))


class PageKaterogiPenginapan(admin.ModelAdmin):
    list_display = ('id_kp','kp')
    list_per_page = 10

    class Meta:
        ordering = ('id_kp',)


class PagePenginaapan(admin.ModelAdmin):
    list_display = ('id_penginapan','title','kategori','kota','alamat')
    search_fields = ('id_penginapan','title')
    prepopulated_fields = {'slug': ('title', )}
    list_filter = ('kategori', 'kota', )
    list_per_page = 10

class PageItemKamar(admin.ModelAdmin):
    list_display = ('id_kamar','penginapan','jenis','harga')
    search_fields = ('id_kamar','jenis')
    list_filter = ('penginapan', )
    list_per_page = 10

admin.site.register(Kota, PageKota)
admin.site.register(Kategori_kuliner, PageKategoriKuliner)
admin.site.register(Kuliner, PageKuliner)
admin.site.register(Item_Kuliner, PageItemKuliner)
admin.site.register(Kategori_penginapan, PageKaterogiPenginapan)
admin.site.register(Penginapan, PagePenginaapan)
admin.site.register(ItemKamar, PageItemKamar)
admin.site.register(Fasilitas)
