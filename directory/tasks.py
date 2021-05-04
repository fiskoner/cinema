import requests

from cinema import celery_app
from directory.models import Country


@celery_app.task()
def get_countries():
    url = 'https://namaztimes.kz/ru/api/country?type=json'
    response = requests.get(url=url)
    response_json = response.json()
    for country in response_json.values():
        Country.objects.update_or_create(name=country)