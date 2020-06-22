from django.urls import include, path
from rest_framework import routers

from .viewsets import PolicyViewSet

router = routers.DefaultRouter()
router.register(r'policies', PolicyViewSet)

urlpatterns = [
    path('v1/', include((router.urls, __package__), namespace='v1')),
]
