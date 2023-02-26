from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from to_do.forms import doform
from .models import dolist
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView,DeleteView

class classView(ListView):
    model=dolist
    template_name= 'todo_list.html'
    context_object_name = 'list'

class detailedView(DetailView):
    model=dolist
    template_name= 'detail.html'
    context_object_name = 'list'

class viewupdate(UpdateView):
    model=dolist
    template_name= 'edit.html'
    context_object_name = 'list'
    fields= ('name','prior','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class viewdelete(DetailView):
    model=dolist
    template_name= 'delete.html'
    success_url = reverse_lazy('cbv')
# Create your views here.
# def todofun(request):
#     return render(request,'todo_list.html')

def add_list(request):
    dolists = dolist.objects.all()
    if request.method=="POST":
        task= request.POST.get('task','')
        prior= request.POST.get('prior','')
        date= request.POST.get('date','')
        list=dolist(name=task,prior=prior,date=date)
        list.save()
    return render(request,'todo_list.html',{'list':dolists})

def delete(request,taskid):
    task=dolist.objects.get(id=taskid)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    task= dolist.objects.get(id=id)
    form=doform(request.POST or None , instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'update.html',{'form':form,'task':task})