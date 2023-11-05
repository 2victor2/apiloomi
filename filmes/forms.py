from django import forms
from .models import Filme

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = [
            'titulo',
            'descricao',
            'link_imagem',
            'data_de_lancamento',
            'diretores',
            'roteiristas',
            'atores',
            'generos',
            'comentarios',
            'estrelas',
            'favorito',
            'status',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['csrfmiddlewaretoken'] = forms.CharField(widget=forms.HiddenInput())
