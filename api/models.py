import uuid
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.PositiveIntegerField()
    course = models.ManyToManyField(
        'Course', through='StudentCourseMapping',
        blank=True,
        through_fields=(
            'student', 'course'),
    )


class Course(models.Model):
    name = models.CharField(max_length=30)
    credits = models.BigIntegerField()


def validate_score(value):
    if value > 100:
        raise ValidationError("value can only below 100")


class StudentCourseMapping(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(validators=[validate_score])
