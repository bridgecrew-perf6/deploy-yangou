from django.contrib import admin

from . models import *

class FormatOne(admin.ModelAdmin):
    list_display = ('name', 'age', 'description', 'image')

admin.site.register(Character,FormatOne)





