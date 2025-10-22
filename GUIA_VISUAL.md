# Prática 05 - Guia Visual Rápido

## 🎯 Objetivo
Sistema CRUD completo com Django ModelForm para gerenciar biblioteca (Autores, Editoras, Livros e Publicações).

## 📊 Diagrama do Banco de Dados

```
┌─────────────┐         ┌──────────────┐         ┌─────────────┐
│   Autor     │         │   Publica    │         │   Livro     │
├─────────────┤         ├──────────────┤         ├─────────────┤
│ id INT      │────┐    │ livro_id FK  │    ┌────│ id INT      │
│ nome VARCHAR│    └────│ autor_id FK  │────┘    │ titulo      │
└─────────────┘         └──────────────┘         │ publicacao  │
                                                  │ preco       │
                                                  │ estoque     │
                        ┌─────────────┐          │ editora_id  │
                        │  Editora    │          └──────┬──────┘
                        ├─────────────┤                 │
                        │ id INT      │─────────────────┘
                        │ nome VARCHAR│
                        └─────────────┘
```

## 🚀 Quick Start

### Opção 1: Script Automático
```powershell
.\setup.ps1
```

### Opção 2: Manual
```powershell
# 1. Instalar Django
pip install -r requirements.txt

# 2. Configurar banco
python manage.py makemigrations
python manage.py migrate

# 3. Popular com dados de exemplo (opcional)
python manage.py shell < populate_db.py

# 4. Criar admin (opcional)
python manage.py createsuperuser

# 5. Rodar servidor
python manage.py runserver
```

## 📱 URLs da Aplicação

| Recurso     | URL                              |
|-------------|----------------------------------|
| Home        | http://localhost:8000/           |
| Admin       | http://localhost:8000/admin/     |
| Autores     | http://localhost:8000/autores/   |
| Editoras    | http://localhost:8000/editoras/  |
| Livros      | http://localhost:8000/livros/    |
| Publicações | http://localhost:8000/publicacoes/ |

## ✨ Funcionalidades por Entidade

### Autor
- ✅ Listar todos (`/autores/`)
- ✅ Criar novo (`/autores/criar/`)
- ✅ Editar (`/autores/<id>/editar/`)
- ✅ Excluir (`/autores/<id>/excluir/`)

### Editora
- ✅ Listar todas (`/editoras/`)
- ✅ Criar nova (`/editoras/criar/`)
- ✅ Editar (`/editoras/<id>/editar/`)
- ✅ Excluir (`/editoras/<id>/excluir/`)

### Livro
- ✅ Listar todos (`/livros/`)
- ✅ Criar novo (`/livros/criar/`)
- ✅ Editar (`/livros/<id>/editar/`)
- ✅ Excluir (`/livros/<id>/excluir/`)

### Publicação (Livro-Autor)
- ✅ Listar todas (`/publicacoes/`)
- ✅ Criar nova (`/publicacoes/criar/`)
- ✅ Editar (`/publicacoes/<id>/editar/`)
- ✅ Excluir (`/publicacoes/<id>/excluir/`)

## 📂 Arquivos Principais

```
pratica-05/
│
├── 📄 manage.py              ← Gerenciador Django
├── 📄 requirements.txt       ← Dependências
├── 📄 README.md             ← Doc completa
├── 📄 INSTRUCOES.md         ← Instruções detalhadas
├── 📄 populate_db.py        ← Popular BD
├── 📄 setup.ps1             ← Setup automático
│
├── 📁 config/               ← Configurações
│   ├── settings.py          ← Settings principais
│   └── urls.py              ← URLs raiz
│
└── 📁 biblioteca/           ← App principal
    ├── models.py            ← 4 Models (Autor, Editora, Livro, Publica)
    ├── forms.py             ← 4 ModelForms
    ├── views.py             ← 16 Views (4 CRUDs completos)
    ├── urls.py              ← URLs do app
    ├── admin.py             ← Admin config
    └── templates/
        └── biblioteca/
            ├── base.html                    ← Base template
            ├── home.html                    ← Dashboard
            ├── autor_*.html                 ← 3 templates
            ├── editora_*.html               ← 3 templates
            ├── livro_*.html                 ← 3 templates
            └── publica_*.html               ← 3 templates
```

## 🎨 Tecnologias

- **Backend**: Django 5.0+
- **Frontend**: Bootstrap 5 + Bootstrap Icons
- **Database**: SQLite3
- **Forms**: Django ModelForm
- **Admin**: Django Admin

## ⚡ Features Especiais

- ✅ **RAD (Rapid Application Development)** - ModelForm agiliza desenvolvimento
- ✅ **Interface Responsiva** - Bootstrap 5
- ✅ **Validação Automática** - Django ModelForm
- ✅ **Mensagens de Feedback** - Success/Error/Warning
- ✅ **Confirmação de Exclusão** - Evita exclusões acidentais
- ✅ **Admin Configurado** - Interface administrativa pronta
- ✅ **Testes Unitários** - Testes para todos os models

## 🐛 Solução de Problemas

### Erro: "No space left on device"
```powershell
# Limpar cache do pip
pip cache purge

# Liberar espaço no disco Z:\
```

### Erro: "Django not found"
```powershell
# Instalar Django
pip install django
```

### Erro: "Table doesn't exist"
```powershell
# Rodar migrações
python manage.py makemigrations
python manage.py migrate
```

## 📝 Comandos Úteis

```powershell
# Ver migrações
python manage.py showmigrations

# Criar superusuário
python manage.py createsuperuser

# Rodar testes
python manage.py test

# Shell interativo
python manage.py shell

# Coletar static files
python manage.py collectstatic
```

## 🎓 Conceitos Aplicados

1. **Django ORM** - Models com relacionamentos
2. **ModelForm** - Formulários automáticos
3. **Class-Based Views** - Function-Based Views
4. **Template Inheritance** - Reutilização de código
5. **CRUD Operations** - Create, Read, Update, Delete
6. **Foreign Keys** - Relacionamentos 1:N
7. **Many-to-Many** - Relacionamentos N:N através de Publica
8. **Django Admin** - Interface administrativa

---

**Desenvolvido para Prática 05 - RAD (Rapid Application Development)**
