from .models import Filme, Usuario
from rest_framework import serializers
from drf_spectacular.utils import extend_schema_serializer, OpenApiExample


@extend_schema_serializer(
    exclude_fields=('usuario',), # schema ignore these fields
    examples = [
         OpenApiExample(
            'Exemplo de criação',
            value={
                "titulo": "string",
                "descricao": "string",
                "link_imagem": "string",
                "data_de_lancamento": "2023-11-16",
                "diretores": "string",
                "roteiristas": "string",
                "atores": "string",
                "generos": "string",
                "comentarios": "string",
                "estrelas": 4,
                "favorito": True,
                "status": "string"
            },
            request_only=True, # signal that example only applies to requests
        ),
    ]
)
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
