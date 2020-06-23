from django.db import transaction
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Customer
from .serializers import CustomerSerializer, CustomerPolicySerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(methods=['put', 'delete'], detail=True, serializer_class=CustomerPolicySerializer)
    def policies(self, request, *args, **kwargs):
        if request.method == 'PUT':
            return self.add_policies(request, *args, **kwargs)
        elif request.method == 'DELETE':
            return self.remove_policies(request, *args, **kwargs)

    def add_policies(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

    def remove_policies(self, request, pk=None):
        customer = self.get_object()
        serializer = self.get_serializer(instance=customer, data=request.data)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            customer.policies.remove(*serializer.data.get('policies'))
        return Response(data=self.get_serializer(instance=customer).data)
