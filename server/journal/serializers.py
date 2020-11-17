from django.db import models
from rest_framework import serializers
from .models import Record, Category


class RecordSerializers(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = [
            'id',
            'type',
            'time',
            'category',
            'amount',
        ]


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'type',
        ]