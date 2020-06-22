# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass
