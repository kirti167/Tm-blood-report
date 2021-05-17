from os import name
from re import I
import re
from django.db import models
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, reverse
from django.http import HttpResponse
from django.views.generic.edit import UpdateView
from .models import Patient,Document,TestResult
from django.views.generic import CreateView,UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import View
from .forms import DocumentForm,PatientForm
from .process import main

# Create your views here.
def home(request):
    template_name = 'patient/home.html'
    context = {
        'patient':Patient.objects.all()
    }
    return render(request,template_name=template_name,context=context)

class PatientCreateView(CreateView):
    model = Patient
    template_name = 'patient/patient_create.html'
    fields = '__all__'
    def get_success_url(self):
        return reverse('patient_detail',kwargs={'pk':self.object.pk})

class PatientUpdateView(View):
    
    template_name = 'patient/patient_create.html'
    fields = '__all__'

    def get(self,request,pk):
        form = PatientForm()
        patient =Patient.objects.all()
        form.patient = patient
        context = {
            'form':form,
            'pk':pk,
            'patient':patient
            
        }

        return render(request,self.template_name,context=context) 

    def post(self,request,pk):
        
        patient =Patient.objects.get(pk=pk)
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
        return reverse('home')





    #def get_success_url(self,request,pk):

    #    return reverse('home')

class DocumentCreateView(CreateView):
    model = Document
    template_name = 'patient/document_create.html'
    fields = ('name','document')
    def get_success_url(self):
        return reverse('home')

class DocumentUploadView(View):
    template_name = 'patient/document_upload.html'

    def get(self,request,pk):
        form = DocumentForm()
        context = {
            'form':form,
            'pk':pk
        }
        return render(request,self.template_name,context)
    def post(self,request,pk):
        patient = Patient.objects.get(pk=pk)
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.patient = patient
            form.save()
            data = main(form.document.path)
            data = eval(data)
            for item in data:
                name = item['name']
                value = item['Value']
                unit = item['Unit']
                testresult = TestResult.objects.create(
                    name = name,
                    unit = unit,
                    value = value,
                    patient = patient,
                    document = form
                )
                testresult.save()
            print(data)

            context= {
                'form':DocumentForm(),
                'pk':pk,
                'data':data
            }
        return redirect(reverse('response',kwargs={'patient_id':patient.id,'document_id':form.id}))
class DisplayResponseView(View):
    template_name = 'patient/dispaly_response.html'
    def get(self,request,patient_id,document_id):
        patient_obj = Patient.objects.get(pk=patient_id)
        document_obj = Document.objects.get(pk=document_id)
        all_testresult = TestResult.objects.filter(patient=patient_obj,document=document_obj)
        context = {
            'all_testresult':all_testresult
        }
        return render(request,self.template_name,context)


class PatientProfileView(DetailView):
    model = Patient
    template_name = 'patient/patient_detail.html'
    context_object_name = 'patient'        

