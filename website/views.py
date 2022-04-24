from operator import imod
from unicodedata import name
from django.shortcuts import render
from .forms import landing_pageleads
from .models import landing_pageRegistrationForm

# Create your views here.

def landing_page(request):
      if request.method =='POST':
            leads = landing_pageleads(request.POST)
            if leads.is_valid():
                  name = leads.cleaned_data['name']
                  email = leads.cleaned_data['email']
                  phone = leads.cleaned_data['phone']
                  lead = landing_pageRegistrationForm(name=name, email=email, phone=phone)
                  lead.save()
                  leads = landing_pageleads()
            print('===== Information is captured======')
      else:
            leads = landing_pageleads()
      return render(request,'index.html',{"leads":leads})

def studymat(request):
      return render(request,'studymaterials.html')


def scholarships(request):
      return render(request,'scholarships.html')

def buycourse(request):
      return render(request,'course.html')
    
    



    


