from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from api.models import Course, Student, StudentCourseMapping
from rest_framework.pagination import PageNumberPagination

from api.versions.mixins import MultiSerializerViewSetMixin
from .serializers import CourseSerializer, StudentCourseMappingSerializer, StudentListSerializer, StudentSerializer


class HelloViewSet(ViewSet):
    def list(self, request):
        version = request.version
        return Response(f"HELLO from version {version} !")


class CustomPagination(PageNumberPagination):
    page_query_param = 'p'
    page_size_query_param = "number"
    page_size = 2


class StudentViewSet(MultiSerializerViewSetMixin, ModelViewSet, ):
    serializer_class = StudentSerializer
    pagination_class = CustomPagination
    queryset = Student.objects.all()
    serializer_action_classes = {
        'list': StudentListSerializer,
    }


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class StudentCourseMappingViewSet(ModelViewSet):
    serializer_class = StudentCourseMappingSerializer
    queryset = StudentCourseMapping.objects.all()
