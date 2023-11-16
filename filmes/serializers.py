from .models import Filme, Usuario
from rest_framework import serializers

class FilmeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Filme
        lookup_field = "uuid"
        fields = [
            "uuid",
            "usuario",
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

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"
