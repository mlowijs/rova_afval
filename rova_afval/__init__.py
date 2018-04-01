import requests
from datetime import date

ROVA_API_URL = 'http://rova.quintor.nl/rest/afvalkalender/{0}/{1}/{2}/{3}?toevoeging={4}'

def get_inzamelingen(postcode, house_number, suffix = ""):
    postcode = postcode.strip()

    postcode_letters = postcode[0:4]
    postcode_numbers = postcode[4:].strip()
    house_number = house_number.strip()
    suffix = suffix.strip()

    request_url = ROVA_API_URL.format(date.today().year, postcode_letters, postcode_numbers, house_number, suffix)
    response = requests.get(request_url).json()

    if 'result' in response and response['result'] == 'failed':
        return False

    return response['afvalkalender']['inzameldagen']
