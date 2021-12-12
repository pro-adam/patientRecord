from django.shortcuts import redirect, render
from . models import Patient
from . forms import PatientForm
from django.contrib import messages


def index(request):
    data = Patient.objects.all()
    return render(request,'index.html',{'data':data})

def add_record(request):
    patientForm = PatientForm()
    if request.method == 'POST':
        patientForm = PatientForm(request.POST)
        if patientForm.is_valid():
            formSave  = patientForm.save(commit=False)
            formSave.save()
            messages.success(request,'record added')
            return redirect('index')
    context = {
        'patient':patientForm
    }
    return render(request,'add-record.html',context)

def update_record(request,patient_id):
    patient = Patient.objects.get(id=patient_id)
    patientForm = PatientForm(instance=patient)
    if request.method == 'POST':
        patientForm = PatientForm(request.POST,instance=patient)
        if patientForm.is_valid():
            formSave = patientForm.save(commit=False)
            formSave.save()
            messages.success(request,'data updated')
            return redirect('index')
    context = {
        'form':patientForm
    }
    return render(request,'update-record.html',context)

def delete_record(request,id):
    Patient.objects.filter(id=id).delete()
    return redirect('/')
