from django import forms
import datetime
from django.core.exceptions import ValidationError


class RenewBookForm(forms.Form):
    """ Renovar Libros"""
    renew_date = forms.DateField(help_text="Enter a date now and 4 weeks")

    def clean_renew_date(self):
        data = self.cleaned_data['renew_date']

        if data < datetime.date.today():
            raise ValidationError('Fecha fuera de rango, ingrese una fecha mayor')
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError('Fecha fuera de rango, ingrese una fecha menor')

        return data