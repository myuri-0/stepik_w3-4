from django.contrib.auth.models import User
from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=64)
    logo = models.ImageField(upload_to="MEDIA_COMPANY_IMAGE_DIR")
    description = models.TextField()
    employee_count = models.IntegerField(null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Specialty(models.Model):
    code = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    picture = models.ImageField(upload_to="MEDIA_SPECIALITY_IMAGE_DIR")


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=120)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()


class Application(models.Model):
    written_username = models.CharField(max_length=24)
    written_phone = models.CharField(max_length=12)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
