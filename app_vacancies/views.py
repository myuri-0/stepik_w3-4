from django.http import HttpResponseNotFound, HttpResponseServerError, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View

from app_vacancies.models import Specialty, Company, Vacancy


class MainView(View):

    def get(self, request):
        specialties = Specialty.objects.all()
        company = Company.objects.all()
        return render(request, 'index.html', {"heading": 'Джуманджи',
                                              "specialties": specialties,
                                              "company": company,
                                              })


class VacanciesView(View):

    def get(self, request):
        vacancies = Vacancy.objects.all()
        total = Vacancy.objects.order_by("title").count()
        return render(request, "vacancies.html", {"title": 'Все вакансии',
                                                  "heading": 'Вакансии | Джуманджи',
                                                  "vacancies": vacancies,
                                                  "total": total,
                                                  })


class CategoryView(View):

    def get(self, request, categories):
        get_object_or_404(Specialty.objects.filter(code=categories))
        speciality = Specialty.objects.get(code=categories)
        vacancies = Vacancy.objects.filter(specialty=speciality)
        return render(request, 'vacancies.html', {"title": categories,
                                                  "heading": 'Вакансии | Джуманджи',
                                                  "vacancies": vacancies,
                                                  })


class CompanyView(View):

    def get(self, request, company_id):
        get_object_or_404(Company.objects.filter(id=company_id))
        firms = Company.objects.filter(id=company_id)
        company_filter = Company.objects.get(id=company_id)
        vacancies = Vacancy.objects.filter(company=company_filter)
        return render(request, 'company.html', {"heading": 'Компания | Джуманджи',
                                                "vacancies": vacancies,
                                                "firms": firms,
                                                })


class VacancyView(View):

    def get(self, request, vacancy):
        get_object_or_404(Vacancy.objects.filter(id=vacancy))
        vacancies = Vacancy.objects.filter(id=vacancy)
        return render(request, 'vacancy.html', {"heading": 'Вакансия | Джуманджи',
                                                "vacancies": vacancies,
                                                })


def custom_handler404(request, exception):
    return HttpResponseNotFound('Page not found 404! Такой страницы не существует!')


def custom_handler500(request):
    return HttpResponseServerError('Internal Server Error 500! Внутренняя ошибка сервера!')
