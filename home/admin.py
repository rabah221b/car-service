from django.contrib import admin

from .models import classofvechiles 
from .models import vechiles
from .models import booking
# Register your models here.

admin.site.register(classofvechiles)
admin.site.register(vechiles)
admin.site.register(booking)