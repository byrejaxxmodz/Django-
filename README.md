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




