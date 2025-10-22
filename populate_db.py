# Script para popular o banco de dados com dados de exemplo
# Execute: python manage.py shell < populate_db.py

from biblioteca.models import Autor, Editora, Livro, Publica
from datetime import date

print("Limpando banco de dados...")
Publica.objects.all().delete()
Livro.objects.all().delete()
Autor.objects.all().delete()
Editora.objects.all().delete()

print("\nCriando Autores...")
autores = [
    Autor.objects.create(nome="Machado de Assis"),
    Autor.objects.create(nome="José de Alencar"),
    Autor.objects.create(nome="Clarice Lispector"),
    Autor.objects.create(nome="Jorge Amado"),
    Autor.objects.create(nome="Carlos Drummond de Andrade"),
]
print(f"✓ {len(autores)} autores criados")

print("\nCriando Editoras...")
editoras = [
    Editora.objects.create(nome="Companhia das Letras"),
    Editora.objects.create(nome="Record"),
    Editora.objects.create(nome="Globo Livros"),
    Editora.objects.create(nome="Saraiva"),
    Editora.objects.create(nome="Ática"),
]
print(f"✓ {len(editoras)} editoras criadas")

print("\nCriando Livros...")
livros = [
    Livro.objects.create(
        titulo="Dom Casmurro",
        publicacao=date(1899, 1, 1),
        preco=29.90,
        estoque=15,
        editora=editoras[0]
    ),
    Livro.objects.create(
        titulo="Memórias Póstumas de Brás Cubas",
        publicacao=date(1881, 1, 1),
        preco=32.50,
        estoque=10,
        editora=editoras[0]
    ),
    Livro.objects.create(
        titulo="Senhora",
        publicacao=date(1875, 1, 1),
        preco=25.00,
        estoque=8,
        editora=editoras[4]
    ),
    Livro.objects.create(
        titulo="A Hora da Estrela",
        publicacao=date(1977, 1, 1),
        preco=28.00,
        estoque=12,
        editora=editoras[1]
    ),
    Livro.objects.create(
        titulo="Capitães da Areia",
        publicacao=date(1937, 1, 1),
        preco=35.00,
        estoque=20,
        editora=editoras[0]
    ),
    Livro.objects.create(
        titulo="Sentimento do Mundo",
        publicacao=date(1940, 1, 1),
        preco=22.90,
        estoque=5,
        editora=editoras[0]
    ),
]
print(f"✓ {len(livros)} livros criados")

print("\nCriando Publicações (Livro-Autor)...")
publicacoes = [
    Publica.objects.create(livro=livros[0], autor=autores[0]),  # Dom Casmurro - Machado
    Publica.objects.create(livro=livros[1], autor=autores[0]),  # Memórias - Machado
    Publica.objects.create(livro=livros[2], autor=autores[1]),  # Senhora - José de Alencar
    Publica.objects.create(livro=livros[3], autor=autores[2]),  # A Hora da Estrela - Clarice
    Publica.objects.create(livro=livros[4], autor=autores[3]),  # Capitães - Jorge Amado
    Publica.objects.create(livro=livros[5], autor=autores[4]),  # Sentimento - Drummond
]
print(f"✓ {len(publicacoes)} publicações criadas")

print("\n" + "="*50)
print("✓ Banco de dados populado com sucesso!")
print("="*50)
print(f"\nResumo:")
print(f"  • {Autor.objects.count()} Autores")
print(f"  • {Editora.objects.count()} Editoras")
print(f"  • {Livro.objects.count()} Livros")
print(f"  • {Publica.objects.count()} Publicações")
print()
