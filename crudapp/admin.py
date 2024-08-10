from django.contrib import admin
from . import models


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'email','age', 'created_at', 'updated_at']

admin.site.register(models.Student, StudentAdmin)
