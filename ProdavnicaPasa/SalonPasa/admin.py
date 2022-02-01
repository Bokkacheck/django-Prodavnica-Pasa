from django.contrib import admin
from .models import TipPsa,Pas

@admin.register(TipPsa)
class TipPsaAdmin(admin.ModelAdmin):
    list_display = ['naziv', 'slug']
    prepopulated_fields = {'slug': ('naziv',)}
@admin.register(Pas)
class PasAdmin(admin.ModelAdmin):
    list_display = ['naziv', 'slug', 'cena',
    'raspoloziv', 'kreiran', 'azuriran']
    list_filter = ['raspoloziv', 'kreiran', 'azuriran']
    list_editable = ['cena', 'raspoloziv']
    prepopulated_fields = {'slug': ('naziv',)}