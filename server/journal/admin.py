from django.contrib import admin
from .models import Category, Record

# Register your models here.
admin.site.register(Record)
admin.site.register(Category)
# class BlogTypeAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'name')
