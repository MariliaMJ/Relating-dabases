from django.conf.urls import url
from rest_framework import routers
from core.views import PersonViewSet

router = routers.DefaultRouter()
router.register(r'owner_name', PersonViewSet)

urlpatterns = router.urls