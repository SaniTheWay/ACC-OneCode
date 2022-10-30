from django.db import models


class Prob_type(models.Model):
    name=models.TextField(max_length=200)
    def __str__(self):
        return u'%s' % (self.name)

class Problem(models.Model):
    LEVEL_CHOICES = (
        ('easy','EASY'),
        ('medium', 'MEDIUM'),
        ('hard','HARD'),
    )
    p_meta = models.ForeignKey(Prob_type, on_delete=models.CASCADE)
    p_title = models.TextField(max_length = 255)
    p_level = models.CharField(max_length=6, choices=LEVEL_CHOICES, default="easy")
    p_link = models.URLField(max_length=255)

    def __str__(self):
        return u'%s' % (self.p_title)