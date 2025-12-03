from django.db import models


class Autor(models.Model):
    """Modelo para representar um Autor."""
    nome = models.CharField(max_length=200, verbose_name='Nome')

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Editora(models.Model):
    """Modelo para representar uma Editora."""
    nome = models.CharField(max_length=200, verbose_name='Nome')

    class Meta:
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Livro(models.Model):
    """Modelo para representar um Livro."""
    titulo = models.CharField(max_length=300, verbose_name='Título')
    publicacao = models.DateField(verbose_name='Data de Publicação')
    preco = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')
    estoque = models.IntegerField(default=0, verbose_name='Estoque')
    editora = models.ForeignKey(
        Editora,
        on_delete=models.CASCADE,
        related_name='livros',
        verbose_name='Editora'
    )

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo


class Publica(models.Model):
    """Modelo para representar o relacionamento entre Livro e Autor (Publicação)."""
    livro = models.ForeignKey(
        Livro,
        on_delete=models.CASCADE,
        related_name='publicacoes',
        verbose_name='Livro'
    )
    autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name='publicacoes',
        verbose_name='Autor'
    )

    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'
        unique_together = ['livro', 'autor']
        ordering = ['livro__titulo', 'autor__nome']

    def __str__(self):
        return f'{self.livro.titulo} - {self.autor.nome}'
