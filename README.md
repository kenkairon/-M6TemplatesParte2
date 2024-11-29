# -M6TemplatesParte2
Educativo y de Aprendizaje Personal

---

## Tabla de Contenidos
- [Requisitos](#requisitos)
- [Configuración del Entorno](#configuración-del-entorno)
- [Activación del Entorno](#Activación-del-Entorno)
- [Configuración Inicial](#configuración-inicial)
- [Pasos del Proyecto](#pasos-del-proyecto)
  - [Configuración del Proyecto](#configuración-del-proyecto)
  - [Creación de Vistas y Modelos](#creación-de-vistas-y-modelos)
 

---

## Requisitos

- Python 3.9 o superior
- Django 4.0 o superior
- Bootstrap 4

---

## Configuración del Entorno

1. Crear el entorno virtual:
   ```bash
   python -m venv venv


## Activación del Entorno

2. Activar el entorno virtual:
    ### Windows
    ```bash
    venv\Scripts\activate

## Configuración Inicial
## Instalar Django y Guardar dependencias

3. Intalación Django
    ```bash
    pip install django

4. Instalamos la actualizacion de pip
    ```bash
    python.exe -m pip install --upgrade pip


## Guardar las dependencias
5. Instalación dependencias
    ```bash
   pip freeze > requirements.txt

## Pasos del Proyecto
6. Crear el Proyecto
    ```bash
    django-admin startproject proyecto_educativo

7. Ingresar al directorio del Proyecto
    ```bash
    cd proyecto_educativo

8. Creamos la Aplicación principal
    ```bash
    python manage.py startapp principal

## Configuración del Proyecto

10. Conectar el proyecto con la aplicación: Agregar 'principal' en la lista INSTALLED_APPS dentro del archivo proyecto_educativo/settings.py

    ```bash
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'principal',
    ]

11. Migramos la base de datos por defecto que tiene django
    ```bash
    python manage.py migrate

12. Creamos el super usuario
    ```bash
    python manage.py createsuperuser

13. Vamos a ir al principal/models.py
    ```bash
    from django.db import models

    # Create your models here.
    class Estudiantes(models.Model):
        nombre = models.CharField(max_length=50)
        apellido = models.CharField(max_length=50)
        edad = models.IntegerField()
        correo = models.EmailField(unique=True)
        fecha_registro = models.DateField(auto_now=True)
        
    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.edad}'

14. Se hacen las migraciones correspondientes
    ```bash
    python manage.py migrate
    python manage.py makemigrations

15. En la carpeta principal proyecto_eductativo creamos templates/base.html
    ```bash
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>

    <body>
        {% block content%}
        {% endblock %}
    </body>

    </html>
1



