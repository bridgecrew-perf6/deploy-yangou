from django.db import models

class Character(models.Model):   
  name = models.CharField(max_length=100)
  age = models.IntegerField()
  description = models.CharField(max_length=300, null=True)
  image = models.ImageField(upload_to='website/characters/', null=True)
