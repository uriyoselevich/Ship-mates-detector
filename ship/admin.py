from django.contrib import admin
from .models import Department, Soldier, SingleRecord

admin.site.register(Department)
admin.site.register(Soldier)
admin.site.register(SingleRecord)
