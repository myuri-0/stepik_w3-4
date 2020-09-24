from django import forms

from app_vacancies.models import Application, Company


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
