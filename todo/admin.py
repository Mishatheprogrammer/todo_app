from django.contrib import admin
from .models import Task
# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'updated_at')
    search_fields = ('task',)

admin.site.register(Task, TaskAdmin) 
# This line registers the Task model with the Django admin site, allowing it to be managed through the admin interface.
