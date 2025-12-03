from django import forms
from .models import Autor, Editora, Livro, Publica


class AutorForm(forms.ModelForm):
    """Formulário para Autor usando ModelForm."""
    
    class Meta:
        model = Autor
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome do autor'
            })
        }


class EditoraForm(forms.ModelForm):
    """Formulário para Editora usando ModelForm."""
    
    class Meta:
        model = Editora
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome da editora'
            })
        }


class LivroForm(forms.ModelForm):
    """Formulário para Livro usando ModelForm."""
    
    class Meta:
        model = Livro
        fields = ['titulo', 'publicacao', 'preco', 'estoque', 'editora']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o título do livro'
            }),
            'publicacao': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'preco': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0'
            }),
            'estoque': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '0',
                'min': '0'
            }),
            'editora': forms.Select(attrs={
                'class': 'form-select'
            })
        }


class PublicaForm(forms.ModelForm):
    """Formulário para Publica usando ModelForm."""
    
    class Meta:
        model = Publica
        fields = ['livro', 'autor']
        widgets = {
            'livro': forms.Select(attrs={
                'class': 'form-select'
            }),
            'autor': forms.Select(attrs={
                'class': 'form-select'
            })
        }
