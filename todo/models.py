from django.db import models
from django.urls import reverse
from datetime import datetime
from django.utils.text import slugify
from accounts.models import CustomRegistrationModel

class TodoList(models.Model):
    class Meta:
        ordering = ("-slug",)
        
    title = models.CharField(max_length=300)
    user = models.ForeignKey(CustomRegistrationModel, on_delete=models.CASCADE, related_name="lists")
    slug = models.SlugField(max_length=200, unique=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        now = datetime.now()
        if not self.slug:
            self.slug = f"{slugify(self.title)}-{str(now.year)}-{str(now.month)}-{str(now.day)}-{str(now.hour)}-{str(now.minute)}-{str(now.second)}"
            self.save()
    
    def get_absolute_url(self):
        return reverse("todo:item", kwargs={"item_slug": self.slug})
    

class TodoItem(models.Model):
    class Meta:
        ordering = ("-created",)
        
    title = models.CharField(max_length=400)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    todo_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name="items")
    
    def __str__(self):
        return '{}- {} | {}'.format(self.pk, self.todo_list, self.title)
    
