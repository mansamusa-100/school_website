from django.contrib import admin

from .models import *

# Register your models here.


@admin.register(AdmissionForm)
class AdmissionFormAdmin(admin.ModelAdmin):
    list_display = ('user', 'fullname', 'status')
    list_filter = ('status',)
    search_fields = ('fullname', 'user__username')