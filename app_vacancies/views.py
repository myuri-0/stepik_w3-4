from django.http import HttpResponseNotFound, HttpResponseServerError, Http404
from django.shortcuts import render
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
        if len(Specialty.objects.filter(code=categories)) == 0:
            raise Http404
        category = Specialty.objects.get(code=categories)
        vacancies = Vacancy.objects.filter(specialty=category)
        total = Vacancy.objects.filter(specialty=category).count()
        return render(request, 'vacancies.html', {"title": categories,
                                                  "heading": 'Вакансии | Джуманджи',
                                                  "vacancies": vacancies,
                                                  "total": total,
                                                  })


class CompanyView(View):

    def get(self, request, company):
        if len(Specialty.objects.filter(id=company)) == 0:
            raise Http404
        firms = Company.objects.filter(id=company)
        company_filter = Company.objects.get(id=company)
        vacancies = Vacancy.objects.filter(company=company_filter)
        return render(request, 'company.html', {"heading": 'Компания | Джуманджи',
                                                "vacancies": vacancies,
                                                "firms": firms,
                                                })


class VacancyView(View):

    def get(self, request, vacancy):
        if len(Vacancy.objects.filter(id=vacancy)) == 0:
            raise Http404
        vacancies = Vacancy.objects.filter(id=vacancy)
        return render(request, 'vacancy.html', {"heading": 'Вакансия | Джуманджи',
                                                "vacancies": vacancies,
                                                })


def custom_handler404(request, exception):
    return HttpResponseNotFound('Page not found 404! Такой страницы не существует!')


def custom_handler500(request):
    return HttpResponseServerError('Internal Server Error 500! Внутренняя ошибка сервера!')
