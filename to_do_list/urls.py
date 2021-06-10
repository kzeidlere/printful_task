"""to_do_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static, serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import todo_list.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_list.views.ToDoListView.as_view()),
    path('saraksts/', todo_list.views.ToDoDetailView.as_view()),
    path('templates/add_new_to_do.html', todo_list.views.AddToDoListView.as_view(), name='todo-list-add'),
    path('post/', todo_list.views.EditToDoListView.as_view(), name='todo_list_edit'),
    path('post/<int:pk>/delete/', todo_list.views.ListDeleteView.as_view(), name='todo-list-delete'),
    
]

urlpatterns += [
    path(settings.STATIC_URL[1:], serve, {'document_root': settings.STATIC_ROOT })
]
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT),
 