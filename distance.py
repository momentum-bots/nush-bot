import requests
from config import TOM_TOM_API_KEY


def get_closest_school(lat, lon):
    """
    :param lat: latitude
    :param lon: longitude
    :return: [5] results ['poi']['name']/['freeformAddress'] || ['position']['lat']/['lon']
    """
    results = []
    r = requests.get('https://api.tomtom.com/search/2/poiSearch/school'
                     '.json?key={0}&lat={1}&lon={2}&radius=10000&limit=100'.format(
                        TOM_TOM_API_KEY,
                        lat,
                        lon
    ))
    for result in r.json()['results']:
        if result['poi']['categories'] == ['school'] and \
                'садок' not in result['poi']['name'] and \
                '1S' not in result['poi']['name'] and \
                'Khammer' not in result['poi']['name']:
            results.append(result)
        if len(results) == 5:
            break
    return results


if __name__ == '__main__':
    get_closest_school(50.4654669, 30.3745462)
