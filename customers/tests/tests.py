# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import resolve
from rest_framework import status
from rest_framework.reverse import reverse

from rest_framework.test import APIClient

from customers.tests.factories import CustomerFactory, PolicyFactory


class CustomerTestCase(TestCase):
    def setUp(self):
        self.customer = CustomerFactory()
        self.policy1 = PolicyFactory()
        self.policy2 = PolicyFactory()
        self.policy_list = [self.policy1.pk, self.policy2.pk]
        self.client = APIClient()

    def test_add_policies_to_customer(self):
        url = reverse('customer-add-policies', kwargs={"pk": self.customer.pk})
        response = self.client.post(url, data={"policies": self.policy_list})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.customer.policies.count(), 2)

    def test_remove_policies_to_customer(self):
        self.customer.policies.add(*self.policy_list)
        url = reverse('customer-remove-policies', kwargs={"pk": self.customer.pk})
        response = self.client.post(url, data={"policies": self.policy_list})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.customer.policies.count(), 0)
