from django.shortcuts import render,redirect
from .forms import AseForm
from .models import Ase

# Create your views here.
def ase_list(request):
    context = {'ase_list':Ase.objects.all()}
    return render(request,"ase_register/ase_list.html",context)

def ase_form(request):
    if request.method == 'GET':
        form = AseForm()
        return render(request,"ase_register/ase_form.html",{'form':form})
    else:
        form = AseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ase/list')
        else:
            return redirect('/ase/form')
            
def ase_delete(request):
    return 