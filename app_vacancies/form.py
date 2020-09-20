from django import forms

from app_vacancies.models import Application


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
