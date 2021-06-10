from django import forms
from todo_list.models import ToDoList


class ToDoListForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = [
            'title',
            'text',
        ]
