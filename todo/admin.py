from django.contrib import admin
from .models import TodoList, TodoItem

class TodoItemAdminInline(admin.TabularInline):
    model = TodoItem
    readonly_fields = ("created", "updated")
    fields = ("todo_list", "title", "created", "status")
    extra = 0
    
    
@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ("slug", "title", "user")
    readonly_fields = ("slug",)
    inlines = (TodoItemAdminInline,)