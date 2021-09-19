from django import forms
from .models import *

class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        models = Employee
        fields = '__all__'