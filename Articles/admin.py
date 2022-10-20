from django.contrib import admin
from .models import *
# Register your models here.
class SourceAdmin(admin.ModelAdmin):
    filter_horizontal = ("articles",)
admin.site.register(Article)
admin.site.register(Source, SourceAdmin)