# Script de Inicialização - Prática 05
# Execute este script após liberar espaço em disco e instalar o Django

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "Prática 05 - Django ModelForm e CRUD" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""

# Verifica se o venv existe
if (Test-Path "venv") {
    Write-Host "[OK] Ambiente virtual encontrado" -ForegroundColor Green
    
    # Ativa o ambiente virtual
    Write-Host "[INFO] Ativando ambiente virtual..." -ForegroundColor Yellow
    .\venv\Scripts\Activate.ps1
    
    # Verifica se Django está instalado
    $djangoInstalled = python -c "import django; print('OK')" 2>$null
    if ($djangoInstalled -eq "OK") {
        Write-Host "[OK] Django já está instalado" -ForegroundColor Green
    } else {
        Write-Host "[INFO] Instalando Django..." -ForegroundColor Yellow
        pip install -r requirements.txt
    }
    
    Write-Host ""
    Write-Host "[INFO] Aplicando migrações..." -ForegroundColor Yellow
    python manage.py makemigrations
    python manage.py migrate
    
    Write-Host ""
    Write-Host "[INFO] Coletando arquivos estáticos..." -ForegroundColor Yellow
    python manage.py collectstatic --noinput 2>$null
    
    Write-Host ""
    Write-Host "==================================================" -ForegroundColor Cyan
    Write-Host "Configuração concluída!" -ForegroundColor Green
    Write-Host "==================================================" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Para criar um superusuário (admin):" -ForegroundColor Yellow
    Write-Host "  python manage.py createsuperuser" -ForegroundColor White
    Write-Host ""
    Write-Host "Para iniciar o servidor:" -ForegroundColor Yellow
    Write-Host "  python manage.py runserver" -ForegroundColor White
    Write-Host ""
    Write-Host "Depois acesse:" -ForegroundColor Yellow
    Write-Host "  http://localhost:8000/         - Home" -ForegroundColor White
    Write-Host "  http://localhost:8000/admin/   - Django Admin" -ForegroundColor White
    Write-Host ""
    
} else {
    Write-Host "[ERRO] Ambiente virtual não encontrado" -ForegroundColor Red
    Write-Host ""
    Write-Host "Execute os seguintes comandos:" -ForegroundColor Yellow
    Write-Host "  1. python -m venv venv" -ForegroundColor White
    Write-Host "  2. .\venv\Scripts\Activate.ps1" -ForegroundColor White
    Write-Host "  3. pip install -r requirements.txt" -ForegroundColor White
    Write-Host "  4. python manage.py migrate" -ForegroundColor White
    Write-Host "  5. python manage.py runserver" -ForegroundColor White
    Write-Host ""
}
