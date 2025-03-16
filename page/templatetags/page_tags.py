from django.conf import settings
from django import template
from django.utils.safestring import mark_safe
from datetime import datetime
from django.core.cache import cache
import json
from datetime import datetime, timedelta
from django.utils import timezone
from django.utils.translation import gettext as _
from slugify import slugify
from work.models import Work
from django.db.models import Count
from user.models import CustomUser
from city.models import Country, City
from profession.models import Profession
from work.models import Gender
from page.forms import TuVanForm
from collections import defaultdict
from page.check_url import is_valid_url
from django.db import models


register = template.Library()
@register.simple_tag
def setting(name):
	return getattr(settings, name, "")

@register.inclusion_tag('widgets/_country.html')
def countries():
	countries = Work.actives.filter(country__show_home = True).values('country__name', 'country__image', 'country__slug').annotate(count=Count('id')).order_by('-count')
	return {'countries': countries}


@register.inclusion_tag('widgets/_ung_vien.html', takes_context=True)
def ungvien(context):
	request = context['request'] 
	user = request.user
	ungvien = CustomUser.objects.filter(role="applicant", is_staff = False).exclude(
		ho_va_ten_dem__isnull=True
	).exclude(
		ten_goi__isnull=True
	).values('id','ho_va_ten_dem', 'avata', 'nam_sinh', 'tinh_thanh_pho__name', 'ten_goi', 'nam_sinh').order_by('-id')[0:10]
	return {'ungvien': ungvien, 'user':user}


@register.inclusion_tag('widgets/_search.html', takes_context=True)
def search(context):
	request = context['request'] 
	countries = Country.actives.values('name').order_by('-priority')
	profess = Profession.actives.values('name').order_by('-priority')
	cities = City.actives.values('name').order_by('-priority')
	genders = Gender.objects.values('name').order_by('-id')
	current_year = datetime.now().year
	min_year = current_year - 18
	years = range(min_year, 1972, -1)
	country_name = request.GET.get("quoc_gia", "").strip()
	profession_name = request.GET.get("nganh_nghe", "").strip()
	city_name = request.GET.get("noi_tuyen", "").strip()
	gender_name = request.GET.get("gioi_tinh", "").strip()
	birth_year = request.GET.get("nam_sinh", "").strip()
	return {'countries': countries, 'profess':profess, 'cities':cities, 'genders':genders,
	'years':years, 'country_name':country_name, 'profession_name':profession_name,
	'city_name':city_name, 'gender_name':gender_name, 'birth_year':birth_year}	


@register.inclusion_tag('widgets/_footer_search.html', takes_context=True)
def footer_search(context):
	request = context['request'] 
	countries = Country.actives.values('name').order_by('-priority')
	profess = Profession.actives.values('name').order_by('-priority')
	cities = City.actives.values('name').order_by('-priority')
	genders = Gender.objects.values('name').order_by('-id')
	current_year = datetime.now().year
	min_year = current_year - 18
	years = range(min_year, 1972, -1)
	country_name = request.GET.get("quoc_gia", "").strip()
	profession_name = request.GET.get("nganh_nghe", "").strip()
	city_name = request.GET.get("noi_tuyen", "").strip()
	gender_name = request.GET.get("gioi_tinh", "").strip()
	birth_year = request.GET.get("nam_sinh", "").strip()
	return {'countries': countries, 'profess':profess, 'cities':cities, 'genders':genders,
	'years':years, 'country_name':country_name, 'profession_name':profession_name,
	'city_name':city_name, 'gender_name':gender_name, 'birth_year':birth_year}


@register.inclusion_tag('widgets/_modal_tu_van.html')
def tuvan():
	form = TuVanForm()
	return {'form':form}

@register.inclusion_tag('widgets/_modal_login.html')
def login():
	countries = Country.actives.values('id','name').order_by('-priority')
	profess = Profession.actives.values('id','name').order_by('-priority')
	cities = City.actives.values('id','name').order_by('-priority')
	genders = Gender.objects.values('id', 'name').order_by('-id')
	current_year = datetime.now().year
	min_year = current_year - 18
	years = range(min_year, 1972, -1)
	return {'countries': countries, 'profess':profess, 'cities':cities, 'genders':genders,
	'years':years}

@register.inclusion_tag('widgets/_blog_work.html')
def blogWork():
	works = Work.actives.select_related('country', 'user').values(
	'id', 
	'country__name', 'country__image', 'country__slug',
	'name', 'slug', 'image', 'luong_co_ban', 'luong_co_ban_menh_gia',
	'nam_sinh', 'ket_thuc_nam_sinh',
	'user__avata', 'user__id', 'user__ho_va_ten_dem', 'user__phone',
	'user__facebook', 'user__zalo', 'view', 'ngay_thi_tuyen', 'user__ten_goi',
	'hot_expiry' 
	).annotate(
		is_hot=models.Case(
		models.When(hot_expiry__gt=timezone.now(), then=1),
		default=0,
		output_field=models.IntegerField(),
	)
	).order_by('-is_hot', '-updated')[0:5]

	require_gioi_tinh_map = defaultdict(list)
	for work in Work.actives.prefetch_related('gioi_tinh'):
		for gioi_tinh in work.gioi_tinh.all():
			require_gioi_tinh_map[work.id].append(gioi_tinh.name)

	for work in works:
		work['gioi_tinh'] = require_gioi_tinh_map.get(work['id'], [])
		fb_link = work.get('user__facebook', '')
		if not fb_link or not is_valid_url(fb_link):
			work['user__facebook'] = None 
	return {'works': works, 'blogWork':blogWork}	


@register.inclusion_tag('widgets/_nhatuyendung.html', takes_context=True)
def NTD(context):
	request = context['request'] 
	user = request.user
	return {'user': user}


@register.inclusion_tag('widgets/_filter_ntd.html')
def filterNTD():
	genders = Gender.objects.all()
	current_year = datetime.now().year
	min_year = current_year - 18
	years = range(min_year, 1972, -1)
	cities = City.objects.all()
	countries = Country.objects.all()
	profess = Profession.objects.all()
	return {'countries': countries, 'profess':profess, 'cities':cities, 'genders':genders,
	'years':years}	