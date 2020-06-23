from django.conf import settings
from rest_framework import serializers

from policies.serializers import PolicySerializer
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    policies = PolicySerializer(many=True, read_only=True)
    dob = serializers.DateField(format=settings.DATE_FORMAT, input_formats=[settings.DATE_FORMAT, ])

    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'dob', 'policies')


class CustomerPolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('policies',)
