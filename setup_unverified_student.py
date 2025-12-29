import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth import get_user_model
from apps.accounts.models import Profile

User = get_user_model()

def create_unverified_student():
    student, created = User.objects.get_or_create(username="student2", email="student2@example.com")
    if created:
        student.set_password("student123")
        student.save()
        print("Student 'student2' created.")
    
    Profile.objects.get_or_create(user=student, defaults={"role": "student", "is_verified_student": False})
    print("Unverified student 'student2' ready.")

if __name__ == "__main__":
    create_unverified_student()
