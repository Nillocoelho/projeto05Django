from django.contrib import admin
from .models import Autor, Editora, Livro, Publica


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']
    ordering = ['nome']


@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome']
    search_fields = ['nome']
    ordering = ['nome']


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'publicacao', 'preco', 'estoque', 'editora']
    list_filter = ['editora', 'publicacao']
    search_fields = ['titulo']
    ordering = ['titulo']


@admin.register(Publica)
class PublicaAdmin(admin.ModelAdmin):
    list_display = ['id', 'livro', 'autor']
    list_filter = ['autor', 'livro']
    search_fields = ['livro__titulo', 'autor__nome']
    ordering = ['livro__titulo', 'autor__nome']
