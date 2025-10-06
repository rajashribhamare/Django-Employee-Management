from django.contrib import admin

# Register your models here.
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created_at')  # Show these fields in the admin list
    list_filter = ('completed',)  # Add filter for completed tasks
    search_fields = ('title', 'description')  # Enable search

