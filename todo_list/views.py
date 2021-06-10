from django.shortcuts import render, redirect
from django.views.generic import ListView,DetailView, FormView, View 
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView

from todo_list.models import ToDoList
from todo_list.forms import ToDoListForm


class ToDoListView(ListView):
    model = ToDoList
    template_name = 'todo_list.html'
   

class ToDoDetailView(DetailView):
    models = ToDoList
    template_name = 'todo_list_details.html'


class AddToDoListView(FormView):
    form_class = ToDoListForm
    template_name = 'add_new_to_do.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)

        return response


class EditToDoListView(View):
    def get(self, request):
        form = ToDoListForm()

        context = {
            'form': form,
        }

        return render(
            template_name='todo_list_edit.html',
            context=context,
            request=request,
        )

    def post(self, request, todo_list_edit):
        dolist = ToDoList.object.get(name=todo_list_edit)

        title = request.POST['title']
        text = request.POST['text']

        if len(title) != 0:
            dolist.title = title

        if len(text) != 0:
            dolist.text = text

        dolist.save()

        return redirect(reverse_lazy('todo-list-edit'))


class ListDeleteView(DeleteView):
    model = ToDoList
    success_url = '/'
