# 🚀 Extensões e Melhorias - Prática 05

Este documento lista possíveis extensões e melhorias que podem ser implementadas no projeto.

## 🎯 Melhorias Sugeridas

### 1. Autenticação e Autorização
```python
# settings.py
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

# urls.py
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

# views.py
from django.contrib.auth.decorators import login_required

@login_required
def livro_create(request):
    # ... código existente
```

**Benefício:** Proteger rotas e controlar acesso.

---

### 2. Paginação nas Listagens
```python
# views.py
from django.core.paginator import Paginator

def livro_list(request):
    livros = Livro.objects.select_related('editora').all()
    paginator = Paginator(livros, 10)  # 10 por página
    page = request.GET.get('page')
    livros_pagina = paginator.get_page(page)
    return render(request, 'biblioteca/livro_list.html', {'livros': livros_pagina})
```

**Benefício:** Melhor performance com muitos registros.

---

### 3. Busca e Filtros
```python
# views.py
def livro_list(request):
    livros = Livro.objects.select_related('editora').all()
    
    # Busca por título
    busca = request.GET.get('busca')
    if busca:
        livros = livros.filter(titulo__icontains=busca)
    
    # Filtro por editora
    editora_id = request.GET.get('editora')
    if editora_id:
        livros = livros.filter(editora_id=editora_id)
    
    # Filtro por preço
    preco_max = request.GET.get('preco_max')
    if preco_max:
        livros = livros.filter(preco__lte=preco_max)
    
    return render(request, 'biblioteca/livro_list.html', {'livros': livros})
```

**Template:**
```html
<form method="get">
    <input type="text" name="busca" placeholder="Buscar livro...">
    <select name="editora">
        <option value="">Todas as editoras</option>
        {% for editora in editoras %}
            <option value="{{ editora.id }}">{{ editora.nome }}</option>
        {% endfor %}
    </select>
    <input type="number" name="preco_max" placeholder="Preço máximo">
    <button type="submit">Buscar</button>
</form>
```

**Benefício:** Facilita encontrar registros específicos.

---

### 4. API REST com Django REST Framework
```bash
pip install djangorestframework
```

```python
# settings.py
INSTALLED_APPS = [
    # ...
    'rest_framework',
]

# serializers.py
from rest_framework import serializers
from .models import Autor, Livro

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

# views.py
from rest_framework import viewsets
from .serializers import AutorSerializer, LivroSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

# urls.py
from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, LivroViewSet

router = DefaultRouter()
router.register(r'autores', AutorViewSet)
router.register(r'livros', LivroViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

**Benefício:** Criar API para consumo externo (mobile, frontend separado).

---

### 5. Upload de Imagens para Livros
```python
# models.py
class Livro(models.Model):
    # ... campos existentes ...
    capa = models.ImageField(upload_to='capas/', blank=True, null=True)

# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# urls.py (config)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... urls existentes ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# forms.py
class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'publicacao', 'preco', 'estoque', 'editora', 'capa']

# template
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Salvar</button>
</form>
```

**Benefício:** Visualização mais rica dos livros.

---

### 6. Exportar para CSV/Excel
```python
# views.py
import csv
from django.http import HttpResponse

def exportar_livros_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="livros.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['ID', 'Título', 'Editora', 'Preço', 'Estoque'])
    
    livros = Livro.objects.all()
    for livro in livros:
        writer.writerow([
            livro.id,
            livro.titulo,
            livro.editora.nome,
            livro.preco,
            livro.estoque
        ])
    
    return response

# urls.py
path('livros/exportar/', views.exportar_livros_csv, name='exportar_livros_csv'),
```

**Benefício:** Análise de dados em planilhas.

---

### 7. Gráficos e Dashboard com Chart.js
```html
<!-- home.html -->
<canvas id="graficoLivros"></canvas>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
const ctx = document.getElementById('graficoLivros');
new Chart(ctx, {
    type: 'bar',
    data: {
        labels: [
            {% for editora in editoras %}
                '{{ editora.nome }}',
            {% endfor %}
        ],
        datasets: [{
            label: 'Quantidade de Livros',
            data: [
                {% for editora in editoras %}
                    {{ editora.livros.count }},
                {% endfor %}
            ],
            backgroundColor: 'rgba(54, 162, 235, 0.5)'
        }]
    }
});
</script>
```

**Benefício:** Visualização de dados de forma gráfica.

---

### 8. Sistema de Empréstimos
```python
# models.py
from django.contrib.auth.models import User

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(auto_now_add=True)
    data_devolucao = models.DateField()
    devolvido = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'
    
    def __str__(self):
        return f"{self.livro.titulo} - {self.usuario.username}"
    
    def esta_atrasado(self):
        from datetime import date
        return not self.devolvido and date.today() > self.data_devolucao
```

**Benefício:** Gerenciar empréstimos de livros.

---

### 9. Avaliações e Comentários
```python
# models.py
class Avaliacao(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='avaliacoes')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comentario = models.TextField(blank=True)
    data = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        unique_together = ['livro', 'usuario']
    
    def __str__(self):
        return f"{self.livro.titulo} - {self.nota} estrelas"
```

**Benefício:** Feedback dos usuários sobre os livros.

---

### 10. Notificações por Email
```python
# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seu_email@gmail.com'
EMAIL_HOST_PASSWORD = 'sua_senha'

# views.py
from django.core.mail import send_mail

def livro_create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            livro = form.save()
            
            # Enviar notificação
            send_mail(
                'Novo Livro Cadastrado',
                f'O livro "{livro.titulo}" foi cadastrado com sucesso!',
                'biblioteca@example.com',
                ['admin@example.com'],
            )
            
            messages.success(request, 'Livro criado com sucesso!')
            return redirect('livro_list')
    # ... resto do código
```

**Benefício:** Notificações automáticas de eventos.

---

### 11. Cache para Performance
```python
# settings.py
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}

# views.py
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)  # Cache por 15 minutos
def livro_list(request):
    livros = Livro.objects.select_related('editora').all()
    return render(request, 'biblioteca/livro_list.html', {'livros': livros})
```

**Benefício:** Melhor performance em listas grandes.

---

### 12. Testes Automatizados Completos
```python
# tests.py
from django.test import TestCase, Client
from django.urls import reverse
from .models import Autor

class AutorViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.autor = Autor.objects.create(nome="Test Author")
    
    def test_autor_list_view(self):
        response = self.client.get(reverse('autor_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Author")
    
    def test_autor_create_view(self):
        response = self.client.post(reverse('autor_create'), {
            'nome': 'New Author'
        })
        self.assertEqual(response.status_code, 302)  # redirect
        self.assertEqual(Autor.objects.count(), 2)
    
    def test_autor_update_view(self):
        response = self.client.post(
            reverse('autor_update', args=[self.autor.pk]),
            {'nome': 'Updated Author'}
        )
        self.autor.refresh_from_db()
        self.assertEqual(self.autor.nome, 'Updated Author')
    
    def test_autor_delete_view(self):
        response = self.client.post(
            reverse('autor_delete', args=[self.autor.pk])
        )
        self.assertEqual(Autor.objects.count(), 0)
```

**Benefício:** Garantir qualidade do código.

---

### 13. Class-Based Views (CBV)
```python
# views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class AutorListView(ListView):
    model = Autor
    template_name = 'biblioteca/autor_list.html'
    context_object_name = 'autores'

class AutorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'biblioteca/autor_form.html'
    success_url = reverse_lazy('autor_list')

class AutorUpdateView(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'biblioteca/autor_form.html'
    success_url = reverse_lazy('autor_list')

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'biblioteca/autor_confirm_delete.html'
    success_url = reverse_lazy('autor_list')

# urls.py
path('autores/', AutorListView.as_view(), name='autor_list'),
path('autores/criar/', AutorCreateView.as_view(), name='autor_create'),
```

**Benefício:** Menos código, mais reutilizável.

---

### 14. Integração com PostgreSQL
```python
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'biblioteca_db',
        'USER': 'postgres',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

```bash
pip install psycopg2-binary
python manage.py migrate
```

**Benefício:** Melhor performance e recursos avançados.

---

### 15. Docker e Docker Compose
```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

```yaml
# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/app
    ports:
      - "8000:8000"
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://postgres:postgres@db:5432/biblioteca

  db:
    image: postgres:15
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=biblioteca
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres

volumes:
  postgres_data:
```

**Benefício:** Ambiente isolado e reproduzível.

---

## 🎓 Recursos de Aprendizado

### Documentação Oficial
- [Django Docs](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Bootstrap 5](https://getbootstrap.com/docs/5.0/)

### Tutoriais
- [Django for Beginners](https://djangoforbeginners.com/)
- [Two Scoops of Django](https://www.feldroy.com/books/two-scoops-of-django-3-x)
- [Real Python Django Tutorials](https://realpython.com/tutorials/django/)

### Vídeos
- [Corey Schafer - Django Tutorial](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
- [Traversy Media - Django Crash Course](https://www.youtube.com/watch?v=e1IyzVyrLSU)

---

## 📝 Checklist de Extensões

- [ ] Implementar autenticação de usuários
- [ ] Adicionar paginação nas listas
- [ ] Criar sistema de busca e filtros
- [ ] Desenvolver API REST
- [ ] Adicionar upload de imagens
- [ ] Implementar exportação CSV/Excel
- [ ] Criar dashboard com gráficos
- [ ] Adicionar sistema de empréstimos
- [ ] Implementar avaliações e comentários
- [ ] Configurar notificações por email
- [ ] Adicionar cache Redis
- [ ] Escrever testes automatizados completos
- [ ] Migrar para Class-Based Views
- [ ] Trocar SQLite por PostgreSQL
- [ ] Dockerizar aplicação
- [ ] Configurar CI/CD
- [ ] Deploy em produção (Heroku/DigitalOcean/AWS)

---

**Este documento serve como roadmap para evolução do projeto.**
