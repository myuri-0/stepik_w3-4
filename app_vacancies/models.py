from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=64)
    logo = models.CharField(max_length=130)
    description = models.TextField()
    employee_count = models.IntegerField(null=True)


class Specialty(models.Model):
    code = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    picture = models.CharField(max_length=130)


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=120)
    description = models.TextField()
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()
