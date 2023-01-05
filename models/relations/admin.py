from django.contrib import admin
from .models import *  # * ile tüm  models verileri import ettik

admin.site.register(Creator)
admin.site.register(Language)
admin.site.register(Freamwork)
admin.site.register(Develepor)



# Register your models here.
