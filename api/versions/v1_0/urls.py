from api.versions.v1_0.views import HelloViewSet, StudentViewSet
from rest_framework.routers import DefaultRouter

app_name = "api"

router = DefaultRouter()
router.register(r'hello', HelloViewSet, basename='hello')
router.register(r'student', StudentViewSet, basename='student')

urlpatterns = []
urlpatterns += router.urls
