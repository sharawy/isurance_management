from django.db import transaction
from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Customer
from .serializers import CustomerSerializer, CustomerPolicySerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(['POST'], detail=True, serializer_class=CustomerPolicySerializer)
    def add_policies(self, request, pk=None):
        customer = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            with transaction.atomic():
                customer.policies.add(*serializer.data.get('policies'))
            return Response(data=CustomerSerializer(instance=customer).data)

    @action(['POST'], detail=True, serializer_class=CustomerPolicySerializer)
    def remove_policies(self, request, pk=None):
        customer = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            with transaction.atomic():
                customer.policies.remove(*serializer.data.get('policies'))
            return Response(data=CustomerSerializer(instance=customer).data)
