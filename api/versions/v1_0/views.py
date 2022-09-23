from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from api.models import Course, Student, StudentCourseMapping
from rest_framework.pagination import PageNumberPagination
from django.db.models import F, Count

from api.versions.mixins import MultiSerializerViewSetMixin
from .serializers import CourseSerializer, StudentCourseMappingSerializer, StudentListSerializer, StudentSerializer, StudentSummarySerializer
from rest_framework.decorators import action


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

    @action(methods=['get'], detail=True)
    def course_summary(self, request, pk=None):
        return Response(self.get_object().course.count())


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    @action(methods=['get'], detail=False)
    def student_summary(self, request):
        result = Course.objects.all().annotate(
            course=F('name'),
            student_count=Count(F('student')))
        data = StudentSummarySerializer(result, many=True).data
        return Response(data)


class StudentCourseMappingViewSet(ModelViewSet):
    serializer_class = StudentCourseMappingSerializer
    queryset = StudentCourseMapping.objects.all()
