from django.contrib import admin
from .models import *

admin.site.register(Item)
admin.site.register(Province)
admin.site.register(City)
admin.site.register(Technician)
admin.site.register(Comment)