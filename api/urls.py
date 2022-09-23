from django.urls import path, include

app_name = "api"
urlpatterns = [
    path('v1.0/', include('api.versions.v1_0.urls', namespace='v1.0')),
]
