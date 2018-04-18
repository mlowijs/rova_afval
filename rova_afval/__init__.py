import requests
from datetime import date

ROVA_API_URL = 'http://rova.quintor.nl/rest/afvalkalender/{0}/{1}/{2}/{3}?toevoeging={4}'

def get_inzamelingen(year, postcode, house_number, suffix = None):
    postcode = str(postcode).strip()
    postcode_letters = postcode[0:4]
    postcode_numbers = postcode[4:].strip()

    year = str(year).strip()
    house_number = str(house_number).strip()

    if suffix == None:
        suffix = ""
    
    suffix = str(suffix).strip()

    request_url = ROVA_API_URL.format(year, postcode_letters, postcode_numbers, house_number, suffix)
    response = requests.get(request_url).json()

    if 'result' in response and response['result'] == 'failed':
        return { 'error': True, 'message': response['description'] }

    return { 'error': False, 'data': response['afvalkalender']['inzameldagen'] }
