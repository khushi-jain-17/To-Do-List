from django.shortcuts import render,redirect
from .models import Todo 

def index(request):
    todo = Todo.objects.all()
    if request.method == 'POST':
        todo = Todo(
            title = request.POST['title']
        )
        todo.save()
        return redirect('index')
    return render(request,'index.html',{ 'todos': todo })

def delete(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')

