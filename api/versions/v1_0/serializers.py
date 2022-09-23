from rest_framework import serializers

from api.models import Course, Student, StudentCourseMapping


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ["course", "age"]


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class StudentCourseMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourseMapping
        fields = "__all__"
