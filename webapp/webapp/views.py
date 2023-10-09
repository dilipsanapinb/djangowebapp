from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm


def home(request):
    todos=Todo.objects.all()

    return render(request,"index.html",{'todos':todos})


def aboutus(request):
    return render(request,'aboutus.html')

def create_todo(request):
    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=TodoForm()
    return render(request,'index.html',{'form':form})

