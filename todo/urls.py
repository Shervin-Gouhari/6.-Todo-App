from django.urls import path
from .views import *

app_name = "todo"

urlpatterns = [
    path("list/", todo_list_view, name="list"),
    path("item/<slug:item_slug>/", todo_item_view, name="item"),
    path("delete/<int:id>/", todo_list_delete, name="delete_list"),
    path("update/<slug:item_slug>/<int:instance_id>/", todo_item_update, name="update_item"),
    path("instance/<int:instance_id>/", todo_instance_view, name="instance"),
]