from django.contrib import admin
from .models import alldata

# Register your models here.

class AlldataAdmin(admin.ModelAdmin):
    pass

admin.site.register(alldata,AlldataAdmin)