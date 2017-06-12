from django.conf.urls import url
from rest_framework import routers
from friends.views import PersonViewSet

router = routers.DefaultRouter()
router.register(r'owner_name', PersonViewSet)

urlpatterns = router.urls