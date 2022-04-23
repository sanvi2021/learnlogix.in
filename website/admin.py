from django.contrib import admin
from .models import landing_pageRegistrationForm
# Register your models here.
@admin.register(landing_pageRegistrationForm)
class Landingleads(admin.ModelAdmin):
    list_display =('id', 'name','email','phone')
    