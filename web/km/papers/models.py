from django.db import models
from django.utils import timezone

class Paper(models.Model):
	index = models.CharField(max_length=10,default="", blank=True, null=True)
	authors = models.CharField(max_length=500,default="", blank=True, null=True)
	title = models.CharField(max_length=500)
	source = models.CharField(max_length=100,default="", blank=True, null=True)
	keywords = models.CharField(max_length=1000,default="", blank=True, null=True)
	abstract = models.CharField(max_length=10000,default="", blank=True, null=True)
	reference = models.CharField(max_length=100000,default="", blank=True, null=True)
	cite = models.CharField(max_length=10,default="", blank=True, null=True)
	year = models.CharField(max_length=10,default="", blank=True, null=True)
	doi = models.CharField(max_length=100,default="", blank=True, null=True)
	sim = models.CharField(max_length=500,default="", blank=True, null=True)
	refs = models.CharField(max_length=2000,default="", blank=True, null=True)
	cites = models.CharField(max_length=10000,default="", blank=True, null=True)
	


