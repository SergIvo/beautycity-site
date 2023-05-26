from rest_framework.serializers import ModelSerializer

from .models import Application
from phonenumber_field.serializerfields import PhoneNumberField

from django.db import transaction


class ApplicationSerializer(ModelSerializer):
    phonenumber = PhoneNumberField()

    class Meta:
        model = Application
        fields = ['name', 'phonenumber', 'question']

    @transaction.atomic
    def create(self, validated_data):
        new_application = Application.objects.create(**validated_data)
        return new_application
