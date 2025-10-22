# ❓ FAQ - Perguntas Frequentes - Prática 05

## 📋 Geral

### 1. O que é este projeto?
Sistema CRUD completo desenvolvido em Django usando ModelForm para gerenciar uma biblioteca (Autores, Editoras, Livros e Publicações).

### 2. Quais são os requisitos do projeto?
- Python 3.8+
- Django 5.0+
- ~100MB de espaço em disco
- Navegador web moderno

### 3. Por que não consigo instalar o Django?
**Erro comum:** "No space left on device"
**Solução:**
```powershell
# Limpar cache do pip
pip cache purge

# Liberar espaço no disco Z:\
# Depois tentar novamente:
pip install django
```

---

## 🚀 Instalação e Configuração

### 4. Como instalo o projeto?
```powershell
# Opção 1: Script automático
.\setup.ps1

# Opção 2: Manual
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 5. Como crio um superusuário?
```powershell
python manage.py createsuperuser
```
Preencha: username, email, password

### 6. Como popular o banco com dados de exemplo?
```powershell
python manage.py shell < populate_db.py
```

### 7. Qual a porta padrão do servidor?
**8000** - Acesse: http://localhost:8000/

Para usar outra porta:
```powershell
python manage.py runserver 8080
```

---

## 💻 Uso do Sistema

### 8. Como criar um novo autor?
1. Acesse http://localhost:8000/autores/
2. Clique em "Novo Autor"
3. Preencha o nome
4. Clique em "Salvar"

### 9. Como criar um livro?
1. Primeiro crie uma editora
2. Acesse http://localhost:8000/livros/
3. Clique em "Novo Livro"
4. Preencha todos os campos
5. Selecione a editora
6. Clique em "Salvar"

### 10. Como relacionar um autor a um livro?
1. Crie o autor e o livro primeiro
2. Acesse http://localhost:8000/publicacoes/
3. Clique em "Nova Publicação"
4. Selecione o livro e o autor
5. Clique em "Salvar"

### 11. Como editar um registro?
1. Vá para a lista (autores, editoras, livros ou publicações)
2. Clique no botão "Editar" do registro desejado
3. Altere os campos
4. Clique em "Salvar"

### 12. Como excluir um registro?
1. Vá para a lista
2. Clique no botão "Excluir"
3. Confirme a exclusão na página seguinte
4. Clique em "Sim, Excluir"

---

## 🐛 Problemas Comuns

### 13. Erro: "No module named django"
**Causa:** Django não está instalado
**Solução:**
```powershell
pip install django
```

### 14. Erro: "Table doesn't exist"
**Causa:** Migrações não foram aplicadas
**Solução:**
```powershell
python manage.py makemigrations
python manage.py migrate
```

### 15. Erro: "CSRF verification failed"
**Causa:** Template sem token CSRF
**Solução:** Adicione `{% csrf_token %}` no formulário:
```html
<form method="post">
    {% csrf_token %}
    <!-- campos do form -->
</form>
```

### 16. Erro: "Page not found (404)"
**Causa:** URL incorreta ou não configurada
**Solução:**
- Verifique se o servidor está rodando
- Verifique a URL no navegador
- Consulte as URLs em `urls.py`

### 17. Erro: "Static files not found"
**Causa:** Arquivos estáticos não coletados
**Solução:**
```powershell
python manage.py collectstatic
```

### 18. Erro: "Template does not exist"
**Causa:** Template não encontrado ou mal configurado
**Solução:**
- Verifique se o arquivo existe em `biblioteca/templates/biblioteca/`
- Verifique `INSTALLED_APPS` em `settings.py`

---

## 🔧 Desenvolvimento

### 19. Como adicionar um novo campo ao modelo?
1. Edite `models.py`:
```python
class Livro(models.Model):
    # ... campos existentes ...
    isbn = models.CharField(max_length=13, blank=True)  # novo campo
```

2. Crie e aplique migração:
```powershell
python manage.py makemigrations
python manage.py migrate
```

3. Atualize o form em `forms.py`:
```python
class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'publicacao', 'preco', 'estoque', 'editora', 'isbn']
```

### 20. Como adicionar validação personalizada?
Em `forms.py`:
```python
class LivroForm(forms.ModelForm):
    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco and preco < 0:
            raise forms.ValidationError('O preço não pode ser negativo.')
        return preco
```

### 21. Como adicionar um novo app?
```powershell
python manage.py startapp nome_do_app
```

Depois adicione em `settings.py`:
```python
INSTALLED_APPS = [
    # ...
    'nome_do_app',
]
```

### 22. Como fazer backup do banco de dados?
```powershell
# SQLite (copiar arquivo)
copy db.sqlite3 db_backup.sqlite3

# Ou usar dumpdata
python manage.py dumpdata > backup.json
```

### 23. Como restaurar backup?
```powershell
python manage.py loaddata backup.json
```

---

## 🎨 Interface

### 24. Como mudar as cores do template?
Edite `base.html` na seção `<style>`:
```css
.navbar {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    /* Mude as cores aqui */
}
```

### 25. Como adicionar mais ícones?
Use [Bootstrap Icons](https://icons.getbootstrap.com/):
```html
<i class="bi bi-star-fill"></i>
```

### 26. Como tornar o template responsivo?
Os templates já são responsivos com Bootstrap 5. Para customizar:
```html
<div class="col-12 col-md-6 col-lg-4">
    <!-- Conteúdo -->
</div>
```

---

## 📊 Dados

### 27. Como ver todos os registros no shell?
```powershell
python manage.py shell
```
```python
from biblioteca.models import *

# Ver todos
for autor in Autor.objects.all():
    print(autor.nome)

# Contar
print(Livro.objects.count())
```

### 28. Como fazer consultas avançadas?
```python
# Livros com preço entre 20 e 30
Livro.objects.filter(preco__gte=20, preco__lte=30)

# Livros de uma editora específica
Livro.objects.filter(editora__nome="Companhia das Letras")

# Autores que publicaram livros caros
Autor.objects.filter(publicacoes__livro__preco__gt=50).distinct()
```

### 29. Como exportar dados?
Veja [EXTENSOES.md](EXTENSOES.md) seção 6 - Exportar CSV/Excel.

---

## 🔐 Segurança

### 30. Como proteger rotas com login?
```python
from django.contrib.auth.decorators import login_required

@login_required
def livro_create(request):
    # ... código
```

### 31. Como mudar a SECRET_KEY?
Em `settings.py`:
```python
SECRET_KEY = 'nova-chave-super-secreta-e-aleatória'
```

**IMPORTANTE:** Nunca compartilhe a SECRET_KEY em produção!

### 32. Como ativar HTTPS?
Para desenvolvimento:
```powershell
python manage.py runserver_plus --cert-file cert.pem
```

Para produção, configure no servidor (Nginx, Apache).

---

## 🧪 Testes

### 33. Como rodar os testes?
```powershell
python manage.py test
```

### 34. Como testar apenas um app?
```powershell
python manage.py test biblioteca
```

### 35. Como ver mais detalhes dos testes?
```powershell
python manage.py test --verbosity=2
```

---

## 🚀 Deploy

### 36. Como fazer deploy em produção?
Opções:
- **Heroku:** https://devcenter.heroku.com/articles/django-app-configuration
- **PythonAnywhere:** https://help.pythonanywhere.com/pages/DeployExistingDjangoProject/
- **DigitalOcean:** https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu

### 37. Quais configurações mudar para produção?
```python
# settings.py
DEBUG = False
ALLOWED_HOSTS = ['seudominio.com']
SECRET_KEY = os.environ.get('SECRET_KEY')

# Usar PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # ... configurações
    }
}

# Configurar arquivos estáticos
STATIC_ROOT = BASE_DIR / 'staticfiles'
```

### 38. Como usar variáveis de ambiente?
```python
# settings.py
import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'default-key-for-dev')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
```

```powershell
# Windows PowerShell
$env:SECRET_KEY="minha-chave-secreta"
$env:DEBUG="False"
python manage.py runserver
```

---

## 📚 Documentação

### 39. Onde encontro mais documentação?
- [INDICE.md](INDICE.md) - Índice completo
- [README.md](README.md) - Visão geral
- [INSTRUCOES.md](INSTRUCOES.md) - Instalação
- [GUIA_VISUAL.md](GUIA_VISUAL.md) - Quick reference
- [DIAGRAMA.md](DIAGRAMA.md) - Arquitetura
- [TESTES.md](TESTES.md) - Guia de testes
- [EXTENSOES.md](EXTENSOES.md) - Melhorias sugeridas

### 40. Como contribuir com o projeto?
1. Fork o repositório
2. Crie uma branch: `git checkout -b minha-feature`
3. Faça commits: `git commit -m "Adiciona feature X"`
4. Push: `git push origin minha-feature`
5. Abra um Pull Request

---

## 🆘 Suporte

### 41. Onde conseguir ajuda?
- **Documentação Django:** https://docs.djangoproject.com/
- **Stack Overflow:** https://stackoverflow.com/questions/tagged/django
- **Django Forum:** https://forum.djangoproject.com/
- **Reddit:** r/django

### 42. Como reportar bugs?
1. Verifique se já não foi reportado
2. Crie uma issue com:
   - Descrição do problema
   - Passos para reproduzir
   - Comportamento esperado vs atual
   - Versão do Python e Django
   - Sistema operacional

---

## 💡 Dicas

### 43. Atalhos úteis do Django
```powershell
# Shell interativo
python manage.py shell

# Shell com IPython (melhor)
pip install ipython
python manage.py shell

# Ver SQL de uma migração
python manage.py sqlmigrate biblioteca 0001

# Verificar problemas
python manage.py check

# Limpar sessões expiradas
python manage.py clearsessions
```

### 44. Como melhorar performance?
1. Use `select_related()` e `prefetch_related()`
2. Adicione índices nos models
3. Use cache (Redis/Memcached)
4. Otimize queries (django-debug-toolbar)
5. Use CDN para static files

### 45. Boas práticas Django
1. Use ModelForm quando possível
2. Separe lógica de negócio em managers/services
3. Use templates inheritance (DRY)
4. Escreva testes
5. Use migrações sempre
6. Nunca faça `objects.all()` sem filtros em produção
7. Use ambiente virtual
8. Mantenha `requirements.txt` atualizado

---

## 🎓 Aprendizado

### 46. Como aprender mais Django?
1. Leia a [documentação oficial](https://docs.djangoproject.com/)
2. Faça o [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)
3. Leia "Two Scoops of Django"
4. Pratique criando projetos
5. Contribua para projetos open source

### 47. Próximos passos após este projeto?
1. Adicione autenticação
2. Crie uma API REST
3. Implemente testes automatizados
4. Faça deploy em produção
5. Adicione recursos avançados (veja [EXTENSOES.md](EXTENSOES.md))

---

## ❓ Não encontrou sua dúvida?

Se sua pergunta não está aqui:
1. Verifique a [documentação completa](INDICE.md)
2. Consulte a [documentação do Django](https://docs.djangoproject.com/)
3. Procure no [Stack Overflow](https://stackoverflow.com/questions/tagged/django)

---

**Última atualização:** Outubro 2025  
**Prática 05 - Django ModelForm e CRUD**
