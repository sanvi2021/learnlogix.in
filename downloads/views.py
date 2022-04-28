from django.shortcuts import render, HttpResponseRedirect

# Create your views here.
def download(request):
    return render(request,'download.html')
    