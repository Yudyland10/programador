from django.db import models

class Instructor(models.Model):
	cc = models.IntegerField()
	name = models.CharField(max_length=30)
	email =models.EmailField()
	telefono=models.IntegerField()
	profesión=models.CharField(max_length=15)
	areaOrientar=models.CharField(max_length=30)
	rol=models.CharField(max_length=10)


	def __str__(self):
	    return self.name