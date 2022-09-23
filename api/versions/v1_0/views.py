from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from api.models import Course, Student, StudentCourseMapping

from .serializers import CourseSerializer, StudentCourseMappingSerializer, StudentSerializer


class HelloViewSet(ViewSet):
    def list(self, request):
        version = request.version
        return Response(f"HELLO from version {version} !")


class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class StudentCourseMappingViewSet(ModelViewSet):
    serializer_class = StudentCourseMappingSerializer
    queryset = StudentCourseMapping.objects.all()
