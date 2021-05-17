from django import forms
from django.db.models import fields
from .models import Document,Patient 

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document 
        fields = ('name','document')

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'        