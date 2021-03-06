"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path
from website import views
from downloads import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing_page,name ="landing_page"),
    path('studymaterials/',views.studymat,name="study_materials"),
    path('scholarships/',views.scholarships, name="scholarships"),
    path('course/',views.buycourse,name="buy_a_course"),
    path('about/', views.about, name = "about"),
    path('career/',views.career,name="career"),
    path('child/',views.child,name ="child"),
    path('privacypolicy/',views.privacy, name ="privacy"),
    path('termscondition/',views.termscondition, name="termscondition"),
    path('contact/',views.contact,name='contact'),
    path('blog/downloads/',v2.download, name ='downloads'),
    
    
    
]
