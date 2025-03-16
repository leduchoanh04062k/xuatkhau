from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from sorl.thumbnail import ImageField
from django.conf import settings
from django.utils.text import slugify
from unidecode import unidecode

class ActiveManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(active=True)

class Country(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField(max_length=127, unique = True, blank=True)
	image = ImageField(upload_to='country', null=True, blank=True)
	content = RichTextUploadingField(blank=True, null=True)
	priority = models.IntegerField(default=1)
	show_home = models.BooleanField(default=False)
	active = models.BooleanField(default=True)
	is_japan = models.BooleanField(default=False) 
	meta_title = models.CharField(max_length=255, blank=True, null=True)
	meta_description = models.CharField(max_length=255, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		verbose_name_plural = "Quốc gia"

	objects = models.Manager() 
	actives = ActiveManager()


	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(unidecode(self.name)) 
		super().save(*args, **kwargs)

		
	def __str__(self):
		return self.name



class City(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField(max_length=127, unique = True, blank=True)
	priority = models.IntegerField(default=1)
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		verbose_name_plural = "Nơi thi tuyển"

	objects = models.Manager() 
	actives = ActiveManager()


	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(unidecode(self.name)) 
		super().save(*args, **kwargs)
		
	def __str__(self):
		return self.name


class Province(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='province_country', verbose_name='Quốc gia')
	name = models.CharField(max_length=250)
	priority = models.IntegerField(default=1)
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('priority',)
		verbose_name_plural = "Tỉnh, khu vực"

	def __str__(self):
		return self.name