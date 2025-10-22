# Prática 05 - Django ModelForm e CRUD

> 📚 **Documentação Completa:** Veja o [INDICE.md](INDICE.md) para navegar por toda a documentação disponível.

## Objetivo
Implementação de formulários dinâmicos com Django ModelForm e CRUDs completos para gerenciar registros de Autor, Editora, Livro e Publica.

## Diagrama do Banco de Dados
```
Autor (id, nome)
Editora (id, nome)
Livro (id, titulo, publicacao, preco, estoque, editora_id)
Publica (livro_id, autor_id)
```

## Estrutura do Projeto
```
pratica05/
├── manage.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── biblioteca/
    ├── models.py
    ├── forms.py
    ├── views.py
    ├── urls.py
    └── templates/
        └── biblioteca/
            ├── base.html
            ├── home.html
            ├── autor_list.html
            ├── autor_form.html
            ├── editora_list.html
            ├── editora_form.html
            ├── livro_list.html
            ├── livro_form.html
            ├── publica_list.html
            └── publica_form.html
```

## Como Executar

### 1. Liberar espaço em disco e criar ambiente virtual
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows PowerShell
```

### 2. Instalar dependências
```bash
pip install -r requirements.txt
```

### 3. Criar o projeto Django
```bash
django-admin startproject config .
python manage.py startapp biblioteca
```

### 4. Aplicar migrações
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Criar superusuário (opcional)
```bash
python manage.py createsuperuser
```

### 6. Executar o servidor
```bash
python manage.py runserver
```

### 7. Acessar a aplicação
- Home: http://localhost:8000/
- Admin: http://localhost:8000/admin/
- Autores: http://localhost:8000/autores/
- Editoras: http://localhost:8000/editoras/
- Livros: http://localhost:8000/livros/
- Publicações: http://localhost:8000/publicacoes/

## Funcionalidades Implementadas

### CRUD Autor
- Listar todos os autores
- Criar novo autor
- Editar autor existente
- Excluir autor

### CRUD Editora
- Listar todas as editoras
- Criar nova editora
- Editar editora existente
- Excluir editora

### CRUD Livro
- Listar todos os livros
- Criar novo livro
- Editar livro existente
- Excluir livro
- Campos: título, publicação, preço, estoque, editora

### CRUD Publica (Relacionamento Livro-Autor)
- Listar todas as publicações
- Criar nova publicação
- Editar publicação existente
- Excluir publicação

## Observações
- **Django ModelForm**: Todos os formulários utilizam ModelForm
- **RAD (Rapid Application Development)**: Uso de Django Admin e ModelForm para agilizar o desenvolvimento
- **Bootstrap**: Interface moderna e responsiva
- **Validações**: Validações automáticas do Django ModelForm
