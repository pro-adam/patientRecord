from django.db import models
from django.forms import ModelForm, fields
from . models import Patient

class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('full_name','email','mobile_no','address','detail','precaution','next_visit_date')