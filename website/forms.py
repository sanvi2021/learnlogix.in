from dataclasses import fields
from logging import error
from sre_constants import IN
from tkinter.ttk import Widget
from turtle import textinput, width
from django.core import validators
from django import forms
from .models import landing_pageRegistrationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class landing_pageleads(forms.ModelForm): 
   

    class Meta:
        model = landing_pageRegistrationForm
        fields = ['name','email','phone']
        labels = {'name': 'Name', 'email': 'Email id','phone':'Phone Number'}
        
        widgets = {
                    'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Candidate name'}),
                    'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Correct Email Id'}),
                    'phone': forms.TextInput(attrs={'class':'form-control'}),
                    
        }
        phone = PhoneNumberField(widget = PhoneNumberPrefixWidget(initial='IN'))
        
        