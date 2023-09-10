from django import forms
from .models import MoviesDB

# функция получения списков стран и годов из базы для фильтров
def get_choices():
    countries = ['']
    years = []

    for i in MoviesDB.objects.values('country').distinct():
        countries.extend(list(i.values()))
    countries.sort()
    countries = tuple(zip(countries, countries))

    for i in MoviesDB.objects.values('year').distinct():
        years.extend(list(i.values()))
    years.sort()
    years.insert(0, '')
    years = tuple(zip(years, years))

    return countries, years

# форма добавления фильма вручную
class MovieForm(forms.Form):
    title = forms.CharField(label='Название', max_length=100)
    country = forms.CharField(label='Страна', max_length=100)
    year = forms.IntegerField(label='Год')

# форма фильтра, переинициализируется при обновлении страницы, чтобы обновлять списки выбора в фильтрах
class FilterForm(forms.Form):
    def __init__(self):
        super().__init__()
        self.countries, self.years = get_choices()
        self.fields['country_data'] = forms.ChoiceField(label='Страна', choices=self.countries, required=False)
        self.fields['tipe_c_filter'] = forms.BooleanField(label='Исключая', required=False)
        self.fields['year_data'] = forms.ChoiceField(label='Год', choices=self.years, required=False)
        self.fields['tipe_y_filter'] = forms.BooleanField(label='Исключая', required=False)






