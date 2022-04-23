from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Person

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields= ('Aadhar_id', 'name', 'address', 'phone_no')