from django.db.models import Sum

from django.db import models

# Create your models here.

STOP_WORD_DENSITY_THRESHOLD = 0.0003
STOP_WORD_ARTICLE_DENSITY_THRESHOLD = 0.85


class Webpage(models.Model):
    url = models.URLField(help_text="URL with word", unique=True)

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        self.url = self.url.replace("http://", "https://")
        self.url = self.url.split('#')[0].split('?')[0]
        return super().save(*args, **kwargs)


class Word(models.Model):
    word = models.CharField(max_length=255, unique=True)
    count = models.IntegerField(help_text="Number of times word appears cumulatively")
    isAlnum = models.BooleanField()
    
    def save(self, *args, **kwargs):
        self.isAlnum = self.word.isalnum()
        return super().save(*args, **kwargs)

    @property
    def wordDensity(self):
        return self.count / Word.objects.filter(
            isAlnum=True
        ).aggregate(
            count=(Sum('count'))
        )['count']

    @property
    def articleDensity(self):
        return WordIndex.objects.filter(word=self).count() / Webpage.objects.all().count()

    @property
    def isStopWord(self):
        return self.wordDensity > STOP_WORD_DENSITY_THRESHOLD or self.articleDensity > STOP_WORD_ARTICLE_DENSITY_THRESHOLD


class WordIndex(models.Model):
    class Meta:
        unique_together = (('word', 'url'),)
        ordering = ('-count',)

    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    url = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    count = models.IntegerField(help_text="Number of times word appears on this page")

    updated_at = models.DateTimeField(auto_now=True)
