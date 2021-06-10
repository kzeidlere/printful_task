from django.db import models


class ToDoList(models.Model):
    title = models.CharField(max_length=20, default='title')
    text = models.TextField(default='text')
