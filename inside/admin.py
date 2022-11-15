from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ['username', 'task_name', 'per_day']


admin.site.register(Task, TaskAdmin)
