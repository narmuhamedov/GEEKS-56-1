from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms

#CRUD - Create Read Update Delete

#Create
def create_todo_view(request):
  if request.method == 'POST':
    form = forms.TodoForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('todo_list')
  else:
    form = forms.TodoForm()
  return render(request, 'create_todo.html', context={'form': form})

#Read
def read_todo_view(request):
  if request.method == 'GET':
    todo = models.Todo.objects.all().order_by('-id')
    context = {'todo': todo}
    return render(request, 'todo_list.html', context=context)


#Update
def update_todo_view(request, id):
  todo_id = get_object_or_404(models.Todo, id=id)
  if request.method == 'POST':
    form = forms.TodoForm(request.POST, instance=todo_id)
    if form.is_valid():
       form.save()
       return redirect('todo_list')
  else:
    form = forms.TodoForm(instance=todo_id)
  context = {
    'form': form,
    'todo_id': todo_id,
  }  
  return render(request, 'update_todo.html', context=context)

#Delete
def delete_todo_view(request, id):
  todo_id = get_object_or_404(models.Todo, id=id)
  todo_id.delete()
  return redirect('todo_list')