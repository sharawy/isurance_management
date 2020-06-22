# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.validators import MaxValueValidator
from django.utils import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _


class Customer(models.Model):
    first_name = models.CharField(max_length=256, verbose_name=_("First name"))
    last_name = models.CharField(max_length=256, verbose_name=_("Last name"))
    dob = models.DateField(validators=[MaxValueValidator(limit_value=timezone.now().date())],
                           help_text=_("Enter the date of birth"), verbose_name=_("Date of birth"))

    policies = models.ManyToManyField('policies.Policy', related_name='customers', blank=True, null=True)

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return self.get_full_name()
