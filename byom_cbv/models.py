from django.db import models
from django.urls import reverse


class Crop(models.Model):
    CROP_NAME = models.CharField(max_length=200)
    AVG_SOIL_PH = models.FloatField()
    AVG_GROW_TEMP = models.FloatField()
    AVG_PRECIP = models.FloatField()

class Biome(models.Model):
    BIOME_NAME = models.CharField(max_length=200)
    SOIL_PH_MIN = models.FloatField()
    SOIL_PH_MAX = models.FloatField()   
    TEMP_MIN = models.FloatField()
    TEMP_MAX = models.FloatField()
    PRECIP_MIN = models.FloatField()
    PRECIP_MAX = models.FloatField()
    CROP = models.ManyToManyField(Crop)




class User(models.Model):
    NAME = models.CharField(max_length=200)
    #PASSWORD = models.CharField(max_length=300)
    # No authentication should be used for now - we shouldn't "roll our own" solution.


    # fixed indentation issue
class Bookmark(models.Model):
    BOOKMARK_DATE = models.DateField()
    crop = models.ForeignKey(Crop, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.BIOME_NAME

    def get_absolute_url(self):
        return reverse('byom_cbv:biome_edit', kwargs={'pk': self.pk})