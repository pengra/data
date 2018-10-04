from django.db.models import Sum

from django.db import models

# Create your models here.

class WordIndex(models.Model):
    class Meta:
        unique_togeter = (('word', 'url'),)

    word = models.CharField(max_length=255, help_text="Word on page")
    isAlnum = models.BooleanField()
    url = models.URLField(help_text="URL with word")
    count = models.IntegerField(help_text="Number of times word appears on page")

    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.url = self.url.replace("http://", "https://")
        self.url = self.url.split('#')[0].split('?')[0]
        self.isAlnum = self.word.isalnum()
        return super().save(*args, **kwargs)

    @property
    def wordPercentage(self):
        return WordIndex.objects.filter(
            isAlnum=True
        ).aggregate(
            count=(Sum('count'))
        )['count']

    @property
    def articleApperancePercentage(self):
        return WordIndex.objects.filter(
            word=self.word
        ).count()

    @property
    def isStopWord(self):
        return (
            self.wordPercentage >= 0.0003 and self.articleApperancePercentage >= 0.85
        )