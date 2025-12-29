import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth import get_user_model
from apps.accounts.models import Profile, SiteSetting
from apps.courses.models import Course
from apps.assignments.models import Assignment

User = get_user_model()

def create_test_data():
    print("Creating test data...")

    # Create Superuser
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "admin123")
        print("Superuser 'admin' created.")

    # Create Teacher
    teacher, created = User.objects.get_or_create(username="teacher1", email="teacher1@example.com")
    if created:
        teacher.set_password("teacher123")
        teacher.save()
        print("Teacher 'teacher1' created.")
    
    Profile.objects.get_or_create(user=teacher, defaults={"role": "teacher"})

    # Create Student
    student, created = User.objects.get_or_create(username="student1", email="student1@example.com")
    if created:
        student.set_password("student123")
        student.save()
        print("Student 'student1' created.")
    
    Profile.objects.get_or_create(user=student, defaults={"role": "student", "is_verified_student": True})

    # Create Course
    course, created = Course.objects.get_or_create(name="Introduction to Python", description="Learn Python basics.")
    if created:
        print(f"Course '{course.name}' created.")

    # Create Assignment
    assignment, created = Assignment.objects.get_or_create(
        course=course,
        title="First Assignment",
        defaults={
            "description": "Write a Hello World program.",
            "due_date": "2025-12-31 23:59:59"
        }
    )
    if created:
        print(f"Assignment '{assignment.title}' created.")

    print("Test data creation complete.")

if __name__ == "__main__":
    create_test_data()
