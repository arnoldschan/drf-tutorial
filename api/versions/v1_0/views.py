from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from api.models import Course, Student, StudentCourseMapping
from rest_framework.pagination import PageNumberPagination
from django.db.models import F, Count

from api.versions.mixins import MultiSerializerViewSetMixin
from .serializers import CourseSerializer, StudentCourseMappingRetrieveSerializer, StudentCourseMappingSerializer, StudentListSerializer, StudentSerializer, StudentSummarySerializer
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import CharFilter, FilterSet
from rest_framework import filters


from django.db import connection


class HelloViewSet(ViewSet):
    def list(self, request):
        version = request.version
        return Response(f"HELLO from version {version} !")


class CustomPagination(PageNumberPagination):
    page_query_param = 'p'
    page_size_query_param = "number"
    page_size = 2


class StudentFilter(FilterSet):
    first_name__in = CharFilter(
        field_name='first_name', lookup_expr='icontains')
    have_course = CharFilter(
        field_name='course__name', lookup_expr='icontains')

    class Meta:
        model = Student
        fields = "__all__"


class StudentViewSet(MultiSerializerViewSetMixin, ModelViewSet, ):
    serializer_class = StudentSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = StudentFilter
    search_fields = ['first_name', 'last_name']

    queryset = Student.objects.all()
    serializer_action_classes = {
        'list': StudentListSerializer,
    }

    @action(methods=['get'], detail=True)
    def course_summary(self, request, pk=None):
        return Response(self.get_object().course.count())

    def list(self, request, *args, **kwargs):
        result = super().list(request, *args, **kwargs)
        print(connection.queries)
        return result


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    @action(methods=['get'], detail=False)
    def student_summary(self, request):
        result = Course.objects.all().annotate(
            course=F('name'),
            student_count=Count(F('student')))
        data = StudentSummarySerializer(result, many=True).data
        print(connection.queries)
        return Response(data)


class StudentCourseMappingFilter(FilterSet):
    class Meta:
        model = StudentCourseMapping
        fields = {
            'score': ['lte', 'gte'],
            'course__credits': ['lte', 'gte'],
            'course__name': ['icontains', 'istartswith'],
        }


class StudentCourseMappingViewSet(MultiSerializerViewSetMixin, ModelViewSet):
    serializer_class = StudentCourseMappingSerializer
    queryset = StudentCourseMapping.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = StudentCourseMappingFilter
    ordering_fields = "__all__"
    serializer_action_classes = {
        'retrieve': StudentCourseMappingRetrieveSerializer,
    }
