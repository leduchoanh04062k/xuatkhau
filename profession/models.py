from django.db import models
from django.utils import timezone
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User
from django.conf import settings
from city.models import Country
from django.utils.text import slugify
from unidecode import unidecode

class ActiveManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(active=True)


class Profession(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField(max_length=127, unique = True, blank=True)
	priority = models.IntegerField(default=1)
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		verbose_name_plural = "Ngành nghề"

	objects = models.Manager() 
	actives = ActiveManager()

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(unidecode(self.name)) 
		super().save(*args, **kwargs)
		
	def __str__(self):
		return self.name
