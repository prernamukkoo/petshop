from django import forms
from .models import Info
# creating a form

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info 
        fields = ('name', 'email', 'subject', 'message')