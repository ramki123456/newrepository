from __future__ import unicode_literals

from django.db import models

# Create your models here.
#creting table with the name:person
class Person(models.Model):
	name=models.CharField(max_length=20)
	age=models.IntegerField()
	mail_id=models.CharField(max_length=40,unique=True)
	phone=models.CharField(max_length=40)

	def __unicode__(self):
		return self.name