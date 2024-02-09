from django.contrib import admin

# Register your models here.
from .models import Doce, Categoria


class DoceAdmin(admin.ModelAdmin):
    list_display = ['nome', 'categoria', 'ativo', 'quantidade', 'valor']
    list_editable = ['ativo', 'quantidade', 'valor']
    list_display_links = ['nome', 'categoria']


admin.site.register(Doce, DoceAdmin)
admin.site.register(Categoria)
