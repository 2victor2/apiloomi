from rest_framework import serializers
from .models import Filme

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = [
            "id",
            "titulo",
            "descricao",
            "link_imagem",
            "data_de_lancamento",
            "diretores",
            "roteiristas",
            "atores",
            "generos",
            "comentarios",
            "estrelas",
            "favorito",
            "status",
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["diretores"] = instance.diretores.split(", ")
        representation["roteiristas"] = instance.roteiristas.split(", ")
        representation["atores"] = instance.atores.split(", ")
        representation["generos"] = instance.generos.split(", ")
        return representation