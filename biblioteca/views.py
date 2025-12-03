from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Autor, Editora, Livro, Publica
from .forms import AutorForm, EditoraForm, LivroForm, PublicaForm


def home(request):
    """View para a página inicial com estatísticas."""
    context = {
        'total_autores': Autor.objects.count(),
        'total_editoras': Editora.objects.count(),
        'total_livros': Livro.objects.count(),
        'total_publicacoes': Publica.objects.count(),
    }
    return render(request, 'biblioteca/home.html', context)


# ==================== CRUD AUTOR ====================

def autor_list(request):
    """Lista todos os autores."""
    autores = Autor.objects.all()
    return render(request, 'biblioteca/autor_list.html', {'autores': autores})


def autor_create(request):
    """Cria um novo autor."""
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor criado com sucesso!')
            return redirect('autor_list')
    else:
        form = AutorForm()
    return render(request, 'biblioteca/autor_form.html', {'form': form, 'titulo': 'Novo Autor'})


def autor_update(request, pk):
    """Edita um autor existente."""
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor atualizado com sucesso!')
            return redirect('autor_list')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'biblioteca/autor_form.html', {'form': form, 'titulo': 'Editar Autor'})


def autor_delete(request, pk):
    """Exclui um autor."""
    autor = get_object_or_404(Autor, pk=pk)
    if request.method == 'POST':
        autor.delete()
        messages.success(request, 'Autor excluído com sucesso!')
        return redirect('autor_list')
    return render(request, 'biblioteca/autor_confirm_delete.html', {'autor': autor})


# ==================== CRUD EDITORA ====================

def editora_list(request):
    """Lista todas as editoras."""
    editoras = Editora.objects.all()
    return render(request, 'biblioteca/editora_list.html', {'editoras': editoras})


def editora_create(request):
    """Cria uma nova editora."""
    if request.method == 'POST':
        form = EditoraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editora criada com sucesso!')
            return redirect('editora_list')
    else:
        form = EditoraForm()
    return render(request, 'biblioteca/editora_form.html', {'form': form, 'titulo': 'Nova Editora'})


def editora_update(request, pk):
    """Edita uma editora existente."""
    editora = get_object_or_404(Editora, pk=pk)
    if request.method == 'POST':
        form = EditoraForm(request.POST, instance=editora)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editora atualizada com sucesso!')
            return redirect('editora_list')
    else:
        form = EditoraForm(instance=editora)
    return render(request, 'biblioteca/editora_form.html', {'form': form, 'titulo': 'Editar Editora'})


def editora_delete(request, pk):
    """Exclui uma editora."""
    editora = get_object_or_404(Editora, pk=pk)
    if request.method == 'POST':
        editora.delete()
        messages.success(request, 'Editora excluída com sucesso!')
        return redirect('editora_list')
    return render(request, 'biblioteca/editora_confirm_delete.html', {'editora': editora})


# ==================== CRUD LIVRO ====================

def livro_list(request):
    """Lista todos os livros."""
    livros = Livro.objects.select_related('editora').all()
    return render(request, 'biblioteca/livro_list.html', {'livros': livros})


def livro_create(request):
    """Cria um novo livro."""
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro criado com sucesso!')
            return redirect('livro_list')
    else:
        form = LivroForm()
    return render(request, 'biblioteca/livro_form.html', {'form': form, 'titulo': 'Novo Livro'})


def livro_update(request, pk):
    """Edita um livro existente."""
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livro atualizado com sucesso!')
            return redirect('livro_list')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'biblioteca/livro_form.html', {'form': form, 'titulo': 'Editar Livro'})


def livro_delete(request, pk):
    """Exclui um livro."""
    livro = get_object_or_404(Livro, pk=pk)
    if request.method == 'POST':
        livro.delete()
        messages.success(request, 'Livro excluído com sucesso!')
        return redirect('livro_list')
    return render(request, 'biblioteca/livro_confirm_delete.html', {'livro': livro})


# ==================== CRUD PUBLICA ====================

def publica_list(request):
    """Lista todas as publicações."""
    publicacoes = Publica.objects.select_related('livro', 'autor').all()
    return render(request, 'biblioteca/publica_list.html', {'publicacoes': publicacoes})


def publica_create(request):
    """Cria uma nova publicação."""
    if request.method == 'POST':
        form = PublicaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Publicação criada com sucesso!')
            return redirect('publica_list')
    else:
        form = PublicaForm()
    return render(request, 'biblioteca/publica_form.html', {'form': form, 'titulo': 'Nova Publicação'})


def publica_update(request, pk):
    """Edita uma publicação existente."""
    publica = get_object_or_404(Publica, pk=pk)
    if request.method == 'POST':
        form = PublicaForm(request.POST, instance=publica)
        if form.is_valid():
            form.save()
            messages.success(request, 'Publicação atualizada com sucesso!')
            return redirect('publica_list')
    else:
        form = PublicaForm(instance=publica)
    return render(request, 'biblioteca/publica_form.html', {'form': form, 'titulo': 'Editar Publicação'})


def publica_delete(request, pk):
    """Exclui uma publicação."""
    publica = get_object_or_404(Publica, pk=pk)
    if request.method == 'POST':
        publica.delete()
        messages.success(request, 'Publicação excluída com sucesso!')
        return redirect('publica_list')
    return render(request, 'biblioteca/publica_confirm_delete.html', {'publica': publica})
