from django.shortcuts import render,redirect
from .forms import EmployeeForms,AdminForms
from .models import employee


# Create your views here.
def home(request):
    return render(request,'home.html')

def slider(request):
    return render(request,'slider.html')

def Employee(request):
    form=EmployeeForms
    if request.method=='POST':
        emp_form=EmployeeForms(request.POST)
        if emp_form.is_valid():
            emp_form.save()
            return redirect('/Employee')
    return render(request,'employee.html',{'form':form})

def Employee_list(request):
    data=employee.objects.all()
    return render(request,'employeelist.html',{'data':data})

def deleteemployee(request,id):
    name=employee.objects.get(id=id)
    name.delete()
    return redirect('/list') #1 1 data ko id ke throgh delete kr denga

def updatemployee(request,id):
    name=employee.objects.get(id=id)
    form=EmployeeForms(instance=name)
    if request.method == 'POST':
        saveform=EmployeeForms(request.POST or None,instance=name)
        if saveform.is_valid():
            saveform.save()
            return redirect('/list')
    return render(request,'updatemployee.html',{'form':form})

def addemployee(request):
    form=EmployeeForms
    if request.method == 'POST':
        saveform=EmployeeForms(request.POST)
        if saveform.is_valid():
            saveform.save()
            return redirect('/list')
    return render(request,'addemployee.html',{'form':form})


def register(request):
    form=AdminForms
    if request.method=='POST':
        admin_form= AdminForms(request.POST)
        if admin_form.is_valid():
            admin_form.save()
            return redirect('/register')
    else:
        form=AdminForms

    return render(request,'registration/adminregistor.html',{'form':form})

