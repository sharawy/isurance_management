from django.contrib import admin

from policies.models import Policy


@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    pass
