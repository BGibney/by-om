from django.db import models

class Plants(models.Model):
    description = models.CharField(max_length=200)
    environment = models.ManyToMany(Environment, on_delete=models.CASCADE)
    plantType   = models.
    
    
class Environment(models.Model):
    description = models.CharField(max_length=200)
    # unnecessary per official documentation; only needed in one model
    # plant = models.ManyToManyField(Plants, on_delete=models.CASCADE)
    environmentType = 
    temperate
    temp_start
    temp_end