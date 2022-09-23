from api.versions.v1_0.views import HelloViewSet
from rest_framework.routers import DefaultRouter

app_name = "api"

router = DefaultRouter()
router.register(r'hello', HelloViewSet, basename='hello')

urlpatterns = []
urlpatterns += router.urls
