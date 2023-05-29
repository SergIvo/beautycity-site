from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import Application, Review
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


class ReviewSerializer(ModelSerializer):
    phonenumber = PhoneNumberField()
    score = serializers.IntegerField()

    class Meta:
        model = Review
        fields = ['name', 'phonenumber', 'text', 'score']

    @transaction.atomic
    def create(self, validated_data):
        new_review = Review.objects.create(**validated_data)
        return new_review
