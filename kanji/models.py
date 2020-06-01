from django.db import models

# Create your models here.


class grammarParticle(models.Model):
    hiragana = models.CharField(max_length=200)
    story = models.TextField(default="")
    example_words = models.TextField(default="")
    translation = models.TextField(default="")
    radical = models.CharField(max_length=50, default="")
    def __str__(self):
        return self.hiragana

class radicals(models.Model):
    radical = models.CharField(max_length=20, default ="")
    radical_name = models.CharField(max_length=25, default="")
    description = models.TextField()

    def __str__(self):
        return self.radical
