from django_seed import Seed
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from api.models import Student, Course, StudentCourseMapping  # noqa
seeder = Seed.seeder()

seeder.add_entity(Student, 200)
seeder.add_entity(Course, 30)
seeder.add_entity(StudentCourseMapping, 600)
seeder.execute()
