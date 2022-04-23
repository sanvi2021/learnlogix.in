from unicodedata import name
from django.shortcuts import render
from .forms import landing_pageleads

# Create your views here.

#def landing_page(request):
  #  if request.method  == 'POST':
   #     leads = landing_pageleads(request.POST)
   #     if leads.is_valid():
   #         leads.save()
   #         print("form is valid and data is saved")
   #     else:
    #        print('Form is not validated, not saved')
   # else:
    #    leads= landing_pageleads()
    #return render(request,'index.html',{"leads":leads})

def landing_page(request):
    return render(request,'index.html')



    


