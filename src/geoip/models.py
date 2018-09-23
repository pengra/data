from django.db import models
from django.template.defaultfilters import slugify

class IPInfo(models.Model):
    IP = models.GenericIPAddressField(unique=True)
    continent = models.CharField(max_length=2, null=True, choices=(
        ('AF', 'Africa'),
        ('AS', 'Asia'),
        ('EU', 'Europe'),
        ('NA', 'North America'),
        ('OC', 'Oceania'),
        ('SA', 'South America'),
        ('AN', 'Antartica')
    ))
    country = models.CharField(max_length=2, blank=True, null=True)
    region_code = models.CharField(max_length=5, blank=True, null=True)
    region_name = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(blank=True, null=True, max_length=50)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    language = models.CharField(max_length=2, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.IP