from django.contrib import admin

# Register your models here.
from .models import Student

admin.site.register(Student)
admin.site.site_title = "ÖGRENCİ UYGULAMASI"
admin.site.site_header = "ÖĞRENCİ Admin Portal"  
admin.site.index_title = "Welcome to ÖĞRENCİ Admin Portal"