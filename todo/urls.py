from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("list/", views.todo_list_view, name="list"),
    path("item/<slug:item_slug>/", views.todo_item_view, name="item"),
    path("delete/<int:id>/", views.todo_list_delete, name="delete_list"),
    path("update/<slug:item_slug>/<int:instance_id>/", views.todo_item_update, name="update_item"),
    path("instance/<int:instance_id>/", views.todo_instance_view, name="instance"),
]