from geoip.models import IPInfo
import requests, os

"""
API LIMITS:
10k requests/month (https://ipstack.com/plan)

Notes:
API returns all fields as null w/ invalid IPs
"""

API_KEY = os.getenv('IP_API_KEY')
ENDPOINT = 'http://api.ipstack.com/{ip}?access_key={api_key}'.format(ip='{ip}', api_key=API_KEY)

def standard_lookup(ip):
    "Query an IP."
    response = requests.get(ENDPOINT.format(ip=ip))
    if response.ok:
        data = response.json()
        if data.get('success', True):
            return {
                'success': True,
                'IP': ip,
                'continent': data['continent_code'],
                'country': data['country_code'],
                'region_code': data['region_code'],
                'region_name': data['region_name'],
                'city': data['city'],
                'zip': data['zip'],
                'latitude': data['latitude'],
                'longitude': data['longitude'],
                'language': (data['location']['languages'][0]['code'] if data['location']['languages'] else None) if data.get('location') else None
            }
    
    return {
        'success': False,
        'IP': ip
    }
        

def get_or_create_ip(addr):
    try:
        ip = IPInfo.objects.get(IP=addr)
    except IPInfo.DoesNotExist:
        data = standard_lookup(addr)
        if data['success']:
            del data['success']
            ip = IPInfo(**data)
            ip.save()
        else:
            raise ValueError("Invalid IP")

    return ip
