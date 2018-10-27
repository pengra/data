from django.db import models

# Create your models here.

class State(models.Model):
    code = models.CharField(max_length=255, unique=True)
    block_gis = models.FileField(upload_to="state_gis/blocks", null=True, blank=True)
    block_count = models.IntegerField(null=True, blank=True)
    county_gis = models.FileField(upload_to="state_gis/counties/", null=True, blank=True)
    county_count = models.IntegerField(null=True, blank=True)
    precinct_gis = models.FileField(upload_to="state_gis/precincts/", null=True, blank=True)
    precinct_count = models.IntegerField(null=True, blank=True)

    @property
    def block_size(self):
        return self.block_gis.size()
    
    @property
    def county_size(self):
        return self.county_gis.size()
    
    @property
    def precinct_size(self):
        return self.precinct_gis.size()
