from rest_framework.viewsets import ViewSet
from rest_framework.response import Response


class HelloViewSet(ViewSet):
    def list(self, request):
        version = request.version
        return Response(f"HELLO from version {version} !")
