from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView

from app_vacancies.form import ApplicationForm, CompanyForm
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

    def get(self, request, vacancy_id):
        get_object_or_404(Vacancy.objects.filter(id=vacancy_id))
        vacancies = Vacancy.objects.filter(id=vacancy_id)
        id_vacancy = vacancy_id
        return render(request, 'vacancy.html', {"heading": 'Вакансия | Джуманджи',
                                                "vacancies": vacancies,
                                                "vacancy_form": ApplicationForm,
                                                'vacancy_id': id_vacancy
                                                })

    def post(self, request, vacancy_id):
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.vacancy = Vacancy.objects.get(id=vacancy_id)
            form.user = request.user if request.user.is_authenticated else None
            form.save()
            return redirect(f'/vacancies/{vacancy_id}/sent/')

        return render(
            request, 'vacancy.html',
            context={
                "vacancy_form": ApplicationForm,
            }
        )


class SentView(View):

    def get(self, request, vacancy_id):
        get_object_or_404(Vacancy.objects.filter(id=vacancy_id))
        vacancy = Vacancy.objects.get(id=vacancy_id)
        return render(
            request, 'sent.html', context={
                'vacancy': vacancy,
                "heading": "Отклик отправлен",
            }
        )


class MyVacancyView(View):

    def get(self, request):
        return render(request, "vacancy-list.html.html")


class MyCompanyView(View):

    def get(self, request):
        try:
            company = Company.objects.get(owner=request.user)
            form = CompanyForm(instance=company)
            return render(
                request, 'company_edit.html', context={
                    'company': company,
                    'form': form
                }
            )
        except Company.DoesNotExist:
            return render(request, 'not_company.html')

    def post(self, request):
        current_user = request.user
        company = Company.objects.get(owner=current_user)

        form = CompanyForm(request.POST, instance=company)

        if form.is_valid():
            form = form.save(commit=False)
            form.owner = current_user
            form.save()
            return redirect('/mycompany/')
        else:
            form = CompanyForm(instance=company)

        return render(
            request, 'company_edit.html',
            context={
                'form': form,
                'company': company
            })


class MyCompanyCreateView(View):
    def get(self, request):

        form = CompanyForm()
        return render(
            request, 'company_create.html', context={
                'form': form
            }
        )

    def post(self, request):
        if request.method == "POST":
            form = CompanyForm(request.POST)
            print(form.is_valid(), form.errors)
            if form.is_valid():
                form = form.save(commit=False)
                form.owner = request.user
                form.logo = 'https://place-hold.it/130x80'
                form.save()
                return redirect('/mycompany/', pk=form.pk)
        else:
            form = CompanyForm()
        return render(request, 'company_create.html', {'form': form})


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = 'login/'
    template_name = 'register.html'


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'


def custom_handler404(request, exception):
    return HttpResponseNotFound('Page not found 404! Такой страницы не существует!')


def custom_handler500(request):
    return HttpResponseServerError('Internal Server Error 500! Внутренняя ошибка сервера!')
