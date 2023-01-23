from django.shortcuts import render, get_object_or_404
from .models import TodoList, TodoItem
from django.contrib.auth.decorators import login_required
from .forms import TodoListForm, TodoItemForm
from django.shortcuts import redirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseNotFound

@login_required
def todo_list_view(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            TodoList.objects.create(**form.cleaned_data, user=request.user)
            object_list = TodoList.objects.filter(user=request.user)
            paginator = Paginator(object_list, 2)
            page_number = request.GET.get('page', '1')
            try:
                todo_list = paginator.page(page_number)
            except PageNotAnInteger:
                todo_list = paginator.page(1)
            except EmptyPage:
                todo_list = paginator.page(paginator.num_pages)
            form = TodoListForm()
    else:
        object_list = TodoList.objects.filter(user=request.user)
        paginator = Paginator(object_list, 2)
        page_number = request.GET.get('page', '1')
        try:
            todo_list = paginator.page(page_number)
        except PageNotAnInteger:
            todo_list = paginator.page(1)
        except EmptyPage:
            todo_list = paginator.page(paginator.num_pages)
        form = TodoListForm()
    return render(request, "todo/list.html", {"todo_list": todo_list, "form": form})




@login_required
def todo_item_view(request, item_slug):
    todo_item = TodoList.objects.get(slug=item_slug)
    items = todo_item.items
    if request.method == "POST":
        form = TodoItemForm(request.POST)
        if form.is_valid():
            TodoItem.objects.create(**form.cleaned_data, todo_list=todo_item)
            form = TodoItemForm()
    else:
        form = TodoItemForm()
    return render(request, "todo/item.html", {"todo_item": todo_item, "items": items, "form": form})




def todo_list_delete(request, id):
    object = TodoList.objects.get(id=id)
    if request.method == "POST":
        object.delete()
        return redirect("todo:list")
    
    
    
    
def todo_item_update(request, item_slug, instance_id):
    object = TodoItem.objects.get(id=instance_id)
    if request.method == "POST" and "delete" in request.POST:
        object.delete()
        return redirect(reverse("todo:item", args=[item_slug]))
    elif request.method == "POST" and "update" in request.POST:
        object.status = True
        object.save()
        return redirect(reverse("todo:item", args=[item_slug]))
    
    
    
    
def todo_instance_view(request, instance_id):
    # try:
    #     object = TodoItem.objects.get(id=instance_id)
    # except TodoItem.DoesNotExist:
    #     return HttpResponseNotFound("TodoItem not found!")
    # return render(request, "todo/instance.html", {"object": object})
    
    object = get_object_or_404(TodoItem, id=instance_id)
    return render(request, "todo/instance.html", {"object": object})