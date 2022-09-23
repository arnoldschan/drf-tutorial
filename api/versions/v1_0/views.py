from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from api.models import Student

from .serializers import StudentSerializer


class HelloViewSet(ViewSet):
    def list(self, request):
        version = request.version
        return Response(f"HELLO from version {version} !")


class StudentViewSet(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
