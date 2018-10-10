from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class WikiArticle(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    wiki_id = models.IntegerField(unique=True)
    page = models.CharField(unique=True, max_length=255)
    title = models.CharField(unique=True, max_length=255)
    bag_size = models.IntegerField()
    bag = JSONField()
    header_bag_size = models.IntegerField()
    header_bag = JSONField()

    @property
    def link(self):
        return "https://en.wikipedia.org/wiki/{name}/".format(name=self.page)

    @property
    def sorted_bag(self):
        return {key: value for key, value in sorted(self.bag.items(), key=lambda x: -x[1])}

    @property
    def sorted_header_bag(self):
        return {key: value for key, value in sorted(self.header_bag.items(), key=lambda x: -x[1])}
