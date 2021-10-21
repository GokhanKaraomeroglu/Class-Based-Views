from django import  forms
from django.forms import fields
from .models import Student
from django.core.exceptions import ValidationError


class StudentForm(forms.ModelForm):
    def clean_number(self):
        number = self.cleaned_data['number']
        if not (1000 < number < 1000):
            raise ValidationError ('Student Number is not valid')
        return number
        
    
    
    class Meta:
        model = Student
        fields = "__all__"