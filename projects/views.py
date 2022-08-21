from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Project, Task, Category
from .forms import ProjectCreateForm, ProjectUpdateForm

# Create your views here.

class ProjectListView(ListView):
    model = Project
    template_name = 'project/list.html'


class ProjectCreateView(CreateView):
    model = Project
    template_name = 'project/create.html'
    form_class = ProjectCreateForm
    success_url = reverse_lazy('Project_list')


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project/update.html'
    form_class = ProjectUpdateForm
    def get_success_url(self):
        return reverse('Project_update', args=[self.object.id])  # the word object refers to the same object which we edit 


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy('Project_list')
    context_object_name = 'project'


class TaskCreateView(CreateView):
    model = Task
    fields = ['project', 'description']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['is_completed']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])


class TaskDeleteView(DeleteView):
    model = Task

    def get_success_url(self):
        return reverse('Project_update', args=[self.object.project.id])
