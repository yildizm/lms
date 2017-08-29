from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User, Group
# Create your models here.
		
class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	available = models.BooleanField(default=True)
	isbn = models.IntegerField()

class Record(models.Model):
	patron = models.ForeignKey(User,related_name="Patron")
	book = models.ForeignKey(Book)
	librarian = models.ForeignKey(User,related_name="Librarian")
	type = models.IntegerField()