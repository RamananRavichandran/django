from django.shortcuts import render,redirect
from .forms import AseForm
from .models import Ase

# Create your views here.
def ase_list(request):
    context = {'ase_list':Ase.objects.all()}
    return render(request,"ase_register/ase_list.html",context)

def ase_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = AseForm()
        else:
            ase = Ase.objects.get(pk=id)
            form = AseForm(instance=ase)
        return render(request,"ase_register/ase_form.html",{'form':form})
        
    else:
        if id == 0:
            form = AseForm(request.POST)
        else:
            ase = Ase.objects.get(pk=id)
            form = AseForm(request.POST,instance=ase)
        if form.is_valid():
            form.save()
            return redirect('/ase/list')
        else:
            return redirect('/ase/form')

def ase_delete(request,id):
    ase = Ase.objects.get(pk=id)
    ase.delete()
    return redirect('/ase/list')