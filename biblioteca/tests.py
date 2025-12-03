from django.test import TestCase
from .models import Autor, Editora, Livro, Publica
from datetime import date


class AutorModelTest(TestCase):
    def test_criar_autor(self):
        autor = Autor.objects.create(nome="Machado de Assis")
        self.assertEqual(autor.nome, "Machado de Assis")
        self.assertEqual(str(autor), "Machado de Assis")


class EditoraModelTest(TestCase):
    def test_criar_editora(self):
        editora = Editora.objects.create(nome="Companhia das Letras")
        self.assertEqual(editora.nome, "Companhia das Letras")
        self.assertEqual(str(editora), "Companhia das Letras")


class LivroModelTest(TestCase):
    def setUp(self):
        self.editora = Editora.objects.create(nome="Companhia das Letras")
    
    def test_criar_livro(self):
        livro = Livro.objects.create(
            titulo="Dom Casmurro",
            publicacao=date(1899, 1, 1),
            preco=29.90,
            estoque=15,
            editora=self.editora
        )
        self.assertEqual(livro.titulo, "Dom Casmurro")
        self.assertEqual(livro.editora.nome, "Companhia das Letras")
        self.assertEqual(str(livro), "Dom Casmurro")


class PublicaModelTest(TestCase):
    def setUp(self):
        self.autor = Autor.objects.create(nome="Machado de Assis")
        self.editora = Editora.objects.create(nome="Companhia das Letras")
        self.livro = Livro.objects.create(
            titulo="Dom Casmurro",
            publicacao=date(1899, 1, 1),
            preco=29.90,
            estoque=15,
            editora=self.editora
        )
    
    def test_criar_publica(self):
        publica = Publica.objects.create(
            livro=self.livro,
            autor=self.autor
        )
        self.assertEqual(publica.livro.titulo, "Dom Casmurro")
        self.assertEqual(publica.autor.nome, "Machado de Assis")
        self.assertEqual(str(publica), "Dom Casmurro - Machado de Assis")
