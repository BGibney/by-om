from django.db import models
from django.urls import reverse


class Biome(models.Model):
    BIOME_NAME = models.CharField(max_length=200)
    SOIL_PH_MIN = models.FloatField()
    SOIL_PH_MAX = models.FloatField()	

    def __str__(self):
        return self.BIOME_NAME

    def get_absolute_url(self):
        return reverse('byom_cbv:biome_edit', kwargs={'pk': self.pk})