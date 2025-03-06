# Django- BASIC  
## Acerca del proyecto
En este repositorio encontrarás un paso a paso básico de cómo crear una aplicación,  usando Python Django para la gestión de tareas pendientes. Se explica los pasos para configurar un entorno virtual, instalar dependencias y manejo de usuarios, correos, etc.
# Instalación y configuración
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
# Creación de la aplicación de tareas 
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

Dentro de la carpeta de tu aplicación (tasks/), crea una nueva carpeta llamada templates/.
Dentro de templates/, crea un archivo denominado base.html.
Agrega el siguiente código en el archivo base.html:
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
Dentro de la carpeta templates/, crea un archivo llamado home.html.

Luego, agrega el siguiente código dentro de home.html:

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
6. Configurar la URL para la Página Principal

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


A continuación, inicia el servidor como lo hiciste anteriormente y verifica que todo funcione correctamente.
Antes de hacerlo, es necesario actualizar algunas líneas en el archivo base.html que acabas de crear:


```
<a href="{% url 'list-tasks' %}">Ver Tareas</a>
<a href="{% url 'create-task' %}">Crear Tarea</a>
```
actualizadas:
```
<a href="">Ver Tareas</a>
<a href="">Crear Tarea</a>
```
7. Definir el Modelo para Tareas
Ahora que ya tienes la estructura del proyecto, es momento de desarrollar la lógica de negocio para que la aplicación no solo muestre un mensaje de bienvenida, sino que también permita gestionar tareas: crearlas, editarlas y eliminarlas.

Para ello, sigue estos pasos:

- Abre el archivo models.py dentro de la aplicación.
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
Modelo para representar las tareas:
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

Generar las migraciones ejecutando el siguiente comando en la terminal:
```
python manage.py makemigrations
```
Esto creará un archivo de migración con los cambios en los modelos.

Aplicar las migraciones con:
```
python manage.py migrate
```
Esto actualizará la base de datos con la estructura definida en los modelos.
Con estos comandos, la base de datos reflejará las modificaciones realizadas en models.py.

8. Panel de administración y agregar modelos
   
Para registrar los modelos en el panel de administración de Django, sigue estos pasos:

- Abre el archivo admin.py dentro de la aplicación tasks.

- Importa los modelos que creaste en models.py:
```
from .models import Status, Task
```
Registra tus modelos:
```
admin.site.register(Status)
admin.site.register(Task)
```
9. Panel de administración
Ahora que tus modelos de datos están listos para funcionar, puedes aprovechar el panel de administración predeterminado de Django.

Este panel proporciona una interfaz web automática que facilita la gestión de los datos del proyecto sin necesidad de escribir consultas SQL. A través de él, puedes crear, modificar y eliminar registros en la base de datos, administrar usuarios y sus permisos, y visualizar los modelos de manera organizada.

Para acceder a este panel, es necesario crear un súper-usuario.
```
python manage.py createsuperuser
```
Nota: al ejecutar el codigo, saldrá una consola la cual te pedirá algunos datos.

Después de crear el súper-usuario, puedes acceder al panel de administración. Para hacerlo, inicia el servidor y dirígete a la ruta /admin en tu navegador (por ejemplo: http://localhost:8000/admin/). Allí encontrarás una página de inicio de sesión donde podrás ingresar con las credenciales creadas.
Explora el panel de administración para familiarizarte con su funcionamiento y crea los diferentes estados en los que podrán estar tus tareas.

10. Crear funcionalidades 
- Implementar la funcionalidad de "Creación de Tareas"
Ahora es momento de añadir la funcionalidad que permitirá a los usuarios agregar nuevas tareas a la aplicación.

El proceso sigue la misma estructura que utilizaste para mostrar la pantalla principal:

- Crear una vista que maneje las solicitudes de creación de tareas y genere una respuesta adecuada.
- Diseñar la plantilla HTML que servirá como interfaz para el usuario.
- Registrar la URL que permitirá acceder a esta nueva funcionalidad.
Estos tres pasos se repetirán cada vez que quieras agregar una nueva pantalla o funcionalidad a la aplicación.
10.1 Crear vista:
- Ve a views.py y define la vista:
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
10.2 Diseñar la pantalla HTML
Para que la vista pueda renderizar contenido, es necesario crear una plantilla HTML.

Dirígete a la carpeta donde se encuentran los templates de la aplicación.
Crea un nuevo archivo llamado create_task.html.
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
10.3 Registrar la URL:
Para permitir el acceso a la pantalla de creación de tareas, es necesario registrar la ruta correspondiente en el archivo de URLs de la aplicación.

Abre el archivo urls.py dentro de la aplicación.
Agrega la siguiente ruta:
```
path('create-task/', views.create_task, name='create-task'),
```
10.4 Crear funcionalidad "Ver lista de Tareas"
Ahora tienes que crear una pantalla que te permita ver las tareas creadas hasta el momento, con su respectiva información.
Crear vista:
- Ve a views.py y define la vista con la que se renderizará la pantalla de listado de tareas:
```
def list_tasks(request):
    return render(request, 'list_tasks.html', {
        'tasks': Task.objects.all(),
    })
```
10.5 Crear la pantalla HTML:

Ve a templates/ y crea un archivo con el nombre list_tasks.html.

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


10.6 Registrar URL:

Ve al archivo de URLs y agrega la ruta así:

````
path('list-tasks/', views.list_tasks, name='list-tasks'),
````
10.7 Crear funcionalidad "Editar tarea"
Ahora debes implementar una forma de editar las tareas que ya hayas creado.
- Crear vista:
- Ve a views.py y define la vista con la que se renderizará la pantalla de edición de tareas:
  ````
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
10.8 Crear la pantalla HTML:

Ve a templates/ y crea un archivo con el nombre edit_task.html.

Dentro de este archivo, pon el código:
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
10.9 Registrar URL:

Ve al archivo de URLs y agrega la ruta así:
````
path('edit-task/<int:task_id>/', views.edit_task, name='edit-task'),
````
10.10 Crear funcionalidad "Eliminar tarea"

La última funcionalidad que falta por crear es la de eliminar tareas.

- Crear vista:
- Ve a views.py y define la vista que se encargará de la acción de eliminar tareas:
  ````
  def delete_task(request, task_id):
    Task.objects.get(id=task_id).delete()

    messages.success(request, '¡Tarea eliminada exitosamente!')

    return redirect('list-tasks')
  ````
  - Registrar URL:

Ve al archivo de URLs y agrega la ruta así:
````
path('delete-task/<int:task_id>/', views.delete_task, name='delete-task'),
````













