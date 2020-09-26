from django import forms
from django.contrib.auth.models import User

from app_vacancies.models import Application, Company, Specialty, Vacancy


class ApplicationForm(forms.ModelForm):
    written_username = forms.CharField(max_length=64, label='Вас зовут')
    written_phone = forms.CharField(max_length=12, label='Ваш телефон')
    written_cover_letter = forms.CharField(
        widget=forms.Textarea,
        label='Сопроводительное письмо')

    class Meta:
        model = Application
        fields = ['written_username',
                  'written_phone',
                  'written_cover_letter']


class CompanyForm(forms.ModelForm):
    name = forms.CharField(
        max_length=64,
        label='Название компании',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'type': 'text',
                   'id': 'companyName'})
    )
    location = forms.CharField(
        max_length=64,
        label='География',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'type': 'text',
                   'id': 'companyLocation'})
    )
    description = forms.CharField(
        label='Информация о компании',
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                   'rows': 4,
                   'id': 'companyInfo',
                   'style': "color:#000;"})
    )
    employee_count = forms.IntegerField(
        label='Количество человек в компании',
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'type': 'text',
                   'id': 'companyTeam'})
    )

    class Meta:
        model = Company
        fields = ['name', 'location', 'logo',
                  'description', 'employee_count']


class MyVacancyEditForm(forms.ModelForm):

    title = forms.CharField(
        max_length=64,
        label='Название вакансии',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'vacancyTitle',
                'type': 'text',
            }
        )
    )
    specialty = forms.ChoiceField(
        label='Специализация',
        widget=forms.Select(
            attrs={
                'class': 'custom-select mr-sm-2',
                'id': 'userSpecialization'
            }
        ),
        choices=((str(Specialty), str(Specialty)) for Specialty in Specialty.objects.all())
    )

    salary_min = forms.IntegerField(
        label='Зарплата от',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'vacancySalaryMin',
                }
        )
    )

    salary_max = forms.IntegerField(
        label='Зарплата до',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'vacancySalaryMax',
                }
        )
    )

    skills = forms.CharField(
        max_length=200,
        label='Требуемые навыки',
        widget=forms.Textarea(
            attrs={
                'rows': '3',
                'class': 'form-control',
                'id': 'vacancySkills',
                'style': "color:#000;"
            }
        )
    )

    description = forms.CharField(
        max_length=200,
        label='Описание',
        widget=forms.Textarea(
            attrs={
                'rows': '13',
                'class': 'form-control',
                'id': 'vacancyDescription',
                'style': "color:#000;"
            }
        )
    )

    class Meta:
        model = Vacancy
        fields = ('title', 'salary_min', 'salary_max', 'skills', 'description', )


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(
        label='Логин',
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'form-control',
                'id': 'inputLogin'}
        )
    )
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'form-control',
                'id': 'inputName'}
        )
    )
    last_name = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(
            attrs={
                'autofocus': True,
                'class': 'form-control',
                'id': 'inputSurname'}
        )
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                'autofocus': True,
                'class': 'form-control',
                'id': 'inputPassword'}
        )
    )

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name',)
