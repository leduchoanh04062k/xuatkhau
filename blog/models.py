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


class Cate(models.Model):
	name = models.CharField(max_length=250)
	slug = models.SlugField(max_length=127, unique = True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-id',)
		verbose_name_plural = "Danh mục"

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(unidecode(self.name)) 
		super().save(*args, **kwargs)

	def __str__(self):
		return self.name


class Blog(models.Model):
	cate = models.ForeignKey(Cate, on_delete=models.CASCADE, related_name='blog_cate', verbose_name='Danh mục')
	name = models.CharField(max_length=250)
	slug = models.SlugField(max_length=127, unique = True, blank=True)
	description = models.TextField(blank=True, null=True)
	content = RichTextUploadingField(blank=True, null=True)
	image = ImageField(upload_to='blog')
	priority = models.IntegerField(default=1)
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-id',)
		verbose_name_plural = "Bài Viết"

	objects = models.Manager() 
	actives = ActiveManager()

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(unidecode(self.name)) 
		super().save(*args, **kwargs)
		
	def __str__(self):
		return self.name


