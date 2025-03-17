# PUNTO A
## Django- BASIC  
## Acerca del proyecto
En este repositorio encontrarás un paso a paso básico de cómo crear una aplicación,  usando Python Django para la gestión de tareas pendientes. Se explica los pasos para configurar un entorno virtual, instalar dependencias y manejo de usuarios, correos, etc.
## Instalación y configuración
## 1. Crear un entorno virtual
Es recomendable utilizar un entorno virtual de Python para aislar las dependencias del proyecto y evitar conflictos con otras aplicaciones.

Ejecuta el siguiente comando para crearlo:
```
python -m venv env
```

Nota: Puedes cambiar el nombre "env" por el que desees.

Para activar el entorno: 
- Windows:
```
./venv/Scripts/activate
```
- Mac/Linux
```

source env/bin/activate
```

NOTA: Es importante asegurarnos que nuestro editor sea el intérprete correcto para que las dependencias que hemos instalado sean reconocidas e implementadas en el proyecto.

En VS Code:
- Abrir Command Palette presionando `Ctrl + Shift + P`
- Escribir "Python: Select Interpreter" y presionar `Enter`
- Buscar el intérprete correspondiente al entorno creado. Suele estar marcado con la palabra `Recommended` y seleccionar
  
## 2. Instalar Django y dependencias
Con el entorno virtual activado, instala Django y otras librerías necesarias:
```
pip install django
```

Para verificar la instalación: 
```
django-admin --version
```
## 3. Crear un archivo de requerimientos
El archivo requirements es una lista donde se guardan todas las dependencias de tu proyecto, pricipalmente para facilitar la instalacion de las versiones de estas. Siguiendo esto, para registrar las dependencias del proyecto, genera el archivo `requirements.txt`:
```
pip freeze > requirements.txt
```
Si deseas instalar dependencia en otro entorno: 
```
pip install -r requirements.txt
```
## 4. Crear proyecto
Para crear: 
```
django-admin startproject mytodo .
```
Para ejecutar: 
```
python manage.py runserver
```

Nota: Recuerda acceder a la URL que muestra la consola para visualizar el proyecto.
Al crear el proyecto, podemos ingresar a settings.py en la carpeta del proyecto para saber que base de datos usaremos. En este caso, buscaremos usar SQLite, por lo que deberiamos encontrarnos con algo así:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
```

## 5. Estructura del proyecto

Al crear el proyecto, se han de tener en cuenta algunos archivos esenciales, como por ejemplo:

```
mytodo/
│-- manage.py  # Herramienta para ejecutar comandos de Django
│-- mytodo/
│   │-- settings.py  # Configuración del proyecto
│   │-- urls.py  # Definición de rutas de la aplicación
│   │-- wsgi.py  # Configuración para servidores web
│   │-- asgi.py  # Configuración para servidores asíncronos
```
## Creación de la aplicación de tareas 
Hasta el momento, lo unico que hemos realizado es la configuracion del entorno y la creación de un proyecto, empezaremos a crear funcionalidades. 

1. Iniciaremos creando una aplicación llamada `tasks` ejecutando: 
```
python manage.py startapp tasks
```
Donde encontrarás archivos como:
```
tasks/
│-- models.py  # Define la estructura de datos
│-- views.py  # Contiene la lógica de las vistas
│-- admin.py  # Configuración del panel de administración
│-- urls.py  # Definición de rutas de la aplicación (crear manualmente)
```
2. Una vez creada la aplicación, es necesario que la registremos en la configuracion del proyecto para que Django la reconozca.
   - Ir a `settings.py`
   - Buscar la lista llamada `INSTALLED_APPS`
   - Y agregamos un elemento, en este caso `tasks`
3. Incluir URLs en el proyecto
   Es necesario que Django reconozca las rutas que el proyecto esta usando, por lo que las incluiremos en el archivo URLs principal.
Para hacer esto, debemos:
- Ir a archivo [URLs principal ](https://github.com/yuluka/django-todo-tutorial/blob/main/todo_app/urls.py)
- Importamos la función `include`:
```
from django.urls import path, include
```
 Agregamos a la lista `urlpatterns` con una funcion `include()`:
 ```
path('', include(tasks.urls)),
```
4. Vista inicial
   Debemos crear una función encargada de mostrarnos en una pagina el inicio de nuestra aplicación.
   Para ello iremos a `views.py` y haremos la siguiente función:
   ```
   def home(request):
    return render(request, 'home.html')
   ```
   
5. Crear la Página de Inicio

Ya has implementado una función que muestra la página principal. Ahora, es necesario diseñar esta página creando una plantilla HTML.

Para ello, debes seguir estos pasos:

Dentro de la carpeta de tu aplicación `(tasks/)`, crea una nueva carpeta llamada `templates/`.
Dentro de `templates/`, crea un archivo denominado `base.html`.
Agrega el siguiente código en el archivo `base.html`:
```
<!DOCTYPE html>
<html lang="en">
    <head>
        {% load static %}

        <meta charset="UTF-8"/>
        <meta http-equiv="X-UA-Compatible" content="IE-edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />

        <title>TO DO APP</title>

        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"/>

        <!-- <script src="{% static 'fontawesomefree/js/all.min.js' %}"></script> -->
        <!-- jQuery, Popper.js, y Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>

        <style>
            .sidebar {
                height: 100vh;
                width: 250px;
                position: fixed;
                top: 0;
                left: 0;
                background: #343a40;
                padding-top: 20px;
            }
            .sidebar a {
                color: white;
                display: block;
                padding: 10px;
                text-decoration: none;
            }
            .sidebar a:hover {
                background: #495057;
            }
            .content {
                margin-left: 260px;
                padding: 20px;
            }
        </style>
    </head>

    <body>
        <div class="sidebar">
            <h4 class="text-white text-center">To-Do App</h4>
            <a href="{% url 'list-tasks' %}">Ver Tareas</a>
            <a href="{% url 'create-task' %}">Crear Tarea</a>
        </div>
    
        <div class="content">
            {% block content %}
            {% endblock %}
        </div>
    </body>
</html>
```
- Dentro de la carpeta `templates/`, crea un archivo llamado `home.html`.

- Luego, agrega el siguiente código dentro de `home.html`:

```
{% extends "base.html" %}

{% block content %}


<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TO DO APP</title>
    
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f4f4f4;
        }
        h1 {
            color: #333;
        }
    </style>
</head>
<body>
    <div class="d-flex justify-content-center">
        <h1>Aplicación To-Do</h1>
    </div>
</body>
</html>

{% endblock content %}
```
## 6. Configurar la URL para la Página Principal

Ahora que ya tienes la vista y la plantilla de la página principal, es necesario definir una URL que permita acceder a ella desde el navegador.

Para hacerlo:

Abre el archivo de rutas de la aplicación tasks.
Añade el siguiente código:
```
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```


- A continuación, inicia el servidor como lo hiciste anteriormente y verifica que todo funcione correctamente.
Antes de hacerlo, es necesario actualizar algunas líneas en el archivo base.html que acabas de crear:


```
<a href="{% url 'list-tasks' %}">Ver Tareas</a>
<a href="{% url 'create-task' %}">Crear Tarea</a>
```
- Actualizadas:
```
<a href="">Ver Tareas</a>
<a href="">Crear Tarea</a>
```
## 7. Definir el Modelo para Tareas
Ahora que ya tienes la estructura del proyecto, es momento de desarrollar la lógica de negocio para que la aplicación no solo muestre un mensaje de bienvenida, sino que también permita gestionar tareas: crearlas, editarlas y eliminarlas.

Para ello, sigue estos pasos:

- Abre el archivo `models.py` dentro de la aplicación.
- Define los modelos que representarán las tareas y sus estados en la base de datos.
- Modelo para gestionar el estado de una tarea:
```
class Status(models.Model):
    id = models.AutoField(
        primary_key=True,
        null=False,
        blank=False,
    )

    name = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name
  ```
- Modelo para representar las tareas:
```
class Task(models.Model):
    id = models.AutoField(
        primary_key=True,
        null=False,
        blank=False,
    )

    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=False,
    )
    
    deadline = models.DateTimeField(
        null=True,
        blank=True,
    )

    status_id = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name
```
Para aplicar los cambios realizados en los modelos y sincronizarlos con la base de datos, sigue estos pasos:

- Generar las migraciones ejecutando el siguiente comando en la terminal:
```
python manage.py makemigrations
```
Esto creará un archivo de migración con los cambios en los modelos.

- Aplicar las migraciones con:
```
python manage.py migrate
```
Esto actualizará la base de datos con la estructura definida en los modelos.
Con estos comandos, la base de datos reflejará las modificaciones realizadas en `models.py`.

## 8. Panel de administración y agregar modelos
   
Para registrar los modelos en el panel de administración de Django, sigue estos pasos:

- Abre el archivo admin.py dentro de la aplicación tasks.

- Importa los modelos que creaste en `models.py`:
```
from .models import Status, Task
```
Registra tus modelos:
```
admin.site.register(Status)
admin.site.register(Task)
```
## 9. Panel de administración
Ahora que tus modelos de datos están listos para funcionar, puedes aprovechar el panel de administración predeterminado de Django.

Este panel proporciona una interfaz web automática que facilita la gestión de los datos del proyecto sin necesidad de escribir consultas SQL. A través de él, puedes crear, modificar y eliminar registros en la base de datos, administrar usuarios y sus permisos, y visualizar los modelos de manera organizada.

Para acceder a este panel, es necesario crear un súper-usuario.
```
python manage.py createsuperuser
```
Nota: al ejecutar el codigo, saldrá una consola la cual te pedirá algunos datos.

Después de crear el súper-usuario, puedes acceder al panel de administración. Para hacerlo, inicia el servidor y dirígete a la ruta `/admin` en tu navegador (por ejemplo: `http://localhost:8000/admin/`). Allí encontrarás una página de inicio de sesión donde podrás ingresar con las credenciales creadas.
Explora el panel de administración para familiarizarte con su funcionamiento y crea los diferentes estados en los que podrán estar tus tareas.

## 10. Crear funcionalidades 
- Implementar la funcionalidad de "Creación de Tareas"
Ahora es momento de añadir la funcionalidad que permitirá a los usuarios agregar nuevas tareas a la aplicación.

El proceso sigue la misma estructura que utilizaste para mostrar la pantalla principal:

- Crear una vista que maneje las solicitudes de creación de tareas y genere una respuesta adecuada.
- Diseñar la plantilla HTML que servirá como interfaz para el usuario.
- Registrar la URL que permitirá acceder a esta nueva funcionalidad.
Estos tres pasos se repetirán cada vez que quieras agregar una nueva pantalla o funcionalidad a la aplicación.
## 10.1 Crear vista:
- Ve a `views.py` y define la vista:
```
def create_task(request):
    if request.method == 'POST':
        name: str = request.POST.get('task-name', '')
        description: str = request.POST.get('task-description', '').strip()
        status_id: Status = Status.objects.get(name='Pendiente')

        deadline_str: str = request.POST.get('task-deadline', '').strip()
        deadline: datetime.datetime = None

        if deadline_str:
            try:
                deadline = datetime.datetime.strptime(deadline_str, '%Y-%m-%d')

            except ValueError:
                pass

        Task.objects.create(
            name=name,
            description=description,
            deadline=deadline,
            status_id=status_id,
        )

        messages.success(request, '¡Tarea creada exitosamente!')

        return redirect('list-tasks')

    return render(request, 'create_task.html')
```
En la vista anterior hay varios elementos nuevos que no están importados aún, por lo que se te marcarán como errores. Para solucionarlo, modifica los imports para que queden así:
```
import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from tasks.models import Task, Status
```
## 10.2 Diseñar la pantalla HTML
Para que la vista pueda renderizar contenido, es necesario crear una plantilla HTML.

Dirígete a la carpeta donde se encuentran los templates de la aplicación.
Crea un nuevo archivo llamado `create_task.html`.
Dentro de este archivo, agrega el código necesario para mostrar el formulario de creación de tareas.
```
{% extends "base.html" %}

{% block content %}
<!DOCTYPE html>
<html lang="es">
<head>
    <title>Crear Tarea</title>
</head>
<body class="bg-light">

    <div class="container mt-5">
        <h2 class="mb-4">Crear Nueva Tarea</h2>

        <div class="card shadow-sm">
            <div class="card-body">
                <form method="POST" action="{% url 'create-task' %}">
                    {% csrf_token %}
                    
                    <div class="mb-3">
                        <label for="task-name" class="form-label">Nombre de la Tarea</label>
                        <input type="text" class="form-control" id="task-name" name="task-name" required>
                    </div>

                    <div class="mb-3">
                        <label for="task-description" class="form-label">Descripción</label>
                        <textarea class="form-control" id="task-description" name="task-description" rows="3"></textarea>
                    </div>

                    <div class="mb-3">
                        <label for="task-deadline" class="form-label">Fecha Límite</label>
                        <input type="date" class="form-control" id="task-deadline" name="task-deadline">
                    </div>

                    <button type="submit" class="btn btn-primary">Crear Tarea</button>
                    <a href="{% url 'list-tasks' %}" class="btn btn-secondary">Cancelar</a>
                </form>
            </div>
        </div>
    </div>

</body>
</html>

{% endblock content %}
```
## 10.3 Registrar la URL:
Para permitir el acceso a la pantalla de creación de tareas, es necesario registrar la ruta correspondiente en el archivo de URLs de la aplicación.

Abre el archivo `urls.py` dentro de la aplicación.
Agrega la siguiente ruta:
```
path('create-task/', views.create_task, name='create-task'),
```
## 10.4 Crear funcionalidad "Ver lista de Tareas"
Ahora tienes que crear una pantalla que te permita ver las tareas creadas hasta el momento, con su respectiva información.
Crear vista:
- Ve a views.py y define la vista con la que se renderizará la pantalla de listado de tareas:
```
def list_tasks(request):
    return render(request, 'list_tasks.html', {
        'tasks': Task.objects.all(),
    })
```
## 10.5 Crear la pantalla HTML:

Ve a `templates/` y crea un archivo con el nombre `list_tasks.html`.

Dentro de este archivo, pon el código:
```
{% extends "base.html" %}

{% block content %}
<!DOCTYPE html>
<html lang="es">
<head>
    <title>Lista de Tareas</title>
</head>
<body class="bg-light">

    <div class="container mt-5">
        <h2 class="mb-4">Lista de Tareas</h2>

        {% if messages %}
            <div class="alert-container">
                {% for message in messages %}
                    <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
                        {{ message }}
                        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Cerrar"></button>
                    </div>
                {% endfor %}
            </div>
        {% endif %}

        {% if tasks %}
            <div class="table-responsive">
                <table class="table table-striped table-hover">
                    <thead class="table-dark">
                        <tr>
                            <th>ID</th>
                            <th>Estado</th>
                            <th>Nombre</th>
                            <th>Descripción</th>
                            <th>Fecha Límite</th>
                            <th>Creado</th>
                            <th>Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for task in tasks %}
                        <tr>
                            <td>{{ task.id }}</td>
                            <td>{{ task.status_id.name }}</td>
                            <td>{{ task.name }}</td>
                            <td>{{ task.description }}</td>
                            <td>{{ task.deadline|default:"No definida" }}</td>
                            <td>{{ task.created_at|date:"F j, Y, g:i A" }}</td>
                            <td>
                                <a href="{% url 'edit-task' task.id %}" class="btn btn-warning btn-sm">Editar</a>
                                <button class="btn btn-danger btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" data-task-id="{{ task.id }}">
                                    Eliminar
                                </button>
                            </td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        {% else %}
            <div class="alert alert-info">No hay tareas registradas.</div>
        {% endif %}

        <a href="{% url 'create-task' %}" class="btn btn-primary mt-3">Crear Nueva Tarea</a>
    </div>

    <div class="modal fade" id="deleteModal" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Confirmar eliminación</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <p>¿Estás seguro de que quieres eliminar esta tarea?</p>
                </div>
                <div class="modal-footer">
                    <form id="delete-form" method="POST">
                        {% csrf_token %}
                        <button type="submit" class="btn btn-danger">Eliminar</button>
                    </form>
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                </div>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", function() {
            var deleteModal = document.getElementById("deleteModal");

            deleteModal.addEventListener("show.bs.modal", function(event) {
                var button = event.relatedTarget;  
                var taskId = button.getAttribute("data-task-id");

                var form = document.getElementById("delete-form");
                form.action = `/delete-task/${taskId}/`;
            });
        });
    </script>

</body>
</html>
{% endblock content %}
```


## 10.6 Registrar URL:

Ve al archivo de URLs y agrega la ruta así:

````
path('list-tasks/', views.list_tasks, name='list-tasks'),
````
## 10.7 Crear funcionalidad "Editar tarea"
Ahora debes implementar una forma de editar las tareas que ya hayas creado.
- Crear vista:
- Ve a `views.py` y define la vista con la que se renderizará la pantalla de edición de tareas:
  ```
  def edit_task(request, task_id):
    if request.method == 'POST':
        task: Task = Task.objects.get(id=task_id)

        task.name = request.POST.get('task-name', '')
        task.description = request.POST.get('task-description', '').strip()
        task.status_id = Status.objects.get(id=int(request.POST.get('task-status', 0)))

        deadline_str: str = request.POST.get('task-deadline', '').strip()
        deadline: datetime.datetime = None

        if deadline_str:
            try:
                deadline = datetime.datetime.strptime(deadline_str, '%Y-%m-%d')

            except ValueError:
                pass

        task.deadline = deadline
        task.save()

        messages.success(request, '¡Tarea actualizada exitosamente!')

        return redirect('list-tasks')

    return render(request, 'edit_task.html', {
        'task': Task.objects.get(id=task_id),
        'task_statuses': Status.objects.all(),
    })
    ````
## 10.8 Crear la pantalla HTML:

- Ve a `templates/` y crea un archivo con el nombre `edit_task.html`.

- Dentro de este archivo, pon el código:
````
{% extends "base.html" %}

{% block content %}
<!DOCTYPE html>
<html lang="es">
<head>
    <title>Editar Tarea</title>
</head>
<body class="bg-light">

    <div class="container mt-5">
        <h2 class="mb-4">Editar Tarea</h2>

        <div class="card shadow-sm">
            <div class="card-body">
                <form method="POST" action="{% url 'edit-task' task.id %}">
                    {% csrf_token %}
                    
                    <div class="mb-3">
                        <label for="task-status" class="form-label">Estado</label>
                        <select class="form-select" id="task-status" name="task-status">
                            {% for status in task_statuses %}
                                <option value="{{ status.id }}" {% if status.id == task.status_id.id %}selected{% endif %}>{{ status.name }}</option>
                            {% endfor %}
                        </select>
                    </div>

                    <div class="mb-3">
                        <label for="task-name" class="form-label">Nombre de la Tarea</label>
                        <input type="text" class="form-control" id="task-name" name="task-name" value="{{ task.name }}" required>
                    </div>

                    <div class="mb-3">
                        <label for="task-description" class="form-label">Descripción</label>
                        <textarea class="form-control" id="task-description" name="task-description" rows="3">{{ task.description }}</textarea>
                    </div>

                    <div class="mb-3">
                        <label for="task-deadline" class="form-label">Fecha Límite</label>
                        <input type="date" class="form-control" id="task-deadline" name="task-deadline" value="{{ task.deadline|date:'Y-m-d' }}">
                    </div>

                    <button type="submit" class="btn btn-primary">Guardar cambios</button>
                    <a href="{% url 'list-tasks' %}" class="btn btn-secondary">Cancelar</a>
                </form>
            </div>
        </div>
    </div>

</body>
</html>

{% endblock content %}
````
## 10.9 Registrar URL:

- Ve al archivo de URLs y agrega la ruta así:
````
path('edit-task/<int:task_id>/', views.edit_task, name='edit-task'),
````
## 10.10 Crear funcionalidad "Eliminar tarea"

La última funcionalidad que falta por crear es la de eliminar tareas.

- Crear vista:
- Ve a `views.py` y define la vista que se encargará de la acción de eliminar tareas:
  ````
  def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()

    messages.success(request, '¡Tarea eliminada exitosamente!')

    return redirect('list-tasks')
  ````
  - Registrar URL:

## 10.11 Ve al archivo de URLs y agrega la ruta así:
````
path('delete-task/<int:task_id>/', views.delete_task, name='delete-task'),
````
# PUNTO B
## Envio de correo
1. Ve a la administración de tu cuenta de google
2. Ve a seguridad y activación en dos pasos
3. Luego, ve a contraseñas de aplicación
4. Crea tu SMTP y guarda la clave generada

- En `settings.py` agrega:
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tu_correo@gmail.com'
EMAIL_HOST_PASSWORD = 'jwhn kyio ttgb lwgk'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```
- Para enviar un correo desde cualquier vista, puedes usar:
```
from django.core.mail import send_mail
send_mail(
 'Asunto del correo',
 'Este es el contenido del correo.',
 'tu_correo@gmail.com', # Remitente (debe coincidir con EMAIL_HOST_USER)
 ['destinatario@gmail.com'], # Lista de destinatarios
 fail_silently=False,
)
```
- En `views.py` agrega:
```
def send_email_view(request):
    if request.method == 'POST':
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        recipient = request.POST.get('recipient', '')

        if subject and message and recipient:
            try:
                send_mail(subject, message, 'tu_correo@gmail.com', [recipient])
                messages.success(request, '¡Correo enviado exitosamente!')
            except Exception as e:
                messages.error(request, f'Error al enviar el correo: {e}')
        else:
            messages.error(request, 'Todos los campos son obligatorios.')

        return redirect('send-email')

    return render(request, 'send_email.html')
```
- Agrega los `imports`:
```
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
```
- En la carpeta templates, crea un nuevo archivo llamado `send_email.html`:
```
{% extends "base.html" %}

{% block content %}
<div class="container mt-5">
    <h2>Enviar Correo</h2>

    {% if messages %}
    <div class="alert-container">
        {% for message in messages %}
        <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
            {{ message }}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
        {% endfor %}
    </div>
    {% endif %}

    <form method="POST">
        {% csrf_token %}
        <div class="mb-3">
            <label class="form-label">Asunto:</label>
            <input type="text" name="subject" class="form-control" required>
        </div>
        <div class="mb-3">
            <label class="form-label">Mensaje:</label>
            <textarea name="message" class="form-control" rows="5" required></textarea>
        </div>
        <div class="mb-3">
            <label class="form-label">Destinatario:</label>
            <input type="email" name="recipient" class="form-control" required>
        </div>
        <button type="submit" class="btn btn-primary">Enviar Correo</button>
    </form>
</div>
{% endblock %}
```
- Agrega la ruta en `urls.py`:
```
path('send-email/', views.send_email_view, name='send-email'),
```
- En el archivo `base.html` agrega el enlace sidebar:
```
<a href="{% url 'send-email' %}">Enviar Correo</a>
```
- Corre el servidor, llena los datos de la funcionalidad que se acaba de crear con un correo destino y verifica la llegada de este mismo.
## Autenticación
Nota: Crea una carpeta en templates llamada `Auth` ya que ahí estaremos trabajando.
1. Configurar la autenticación en settings:
```
LOGIN_URL = "login" #ruta del login
LOGIN_REDIRECT_URL = "list-tasks" # Redirigir al usuario tras login
LOGOUT_REDIRECT_URL = "login" # Redirigir al login tras logout
```
2. Agregar las vistas para login y logout
```
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("list-tasks")  # Redirige a la lista de tareas
        else:
            messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, "login.html")

def user_logout(request):
    logout(request)
    return redirect("login")
```
3. Ve a la carpeta templates, crea el archivo `login.html` y agrega lo siguiente:
```
{% extends "base.html" %}

{% block content %}
<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <h2 class="text-center">Iniciar Sesión</h2>

            {% if messages %}
                {% for message in messages %}
                    <div class="alert alert-{{ message.tags }}">{{ message }}</div>
                {% endfor %}
            {% endif %}

            <form method="post">
                {% csrf_token %}
                <div class="mb-3">
                    <label class="form-label">Usuario</label>
                    <input type="text" name="username" class="form-control" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Contraseña</label>
                    <input type="password" name="password" class="form-control" required>
                </div>
                <button type="submit" class="btn btn-primary w-100">Ingresar</button>
            </form>

            <p class="text-center mt-3">
                ¿No tienes cuenta? <a href="{% url 'register' %}">Regístrate</a>
            </p>
        </div>
    </div>
</div>
{% endblock %}
```
4. Se deben proteger las demás vistas de tareas, por lo que agregaremos lo siguiente:
```
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Task  # Asegúrate de importar el modelo Task

@login_required
def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, "list_tasks.html", {"tasks": tasks})

```
5. En la urls, eliminaremos la ruta de de home y agregaremos la siguiente para que nuestro home sea el login:
```
path("", views.user_login, name="login"),
```
6. Creamos un nuevo archivo en `templates/Auth` llamado `register.html` y agregamos lo siguiente:
```
{% extends "base.html" %}

{% block content %}
<div class="container mt-5">
    <div class="row justify-content-center">
        <div class="col-md-6">
            <h2 class="text-center">Registro</h2>

            {% if messages %}
                {% for message in messages %}
                    <div class="alert alert-{{ message.tags }}">{{ message }}</div>
                {% endfor %}
            {% endif %}

            <form method="post">
                {% csrf_token %}
                <div class="mb-3">
                    <label class="form-label">Usuario</label>
                    <input type="text" name="username" class="form-control" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Correo Electrónico</label>
                    <input type="email" name="email" class="form-control" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Contraseña</label>
                    <input type="password" name="password1" class="form-control" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Confirmar Contraseña</label>
                    <input type="password" name="password2" class="form-control" required>
                </div>
                <button type="submit" class="btn btn-primary w-100">Registrarse</button>
            </form>

            <p class="text-center mt-3">
                ¿Ya tienes una cuenta? <a href="{% url 'login' %}">Inicia sesión</a>
            </p>
        </div>
    </div>
</div>
{% endblock %}
```
7. Crea la vista:
```
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe")
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            login(request, user)
            messages.success(request, "¡Registro exitoso!")
            return redirect("list-tasks")

    return render(request, "auth/register.html")
```
8. Define la ruta:
```
`path("register/", views.register, name="register"),
```
## Logout
1. Crear la vista:
```
def user_logout(request):
    logout(request)
    messages.success(request, "Sesión cerrada correctamente")
    return redirect("login")
```
2. Añadir la ruta:
```
path("logout/", views.user_logout, name="logout")
```
3. Añadir en el sidebar esto para mostrar el botón solo si se está logueado:
```
{% if user.is_authenticated %}
    <div class="logout-btn">
        <form action="{% url 'logout' %}" method="post">
            {% csrf_token %}
            <button type="submit" class="btn btn-danger w-100">Cerrar Sesión</button>
        </form>
    </div>
{% endif %}
```
## Autorización
Aclaraciones:
Django tiene grupos y permisos listos para usar:
## Grupos: 
Son conjuntos de permisos. Puedes agrupar usuarios bajo un rol ("Admin", "Usuario Normal").
## Permisos: 
Son acciones específicas que los usuarios pueden o no hacer ("Puede agregar tareas", "Puede
editar tareas")
## 1. Crear roles 
- Para crear los roles en `admin.py`, debemos ir a la ruta admin de nuestra url raíz (`http://localhost:8000/admin/`)
- Añadimos presionando `add`
- En `groups`, crearemos el Group user
- Agregaremos el permiso `can_view_task`
- Luego, en el grupo `admin` agregaremos todos los permisos

Ahora en registro, lo modificaremos para que se hagan según los grupos que creamos.
```
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe")
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)

            # Asignar grupo "Usuarios" automáticamente
            user_group, created = Group.objects.get_or_create(name="Usuarios")
            user.groups.add(user_group)

            login(request, user)
            messages.success(request, "¡Registro exitoso!")
            return redirect("list-tasks")

    return render(request, "auth/register.html")
```
Agregamos ls imports:
```
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```
Ahora podemos proteger nuestras rutas por permisos:
```
  from django.contrib.auth.decorators import permission_required
@permission_required("task.add_task", raise_exception=True)
```
Ahora al ejecutar la pagina e ingresar con un usuario normal, si intentamos crear una tarea, nos debería mostrar el error `403 Forbidden`. Sin embargo, al ingresar con las credenciales `admin` esto no pasay funciona normal.
## Manejo de roles 
Para hacer funcionalidades segun los roles tenemos que hacer una funcion para verificar que mi usuario pasa
un filtro definido por una función en esta caso vamos a verificar si es `admin`, es decir, si es superuser o
pertenece al grupo admin que creamos esto en `views.py`
```
def is_role_admin(user):
    return user.groups.filter(name="admin").exists() or user.is_superuser
```
Ahora podemos usar el decorador `@user_passes_test()` para restringir solo los usuario que cumplane esa
condición vamos a hacer una vista para gestionar los roles:
```
@login_required
@user_passes_test(is_role_admin)  # Solo admins pueden acceder
def manage_roles(request):
    users = User.objects.all()
    groups = Group.objects.all()

    if request.method == "POST":
        user_id = request.POST.get("user_id")
        group_id = request.POST.get("group_id")
        action = request.POST.get("action")

        try:
            user = User.objects.get(id=user_id)
            group = Group.objects.get(id=group_id)

            if action == "add":
                user.groups.add(group)
                messages.success(request, f"Se añadió {user.username} al grupo {group.name}.")
            elif action == "remove":
                user.groups.remove(group)
                messages.warning(request, f"Se eliminó {user.username} del grupo {group.name}.")
            else:
                messages.error(request, "Acción no válida.")

        except User.DoesNotExist:
            messages.error(request, "Usuario no encontrado.")
        except Group.DoesNotExist:
            messages.error(request, "Grupo no encontrado.")

        return redirect("manage-roles")

    return render(request, "roles/manage_roles.html", {"users": users, "groups": groups})
```
Agregamos los imports:
```
from django.contrib.auth.decorators import login_required, user_passes_test
```
Ahora creamos una carpeta llamada `role` y dentro de esta agregaremos el archivo `manage_role.html` en el cual pondremos lo siguiente:
```
{% extends "base.html" %}
{% block content %}
    <div class="container mt-5">
        <h2 class="mb-4">Administrar Roles</h2>
        {% if messages %}
            {% for message in messages %}
                <div class="alert alert-{{ message.tags }} alert-dismissible fade show">
                    {{ message }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
            {% endfor %}
        {% endif %}
        <div class="row">
            <div class="col-md-6">
                <h4>Usuarios</h4>
                <table class="table table-bordered">
                    <thead class="table-dark">
                        <tr>
                            <th>Usuario</th>
                            <th>Roles</th>
                            <th>Acciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for user in users %}
                            <tr>
                                <td>{{ user.username }}</td>
                                <td>
                                    {% for group in user.groups.all %}
                                        <span class="badge bg-info">{{ group.name }}</span>
                                    {% empty %}
                                        <span class="text-muted">Sin rol</span>
                                    {% endfor %}
                                </td>
                                <td>
                                    <form method="post" class="d-inline">
                                        {% csrf_token %}
                                        <input type="hidden" name="user_id" value="{{ user.id }}">
                                        <select name="group_id" class="form-select form-select-sm d-inline w-auto">
                                            {% for group in groups %}
                                                <option value="{{ group.id }}">{{ group.name }}</option>
                                            {% endfor %}
                                        </select>
                                        <button type="submit" name="action" value="add" class="btn btn-success btn-sm">Añadir</button>
                                        <button type="submit" name="action" value="remove" class="btn btn-danger btn-sm">Quitar</button>
                                    </form>
                                </td>
                            </tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
{% endblock %}

```
Agregamos la ruta:
```
path("admins/roles/", views.manage_roles, name="manage-roles"),
```
Con esto, al acceder a la pantalla de roles desde la ruta `http://localhost:8000/admins/roles/` y podremos manejar los roles desde ahí
## Manejo de permisos
## 1. Crear un archivo signals.py
Hacemos esto para manejar la creación cada que implementemos una nueva tarea.
```
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import Task

@receiver(post_save, sender=Task)
def create_task_permissions(sender, instance, created, **kwargs):
    if created:
        content_type = ContentType.objects.get_for_model(Task)
        
        view_perm = Permission.objects.create(
            codename=f'view_task_{instance.id}',
            name=f'Puede ver la tarea {instance.name}',
            content_type=content_type
        )
        
        edit_perm = Permission.objects.create(
            codename=f'edit_task_{instance.id}',
            name=f'Puede editar la tarea {instance.name}',
            content_type=content_type
        )
        
        delete_perm = Permission.objects.create(
            codename=f'delete_task_{instance.id}',
            name=f'Puede eliminar la tarea {instance.name}',
            content_type=content_type
        )
        
        print(f"Permisos creados para la tarea {instance.name}: {view_perm.codename}, {edit_perm.codename}, {delete_perm.codename}")

```
## 2. En el archivo apps.py agregaremos el siguiente metodo para TaskConfig:
```
def ready(self):
    import task.signals
```
Ahora crearemos una vista para que el administrador pueda manejar quien puede acceder a las tareas y de que manera.
## Creamos la vista:
```
@login_required
def assign_permissions(request):
    tasks = Task.objects.all()
    users = User.objects.all()

    if request.method == "POST":
        user_id = request.POST.get("user_id")
        task_id = request.POST.get("task_id")
        permission_type = request.POST.get("permission_type")

        user = User.objects.get(id=user_id)
        permission = Permission.objects.get(codename=f"{permission_type}_task_{task_id}")

        print("Se le agregó al usuario el permiso")
        print(f"{permission_type}_task_{task_id}")

        user.user_permissions.add(permission)

    return render(request, "assign_permissions.html", {"tasks": tasks, "users": users})
```
En la carpeta `templates` creamos el archivo `assign_permissions.html` y agregamos:
```
{% extends 'base.html' %}

{% block content %}
<div class="container mt-5">
    <h2>Asignar Permisos</h2>
    <form method="POST">
        {% csrf_token %}
        <div class="mb-3">
            <label for="user_id" class="form-label">Selecciona un usuario:</label>
            <select name="user_id" class="form-control">
                {% for user in users %}
                    <option value="{{ user.id }}">{{ user.username }}</option>
                {% endfor %}
            </select>
        </div>
        
        <div class="mb-3">
            <label for="task_id" class="form-label">Selecciona una tarea:</label>
            <select name="task_id" class="form-control">
                {% for task in tasks %}
                    <option value="{{ task.id }}">{{ task.name }}</option>
                {% endfor %}
            </select>
        </div>
        
        <div class="mb-3">
            <label for="permission_type" class="form-label">Tipo de Permiso:</label>
            <select name="permission_type" class="form-control">
                <option value="view">Ver</option>
                <option value="edit">Editar</option>
                <option value="delete">Eliminar</option>
            </select>
        </div>
        
        <button type="submit" class="btn btn-primary">Asignar Permiso</button>
    </form>
</div>
{% endblock %}
```
Agregamos la ruta:
```
 path("assign-permissions/", views.assign_permissions, name="assignpermissions"),
```
Ahora modificaremos la lógica de como se muestran las listas para hacerlo en función de los parametros establecidos.
- Modificamos la vista:
```
@login_required
def list_tasks(request):
    tasks = Task.objects.all()
    print(request.user.get_all_permissions())

    filtered_tasks = []

    for task in tasks:
        perm_view = f"task.view_task_{task.id}"
        perm_edit = f"task.edit_task_{task.id}"
        perm_delete = f"task.delete_task_{task.id}"
        
        print(perm_view)

        if request.user.has_perm(perm_view):
            print("tiene edit")
            print(request.user.has_perm(perm_edit))

            # Agregar permisos específicos a la tarea
            task.can_edit = request.user.has_perm(perm_edit)
            task.can_delete = request.user.has_perm(perm_delete)
            filtered_tasks.append(task)

    return render(request, "list_tasks.html", {"tasks": filtered_tasks})
```
- Modificamos el template `list_task.html` para que quede de la siguiente manera:
```
{% extends "base.html" %}
{% block content %}
<!DOCTYPE html>
<html lang="es">
<head>
    <title>Lista de Tareas</title>
</head>
<body class="bg-light">
    <div class="container mt-5">
        <h2 class="mb-4">Lista de Tareas</h2>

        {% if tasks %}
        <div class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th>ID</th>
                        <th>Estado</th>
                        <th>Nombre</th>
                        <th>Descripción</th>
                        <th>Fecha Límite</th>
                        <th>Creado</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {% for task in tasks %}
                    <tr>
                        <td>{{ task.id }}</td>
                        <td>{{ task.status_id.name }}</td>
                        <td>{{ task.name }}</td>
                        <td>{{ task.description }}</td>
                        <td>{{ task.deadline|default:"No definida" }}</td>
                        <td>{{ task.created_at|date:"F j, Y, g:i A" }}</td>
                        <td>
                            {% if task.can_edit %}
                            <a href="{% url 'edit-task' task.id %}" class="btn btn-warning btn-sm">Editar</a>
                            {% endif %}

                            {% if task.can_delete %}
                            <button class="btn btn-danger btn-sm" data-bs-toggle="modal" data-bs-target="#deleteModal" data-task-id="{{ task.id }}">
                                Eliminar
                            </button>
                            {% endif %}
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        {% else %}
        <div class="alert alert-info">No tienes permiso para ver ninguna tarea.</div>
        {% endif %}

        <a href="{% url 'create-task' %}" class="btn btn-primary mt-3">Crear Nueva Tarea</a>
    </div>

    <!-- Modal de confirmación de eliminación -->
    <div class="modal fade" id="deleteModal" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Confirmar eliminación</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <p>¿Estás seguro de que quieres eliminar esta tarea?</p>
                </div>
                <div class="modal-footer">
                    <form id="delete-form" method="POST">
                        {% csrf_token %}
                        <button type="submit" class="btn btn-danger">Eliminar</button>
                    </form>
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
                </div>
            </div>
        </div>
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", function() {
            var deleteModal = document.getElementById("deleteModal");
            deleteModal.addEventListener("show.bs.modal", function(event) {
                var button = event.relatedTarget;
                var taskId = button.getAttribute("data-task-id");
                var form = document.getElementById("delete-form");
                form.action = `/delete-task/${taskId}/`;
            });
        });
    </script>
</body>
</html>
{% endblock content %}
```
A partir de ahora, solo será posible ver, editar y eliminar las tareas para las cuales se tenga el permiso correspondiente. Es importante eliminar las tareas creadas hasta este momento, ya que no cuentan con permisos y podrían generar un error al intentar asignarlos.

En este caso, la lógica de los permisos se implementó de forma visual, pero las acciones aún pueden ejecutarse mediante la ruta, por lo que es necesario modificar la lógica de edición y eliminación.
```
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if not request.user.has_perm(f"task.change_task_{task.id}"):
        raise PermissionDenied("No tienes permiso para editar esta tarea.")

    if request.method == 'POST':
        task.name = request.POST.get('task-name', '')
        task.description = request.POST.get('task-description', '').strip()

        deadline_str = request.POST.get('task-deadline', '').strip()
        deadline = None

        if deadline_str:
            try:
                deadline = datetime.datetime.strptime(deadline_str, '%Y-%m-%d')
            except ValueError:
                pass

        task.deadline = deadline
        task.save()
        messages.success(request, '¡Tarea actualizada exitosamente!')
        return redirect('list-tasks')

    return render(request, 'edit_task.html', {
        'task': task,
        'task_statuses': Status.objects.all(),
    })


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if not request.user.has_perm(f"task.delete_task_{task.id}"):
        raise PermissionDenied("No tienes permiso para eliminar esta tarea.")

    task.delete()
    messages.success(request, '¡Tarea eliminada exitosamente!')
    return redirect('list-tasks')
```
Agregamos los imports:
```
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if not request.user.has_perm(f"task.change_task_{task.id}"):
        raise PermissionDenied("No tienes permiso para editar esta tarea.")

    if request.method == 'POST':
        task.name = request.POST.get('task-name', '')
        task.description = request.POST.get('task-description', '').strip()

        deadline_str = request.POST.get('task-deadline', '').strip()
        deadline = None

        if deadline_str:
            try:
                deadline = datetime.datetime.strptime(deadline_str, '%Y-%m-%d')
            except ValueError:
                pass

        task.deadline = deadline
        task.save()
        messages.success(request, '¡Tarea actualizada exitosamente!')
        return redirect('list-tasks')

    return render(request, 'edit_task.html', {
        'task': task,
        'task_statuses': Status.objects.all(),
    })


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if not request.user.has_perm(f"task.delete_task_{task.id}"):
        raise PermissionDenied("No tienes permiso para eliminar esta tarea.")

    task.delete()
    messages.success(request, '¡Tarea eliminada exitosamente!')
    return redirect('list-tasks')
```
Para finalizar, podemos realizar una conversión de las vistas que tenemos, ya que las hemos implementado como Vistas Basadas en Funciones, en este caso podemos presentar otras opciones, como por ejemplo las vistas basadas en clases.
Como por ejemplo, si decidieramos hacer la conversión, deberia quedar de la siguiente manera (cabe aclarar que solo es un ejemplo, por lo que no es practico usarlo en el codigo sin hacer los cambios pertinentes)
```
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect
from .models import Task

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "list_tasks.html"
    context_object_name = "tasks"

    def get_queryset(self):
        tasks = Task.objects.all()
        filtered_tasks = []
        for task in tasks:
            perm_view = f"task.view_task_{task.id}"
            perm_edit = f"task.edit_task_{task.id}"
            perm_delete = f"task.delete_task_{task.id}"
            if self.request.user.has_perm(perm_view):
                task.can_edit = self.request.user.has_perm(perm_edit)
                task.can_delete = self.request.user.has_perm(perm_delete)
                filtered_tasks.append(task)
        return filtered_tasks

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "create_task.html"
    fields = ["name", "description", "status", "deadline"]
    success_url = reverse_lazy("list-tasks")

    def form_valid(self, form):
        messages.success(self.request, "¡Tarea creada exitosamente!")
        return super().form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "edit_task.html"
    fields = ["name", "description", "status", "deadline"]
    success_url = reverse_lazy("list-tasks")

    def form_valid(self, form):
        messages.success(self.request, "¡Tarea actualizada exitosamente!")
        return super().form_valid(form)

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("list-tasks")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "¡Tarea eliminada exitosamente!")
        return super().delete(request, *args, **kwargs)
```
Seguido de esto, al haccer este cambio, se deberán actualizar las rutas:
```
from django.urls import path
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='list-tasks'),
    path('tasks/create/', TaskCreateView.as_view(), name='create-task'),
    path('tasks/edit/<int:pk>/', TaskUpdateView.as_view(), name='edit-task'),
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name='delete-task'),
]
```
## Migrar un cambio de dato
Migrar un cambio de dato en Django significa modificar los valores almacenados en la base de datos mediante una migración de datos, sin alterar la estructura de las tablas.

🔹 Ejemplo práctico
Si tienes un modelo Task con un campo status que almacena estados como "Pendiente", "En progreso", etc., y quieres actualizar todas las tareas "Pendiente" a "En progreso", puedes hacerlo con una migración de datos.

Siguiendo esto, podemos ir y establecer lo siguiente para ello:
```
def update_task_status(apps, schema_editor):
    Task = apps.get_model('tasks', 'Task')
    Task.objects.filter(status='Pendiente').update(status='En progreso')

class Migration(migrations.Migration):
    dependencies = [
        ('tasks', 'última_migración'),
    ]
    operations = [
        migrations.RunPython(update_task_status),
    ]
```
Suponiendo que tenemos un modelo tasks que almmacena tareas en pendiente y deseamos migrarlas a "en proceso".

# Agregar nuevas columnas 
```
class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50)
    new_field = models.CharField(max_length=100, default='Nuevo valor')  # Nuevo campo
```
Ejecutas en la consola: 
```
python manage.py makemigrations tasks
python manage.py migrate
```
Y si deseas cambiar el tipo de dato de la columna:
```
class Task(models.Model):
    status = models.IntegerField(default=0)  # Antes era CharField
```
## Crear una nueva tabla 
```
class Category(models.Model):
    name = models.CharField(max_length=255)
```
Y ejecutas:
```
python manage.py makemigrations tasks
python manage.py migrate
```
