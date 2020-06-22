from django.db import models
from django.utils.translation import gettext_lazy as _


class Policy(models.Model):
    PERSONAL_ACCIDENT_TYPE = 'personal-accident'
    TRAVEL_TYPE = 'travel'
    PROPERTY_TYPE = 'property'
    TYPES = [
        (PERSONAL_ACCIDENT_TYPE, _('Personal Accident')),
        (TRAVEL_TYPE, _('Borrowed by someone')),
        (PROPERTY_TYPE, _('Archived - not available anymore')),
    ]
    type = models.CharField(choices=TYPES, max_length=25)
    premium = models.DecimalField(decimal_places=2, max_digits=12)
    cover = models.DecimalField(decimal_places=2, max_digits=12)

    class Meta:
        verbose_name = _("Policy")
        verbose_name_plural = _("Policies")

    def __str__(self):
        return '%s - %s - %s' % (self.type, self.premium, self.cover)
