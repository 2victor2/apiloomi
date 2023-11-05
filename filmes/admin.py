from django.contrib import admin
from .models import Filme

class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao_preview', 'data_de_lancamento', 'estrelas', 'favorito', 'status', 'diretores', 'roteiristas', 'atores', 'generos', 'usuario')
    list_filter = ('favorito', 'status', 'usuario')
    search_fields = ('titulo', 'descricao', 'diretores', 'roteiristas', 'atores', 'generos')

    def descricao_preview(self, obj):
        if obj.descricao and len(obj.descricao) > 123:
            return f'{obj.descricao[:123]}...'
        return obj.descricao

    descricao_preview.short_description = 'Descrição'

admin.site.register(Filme, FilmeAdmin)
