from django.contrib import admin
from cars.models import Car, Brand

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value', 'photo') #Para aparecer os campos das tabelas
    search_fields = ('model', 'brand' ) # Para pesquisar por aquele campo


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search = ('name',)

admin.site.register(Car, CarAdmin)
admin.site.register(Brand, BrandAdmin)