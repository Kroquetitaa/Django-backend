# Django-backend

1. Lo primero que haremos sera un pip install virtualenv
2. Lo segundo crear nuestro virtualenv -> virtualenv "Nombre"
3. Ejecutar el activate dentro del bin o script -> source "Nombre carpeta"/bin/activate
4. Instalar Django -> pip install django
5. Veamos la lista de los paquetes instalados con -> pip list
6. Crear un nuevo proyecto en Django -> django-admin startproject backend
7. Vamos a instalar `boto3` -> que es una biblioteca de python que proporciona una interfaz para trabajar con los servicios de amazon web service(AWS). Como pueden  ser Amazon S3(almacenamiento en la nube), Amazon EC2(computacion en la nube), Amazon DynamoDB(base de datos NoSQL), Amazon SQS(cola de mensajes)
8. Vamos a instalar `django-cors-headers`-> que es una biblioteca de Django que proporciona un middleware para manejar solicitudes de recursos cruzados (CORS).
9. Vamos a instalar `django-dotenv` -> que es una biblioteca que permite cargar variables de entorno desde archivos .env en proyectos Django.
10. Vamos a instalar `django-filter` -> que es una biblioteca que proporciona una forma sencilla de filtrar objetos de modelos en aplicaciones Django. Esta biblioteca es especialmente útil cuando necesitas implementar funcionalidades de búsqueda avanzada o filtrado complejo en tus vistas de Django.
11. Vamos a instalar `django-storages` -> que es una biblioteca que proporciona integraciones con varios servicios de almacenamiento en la nube para proyectos Django. Está diseñada para facilitar el almacenamiento de archivos de medios estáticos y cargados por el usuario en servicios en la nube, como Amazon S3, Google Cloud Storage, Microsoft Azure Storage, entre otros.
12. Vamos a instalar `djangorestframework` -> que es un marco de desarrollo para crear API RESTful en aplicaciones web Django. Proporciona una amplia gama de herramientas y bibliotecas para simplificar y agilizar el desarrollo de API basadas en REST en Django
13. Vamos a instalar `djangorestframework-simplejwt` -> que es una extensión de Django REST Framework que proporciona un conjunto de herramientas para implementar la autenticación basada en tokens JSON Web Tokens (JWT) en aplicaciones web Django.
14. Vamos a instalar `geocoder` -> que es una biblioteca que proporciona una interfaz sencilla para interactuar con varios servicios de geocodificación y reverse geocodificación desde Python
15. Vamos a instalar `gunicorn` -> que es un servidor web HTTP de código abierto para aplicaciones Python WSGI (Web Server Gateway Interface). Es ampliamente utilizado para desplegar aplicaciones web Python en producción debido a su facilidad de uso, rendimiento y escalabilidad
16. Vamos a instalar `whitenoise` -> que es una biblioteca de Python utilizada en aplicaciones web Django para servir archivos estáticos de forma eficiente y segura. Cuando despliegas una aplicación Django en producción, normalmente necesitas servir archivos estáticos como CSS, JavaScript e imágenes de una manera rápida y eficiente. WhiteNoise proporciona un middleware que se integra fácilmente en tu aplicación Django y se encarga de servir estos archivos estáticos de manera eficiente, sin necesidad de configurar un servidor web adicional como Nginx o Apache para este propósito.
17. Vamos a instalar `psycopg2` -> que es un adaptador de base de datos PostgreSQL para Python. Es una biblioteca de código abierto que permite a los desarrolladores de Python interactuar con bases de datos PostgreSQL desde sus aplicaciones Python de manera eficiente y fácil.
18. Vamos a instalar `dj-database-url` -> que es una biblioteca de Python que simplifica la configuración de la base de datos en aplicaciones Django al permitir la carga de la configuración de la base de datos desde una URL. Esta biblioteca es útil especialmente en entornos donde la configuración de la base de datos puede variar dependiendo del entorno de despliegue (desarrollo, prueba, producción, etc.).
19. Vamos a instalar `psycopg2-binary` -> que es una distribución binaria de la biblioteca psycopg2, que es un adaptador de base de datos PostgreSQL para el lenguaje de programación Python. Esta distribución binaria se utiliza para facilitar la instalación de psycopg2 sin necesidad de compilar el código fuente.
20.  Vamos a instalar `python-dotenv` -> que se utiliza para cargar variables de entorno desde un archivo .env

EXPORTAR siempre estas dos librerias antes de ejecutar servidor porque siempre da fallos:
export GDAL_LIBRARY_PATH=/opt/homebrew/lib/libgdal.dylib
export GEOS_LIBRARY_PATH=/opt/homebrew/lib/libgeos_c.dylib

Lo siguiente que tenemos que hacer es configurar nuestro archivo settings.py ir a DATABASES = {} y añadir nuestra bbdd en mi caso POSTGRESQL

Un ejemplo seria: 
```python
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",
        "NAME": "jobbee-api",
        "USER": "postgres",
        "PASSWORD": "admin",
        "HOST": "localhost",
        "PORT": 5433
    }
}

```

Por último ejecutamos nuestro servidor -> python manage.py runserver

Creamos un .env para guardar todas las variables y una vez terminado toda la configuracion de settings lo primero que haremos sera un migrate. Para aplicar las migraciones pendientes a la base de datos -> python manage.py migrate

Por último crearemos un superuser para nuestra ruta de /admin -> python manage.py createsuperuser
Por ultimo lo que haremos será crear nuestra aplicacion con el comando `python manage.py startapp job` -> que es un comando utilizado en Django para crear una nueva aplicación dentro de un proyecto Django. Al ejecutar este comando, se creará una nueva carpeta dentro del directorio del proyecto Django, la cual contendrá toda la estructura inicial de una aplicación de Django.

- [Estos comandos se usan solo cuando hacemos cambios en nuestros models que afecten a nuestra base de datos]
- Despues de crear en nuestro models la class Job ejecutaremos el comando `python manage.py makemigrations`
- Acto seguido hacemos el migrate con el comando `python manage.py migrate`