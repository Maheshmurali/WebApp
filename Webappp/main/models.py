from django.db import models

class Generaldata(models.Model):
    heart_Likes = models.IntegerField(null=True)
    heart_Dislikes = models.IntegerField(null=True)
    comments = models.CharField(max_length=1000)
