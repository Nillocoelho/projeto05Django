# 🧪 Testes e Exemplos - Prática 05

## 🎯 Testes Manuais no Browser

### 1. Teste de Criação de Autor
```
1. Acesse: http://localhost:8000/autores/
2. Clique em "Novo Autor"
3. Preencha: "Machado de Assis"
4. Clique em "Salvar"
5. ✅ Deve aparecer mensagem de sucesso
6. ✅ Deve redirecionar para lista de autores
7. ✅ Deve mostrar o autor criado na tabela
```

### 2. Teste de Criação de Editora
```
1. Acesse: http://localhost:8000/editoras/
2. Clique em "Nova Editora"
3. Preencha: "Companhia das Letras"
4. Clique em "Salvar"
5. ✅ Deve aparecer mensagem de sucesso
```

### 3. Teste de Criação de Livro
```
1. Acesse: http://localhost:8000/livros/
2. Clique em "Novo Livro"
3. Preencha:
   - Título: "Dom Casmurro"
   - Data de Publicação: 01/01/1899
   - Preço: 29.90
   - Estoque: 15
   - Editora: Companhia das Letras
4. Clique em "Salvar"
5. ✅ Deve aparecer mensagem de sucesso
6. ✅ Livro deve aparecer na lista com todos os dados
```

### 4. Teste de Criação de Publicação
```
1. Acesse: http://localhost:8000/publicacoes/
2. Clique em "Nova Publicação"
3. Selecione:
   - Livro: Dom Casmurro
   - Autor: Machado de Assis
4. Clique em "Salvar"
5. ✅ Deve aparecer mensagem de sucesso
6. ✅ Publicação deve aparecer na lista
```

### 5. Teste de Edição
```
1. Acesse qualquer lista (autores, editoras, livros, publicações)
2. Clique em "Editar" em um registro
3. Altere algum campo
4. Clique em "Salvar"
5. ✅ Deve aparecer mensagem de sucesso
6. ✅ Alteração deve aparecer na lista
```

### 6. Teste de Exclusão
```
1. Acesse qualquer lista
2. Clique em "Excluir" em um registro
3. ✅ Deve mostrar página de confirmação
4. Clique em "Sim, Excluir"
5. ✅ Deve aparecer mensagem de sucesso
6. ✅ Registro deve sumir da lista
```

### 7. Teste de Validação
```
1. Tente criar um autor sem nome
2. ✅ Deve mostrar erro "Este campo é obrigatório"

3. Tente criar um livro com preço negativo
4. ✅ Deve mostrar erro de validação

5. Tente criar publicação duplicada (mesmo livro + mesmo autor)
6. ✅ Deve mostrar erro "Já existe"
```

## 🧪 Testes Unitários

### Executar todos os testes
```powershell
python manage.py test
```

### Executar testes específicos
```powershell
# Apenas testes do app biblioteca
python manage.py test biblioteca

# Apenas testes de models
python manage.py test biblioteca.tests.AutorModelTest

# Com verbosidade
python manage.py test --verbosity=2
```

### Resultado esperado
```
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
........
----------------------------------------------------------------------
Ran 4 tests in 0.XXXs

OK
Destroying test database for alias 'default'...
```

## 💻 Testes via Django Shell

### Abrir o shell
```powershell
python manage.py shell
```

### Exemplos de comandos

#### Criar Autor
```python
from biblioteca.models import Autor

# Criar
autor = Autor.objects.create(nome="Clarice Lispector")
print(autor)  # Clarice Lispector
print(autor.id)  # 1

# Listar todos
autores = Autor.objects.all()
print(autores)

# Contar
print(Autor.objects.count())  # 1
```

#### Criar Editora
```python
from biblioteca.models import Editora

editora = Editora.objects.create(nome="Record")
print(editora)  # Record
```

#### Criar Livro
```python
from biblioteca.models import Livro
from datetime import date

livro = Livro.objects.create(
    titulo="A Hora da Estrela",
    publicacao=date(1977, 1, 1),
    preco=28.00,
    estoque=12,
    editora=editora  # objeto criado antes
)
print(livro)  # A Hora da Estrela - Record
print(livro.editora.nome)  # Record
```

#### Criar Publicação
```python
from biblioteca.models import Publica

publica = Publica.objects.create(
    livro=livro,
    autor=autor
)
print(publica)  # A Hora da Estrela - Clarice Lispector
```

#### Consultas Avançadas
```python
# Filtrar livros por editora
livros = Livro.objects.filter(editora__nome="Record")

# Filtrar livros com preço < 30
livros_baratos = Livro.objects.filter(preco__lt=30)

# Buscar livros por título (case-insensitive)
livros = Livro.objects.filter(titulo__icontains="hora")

# Ordenar livros por preço
livros = Livro.objects.order_by('preco')

# Livros com estoque > 0
livros_disponiveis = Livro.objects.filter(estoque__gt=0)

# Todos os livros de um autor
autor = Autor.objects.get(nome="Clarice Lispector")
livros = Livro.objects.filter(publicacoes__autor=autor)

# Todos os autores de um livro
livro = Livro.objects.get(titulo="A Hora da Estrela")
autores = Autor.objects.filter(publicacoes__livro=livro)
```

#### Atualizar
```python
# Método 1: Atualizar objeto
autor = Autor.objects.get(id=1)
autor.nome = "Clarice Lispector Silva"
autor.save()

# Método 2: Update direto
Autor.objects.filter(id=1).update(nome="Clarice Lispector")

# Update em massa
Livro.objects.filter(estoque=0).update(estoque=5)
```

#### Deletar
```python
# Deletar um objeto
autor = Autor.objects.get(id=1)
autor.delete()

# Deletar múltiplos
Livro.objects.filter(estoque=0).delete()

# Deletar todos (CUIDADO!)
Autor.objects.all().delete()
```

## 🔍 Testes de Integração

### Popular banco e validar
```powershell
# Popular com dados de exemplo
python manage.py shell < populate_db.py

# Verificar no shell
python manage.py shell
```

```python
from biblioteca.models import *

# Verificar dados
print(f"Autores: {Autor.objects.count()}")
print(f"Editoras: {Editora.objects.count()}")
print(f"Livros: {Livro.objects.count()}")
print(f"Publicações: {Publica.objects.count()}")

# Listar tudo
for autor in Autor.objects.all():
    print(f"- {autor.nome}")

for livro in Livro.objects.all():
    print(f"- {livro.titulo} | R$ {livro.preco} | {livro.editora.nome}")

for pub in Publica.objects.all():
    print(f"- {pub.livro.titulo} por {pub.autor.nome}")
```

## 🎭 Testes de Scenarios

### Scenario 1: Livraria completa
```python
# 1. Criar editora
editora = Editora.objects.create(nome="Saraiva")

# 2. Criar autores
machado = Autor.objects.create(nome="Machado de Assis")
jose = Autor.objects.create(nome="José de Alencar")

# 3. Criar livros
livro1 = Livro.objects.create(
    titulo="Dom Casmurro",
    publicacao=date(1899, 1, 1),
    preco=29.90,
    estoque=15,
    editora=editora
)

livro2 = Livro.objects.create(
    titulo="Senhora",
    publicacao=date(1875, 1, 1),
    preco=25.00,
    estoque=8,
    editora=editora
)

# 4. Criar publicações
Publica.objects.create(livro=livro1, autor=machado)
Publica.objects.create(livro=livro2, autor=jose)

# 5. Validar
print(f"Editora {editora.nome} tem {editora.livros.count()} livros")
print(f"Autor {machado.nome} tem {machado.publicacoes.count()} publicações")
```

### Scenario 2: Livro com múltiplos autores
```python
# Criar editora e livro
editora = Editora.objects.create(nome="Companhia das Letras")
livro = Livro.objects.create(
    titulo="Antologia Brasileira",
    publicacao=date(2020, 1, 1),
    preco=45.00,
    estoque=20,
    editora=editora
)

# Criar autores
autor1 = Autor.objects.create(nome="Carlos Drummond")
autor2 = Autor.objects.create(nome="Cecília Meireles")
autor3 = Autor.objects.create(nome="Vinícius de Moraes")

# Associar múltiplos autores ao livro
Publica.objects.create(livro=livro, autor=autor1)
Publica.objects.create(livro=livro, autor=autor2)
Publica.objects.create(livro=livro, autor=autor3)

# Listar autores do livro
print(f"Livro: {livro.titulo}")
for pub in livro.publicacoes.all():
    print(f"  - Autor: {pub.autor.nome}")
```

### Scenario 3: Consultas complexas
```python
# Livros mais caros que R$ 30
caros = Livro.objects.filter(preco__gt=30)
print(f"Livros caros: {caros.count()}")

# Livros sem estoque
sem_estoque = Livro.objects.filter(estoque=0)
print(f"Livros sem estoque: {sem_estoque.count()}")

# Livros publicados após 1900
recentes = Livro.objects.filter(publicacao__year__gte=1900)
print(f"Livros recentes: {recentes.count()}")

# Autores com mais de 2 publicações
from django.db.models import Count
prolific = Autor.objects.annotate(
    num_pubs=Count('publicacoes')
).filter(num_pubs__gt=2)
for autor in prolific:
    print(f"{autor.nome}: {autor.num_pubs} publicações")

# Editoras com mais livros
top_editoras = Editora.objects.annotate(
    num_livros=Count('livros')
).order_by('-num_livros')
for ed in top_editoras:
    print(f"{ed.nome}: {ed.num_livros} livros")
```

## 🐛 Testes de Erro

### Teste de validação de campo obrigatório
```python
from biblioteca.forms import AutorForm

# Form vazio
form = AutorForm({})
print(form.is_valid())  # False
print(form.errors)  # {'nome': ['Este campo é obrigatório.']}
```

### Teste de constraint unique_together
```python
from biblioteca.models import Publica, Livro, Autor

livro = Livro.objects.first()
autor = Autor.objects.first()

# Criar primeira publicação
Publica.objects.create(livro=livro, autor=autor)

# Tentar criar duplicata
try:
    Publica.objects.create(livro=livro, autor=autor)
except Exception as e:
    print(f"Erro esperado: {e}")  # IntegrityError
```

## 📊 Relatórios e Estatísticas

### Gerar relatório no shell
```python
from biblioteca.models import *
from django.db.models import Count, Sum, Avg

# Estatísticas gerais
print("="*50)
print("RELATÓRIO DA BIBLIOTECA")
print("="*50)
print(f"\nTotal de Autores: {Autor.objects.count()}")
print(f"Total de Editoras: {Editora.objects.count()}")
print(f"Total de Livros: {Livro.objects.count()}")
print(f"Total de Publicações: {Publica.objects.count()}")

# Estoque total
estoque_total = Livro.objects.aggregate(Sum('estoque'))['estoque__sum']
print(f"\nEstoque Total: {estoque_total} livros")

# Preço médio
preco_medio = Livro.objects.aggregate(Avg('preco'))['preco__avg']
print(f"Preço Médio: R$ {preco_medio:.2f}")

# Livro mais caro
mais_caro = Livro.objects.order_by('-preco').first()
print(f"\nLivro mais caro: {mais_caro.titulo} (R$ {mais_caro.preco})")

# Livro mais barato
mais_barato = Livro.objects.order_by('preco').first()
print(f"Livro mais barato: {mais_barato.titulo} (R$ {mais_barato.preco})")

# Top 5 editoras
print("\nTop 5 Editoras:")
top_editoras = Editora.objects.annotate(
    num_livros=Count('livros')
).order_by('-num_livros')[:5]
for i, ed in enumerate(top_editoras, 1):
    print(f"{i}. {ed.nome}: {ed.num_livros} livros")

# Top 5 autores
print("\nTop 5 Autores:")
top_autores = Autor.objects.annotate(
    num_pubs=Count('publicacoes')
).order_by('-num_pubs')[:5]
for i, autor in enumerate(top_autores, 1):
    print(f"{i}. {autor.nome}: {autor.num_pubs} publicações")
```

## ✅ Checklist de Testes

### Funcionalidades Básicas
- [ ] Criar autor
- [ ] Editar autor
- [ ] Excluir autor
- [ ] Listar autores
- [ ] Criar editora
- [ ] Editar editora
- [ ] Excluir editora
- [ ] Listar editoras
- [ ] Criar livro
- [ ] Editar livro
- [ ] Excluir livro
- [ ] Listar livros
- [ ] Criar publicação
- [ ] Editar publicação
- [ ] Excluir publicação
- [ ] Listar publicações

### Validações
- [ ] Campo nome vazio em Autor
- [ ] Campo nome vazio em Editora
- [ ] Campo título vazio em Livro
- [ ] Preço negativo em Livro
- [ ] Estoque negativo em Livro
- [ ] Data inválida em Livro
- [ ] Publicação duplicada (unique_together)

### Interface
- [ ] Navegação entre páginas
- [ ] Mensagens de sucesso/erro
- [ ] Confirmação de exclusão
- [ ] Responsividade (mobile)
- [ ] Botões e links funcionando

### Admin
- [ ] Login no admin
- [ ] CRUD de Autor no admin
- [ ] CRUD de Editora no admin
- [ ] CRUD de Livro no admin
- [ ] CRUD de Publicação no admin
- [ ] Filtros funcionando
- [ ] Busca funcionando

---

**Guia de testes para Prática 05 - Django ModelForm e CRUD**
