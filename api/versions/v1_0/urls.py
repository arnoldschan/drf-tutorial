from api.versions.v1_0.views import CourseViewSet, HelloViewSet, StudentCourseMappingViewSet, StudentViewSet
from rest_framework.routers import DefaultRouter

app_name = "api"

router = DefaultRouter()
router.register(r'hello', HelloViewSet, basename='hello')
router.register(r'student', StudentViewSet, basename='student')
router.register(r'course', CourseViewSet, basename='course')
router.register(r'studentcourse', StudentCourseMappingViewSet,
                basename='studentcourse')

urlpatterns = []
urlpatterns += router.urls
