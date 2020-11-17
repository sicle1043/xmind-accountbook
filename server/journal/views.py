from django.shortcuts import render

from rest_framework import viewsets
from .models import Record, Category
from .serializers import RecordSerializers, CategorySerializers

# Create your views here.


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all().order_by('-time')
    serializer_class = RecordSerializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializers
