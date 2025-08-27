from django.contrib import admin

# Register your models here.
from .models import Status, Task

admin.site.register(Status)
admin.site.register(Task)