from django import forms
from .movie_choices import get_choices


class MovieForm(forms.Form):
    title = forms.CharField(label='Название', max_length=100)
    country = forms.CharField(label='Страна', max_length=100)
    year = forms.IntegerField(label='Год')


class FilterForm(forms.Form):
    def __init__(self):
        super().__init__()
        self.countries, self.years = get_choices()
        self.fields['country_data'] = forms.ChoiceField(label='Страна', choices=self.countries, required=False)
        self.fields['tipe_c_filter'] = forms.BooleanField(label='Исключая', required=False)
        self.fields['year_data'] = forms.ChoiceField(label='Год', choices=self.years, required=False)
        self.fields['tipe_y_filter'] = forms.BooleanField(label='Исключая', required=False)






