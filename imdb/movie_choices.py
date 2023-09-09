from .models import MoviesDB


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
