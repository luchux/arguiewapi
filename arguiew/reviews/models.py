from django.db import models

# Create your models here.

### Review #######
### Represents the Review that contains the opinion, features, etc. 
### TODO: all :) 

class Review(models.Model):
	text = models.CharField(blank=True,max_length=200)

### End Review ###

