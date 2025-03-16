from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from sorl.thumbnail import ImageField
from datetime import date
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.text import slugify
from unidecode import unidecode


class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class Page(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField(max_length=127, blank=True, null=True)
	content = RichTextUploadingField(blank=True, null=True)
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	
	class Meta:
		ordering = ('-id',)
		verbose_name_plural = "Page"

	objects = models.Manager() 
	actives = ActiveManager()

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(unidecode(self.name)) 
		super().save(*args, **kwargs)

	def __str__(self):
		return self.name

