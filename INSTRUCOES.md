# INSTRUÇÕES PARA EXECUTAR A PRÁTICA 05

## PROBLEMA: Espaço em disco insuficiente

Seu disco Z:\ está sem espaço. Antes de continuar, você precisa:

1. **Liberar espaço em disco** (pelo menos 100MB)
2. **Limpar o cache do pip**: `pip cache purge`
3. **Remover pastas temporárias** desnecessárias

## PASSO A PASSO APÓS LIBERAR ESPAÇO

### 1. Ativar o ambiente virtual (se já criado)
```powershell
cd z:\20222370031\Documents\.rad-praticas\pratica-05
.\venv\Scripts\Activate.ps1
```

### 2. Instalar Django
```powershell
pip install -r requirements.txt
```

### 3. Aplicar migrações
```powershell
python manage.py makemigrations
python manage.py migrate
```

### 4. (Opcional) Criar superusuário para acessar o Admin
```powershell
python manage.py createsuperuser
```
- Username: admin
- Email: admin@example.com
- Password: admin (ou qualquer senha)

### 5. (Opcional) Popular banco com dados de exemplo
```powershell
python manage.py shell < populate_db.py
```

### 6. Executar o servidor
```powershell
python manage.py runserver
```

### 7. Acessar a aplicação
- **Home**: http://localhost:8000/
- **Django Admin**: http://localhost:8000/admin/
- **Autores**: http://localhost:8000/autores/
- **Editoras**: http://localhost:8000/editoras/
- **Livros**: http://localhost:8000/livros/
- **Publicações**: http://localhost:8000/publicacoes/

## ALTERNATIVA: Usar script automatizado
```powershell
.\setup.ps1
```

## ESTRUTURA DO PROJETO

```
pratica-05/
├── manage.py                    # Script principal do Django
├── requirements.txt             # Dependências Python
├── README.md                    # Documentação principal
├── INSTRUCOES.md               # Este arquivo
├── populate_db.py              # Script para popular BD
├── setup.ps1                   # Script de setup automático
├── .gitignore                  # Arquivos ignorados pelo Git
├── db.sqlite3                  # Banco de dados (criado após migrate)
├── config/                     # Configurações do Django
│   ├── __init__.py
│   ├── settings.py             # Configurações gerais
│   ├── urls.py                 # URLs principais
│   ├── asgi.py
│   └── wsgi.py
└── biblioteca/                 # App principal
    ├── __init__.py
    ├── admin.py                # Configuração do Django Admin
    ├── apps.py
    ├── models.py               # Modelos (Autor, Editora, Livro, Publica)
    ├── forms.py                # Forms com ModelForm
    ├── views.py                # Views (CRUDs)
    ├── urls.py                 # URLs do app
    ├── tests.py                # Testes unitários
    ├── migrations/             # Migrações do banco
    └── templates/
        └── biblioteca/
            ├── base.html                    # Template base
            ├── home.html                    # Página inicial
            ├── autor_list.html              # Lista autores
            ├── autor_form.html              # Form criar/editar autor
            ├── autor_confirm_delete.html    # Confirmar exclusão
            ├── editora_list.html            # Lista editoras
            ├── editora_form.html            # Form criar/editar editora
            ├── editora_confirm_delete.html  # Confirmar exclusão
            ├── livro_list.html              # Lista livros
            ├── livro_form.html              # Form criar/editar livro
            ├── livro_confirm_delete.html    # Confirmar exclusão
            ├── publica_list.html            # Lista publicações
            ├── publica_form.html            # Form criar/editar publicação
            └── publica_confirm_delete.html  # Confirmar exclusão
```

## FEATURES IMPLEMENTADAS

✅ **Models** (models.py):
- Autor (id, nome)
- Editora (id, nome)
- Livro (id, titulo, publicacao, preco, estoque, editora_id)
- Publica (livro_id, autor_id) - relacionamento many-to-many

✅ **Forms com ModelForm** (forms.py):
- AutorForm
- EditoraForm
- LivroForm
- PublicaForm
- Todos com widgets Bootstrap

✅ **Views CRUD Completo** (views.py):
- Create (criar)
- Read (listar)
- Update (editar)
- Delete (excluir)
- Para todas as entidades

✅ **Templates Bootstrap 5**:
- Interface moderna e responsiva
- Mensagens de feedback
- Validação de formulários
- Confirmação de exclusão

✅ **Django Admin**:
- Todas as entidades registradas
- Filtros e busca configurados
- Interface administrativa completa

✅ **Testes Unitários** (tests.py):
- Testes para todos os models
- Testes de criação e relacionamentos

## OBSERVAÇÕES

- ✅ Usa Django ModelForm (requisito da prática)
- ✅ RAD - Rapid Application Development
- ✅ Interface moderna com Bootstrap 5
- ✅ Todas as entidades do diagrama implementadas
- ✅ CRUDs completos
- ✅ Validações automáticas do Django
- ✅ Mensagens de feedback para usuário
- ✅ Confirmação antes de excluir

## PRÓXIMOS PASSOS

1. Libere espaço em disco
2. Execute: `pip install -r requirements.txt`
3. Execute: `python manage.py migrate`
4. Execute: `python manage.py runserver`
5. Acesse: http://localhost:8000/

Boa prática! 🚀
