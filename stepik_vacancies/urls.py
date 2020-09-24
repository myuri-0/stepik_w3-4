from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from app_vacancies.views import MainView, VacanciesView, CategoryView, CompanyView, VacancyView, custom_handler404, \
    custom_handler500, MySignupView, MyLoginView, SentView, MyCompanyView, MyVacancyView, MyCompanyCreateView

urlpatterns = [
    path('', MainView.as_view()),
    path('vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('vacancies/cat/<str:categories>/', CategoryView.as_view()),
    path('companies/<int:company_id>/', CompanyView.as_view(), name='companies'),
    path('vacancies/<int:vacancy_id>/', VacancyView.as_view(), name='vacancy'),
    path('vacancies/<int:vacancy_id>/sent/', SentView.as_view()),
    path('admin/', admin.site.urls),
    path('mycompany/', MyCompanyView.as_view(), name='company'),
    path('mycompany/vacancies/', MyVacancyView.as_view(), name='myvacancy'),
    path('mycompany/create/', MyCompanyCreateView.as_view()),
]

handler404 = custom_handler404
handler500 = custom_handler500

urlpatterns += [
    path('register/', MySignupView.as_view(), name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
