from django.contrib import admin
from django.urls import path

from app_vacancies.views import MainView, VacanciesView, CategoryView, CompanyView, VacancyView, custom_handler404, \
    custom_handler500

urlpatterns = [
    path('', MainView.as_view()),
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('vacancies/cat/<str:categories>/', CategoryView.as_view()),
    path('companies/<int:company>/', CompanyView.as_view(), name='companies'),
    path('vacancies/<int:vacancy>/', VacancyView.as_view()),
    path('admin/', admin.site.urls),
]

handler404 = custom_handler404
handler500 = custom_handler500
