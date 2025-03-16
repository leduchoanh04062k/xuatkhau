from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponsePermanentRedirect
import requests
from datetime import datetime, timedelta
import json
from .models import *
from django.contrib.postgres.search import SearchQuery
from work.models import Work
from collections import defaultdict
from page.pagination import paginate
from page.check_url import is_valid_url
PAGE_NUMBER = 30


def detail(request, slug, page=1):
	country = get_object_or_404(Country, slug=slug)
	total = Work.actives.filter(country__id = country.id).all().count()
	paginator = paginate(page, total,PAGE_NUMBER)
	start_index = paginator.number
	path_url = "/{0}".format(country.slug)
	works = Work.actives.filter(country__id = country.id).select_related('country', 'user').values(
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
	).order_by('-is_hot', '-updated')[(start_index-1)*PAGE_NUMBER:start_index*PAGE_NUMBER]
	require_gioi_tinh_map = defaultdict(list)
	for work in Work.actives.prefetch_related('gioi_tinh'):
		for gioi_tinh in work.gioi_tinh.all():
			require_gioi_tinh_map[work.id].append(gioi_tinh.name)

	for work in works:
		work['gioi_tinh'] = require_gioi_tinh_map.get(work['id'], [])
		fb_link = work.get('user__facebook', '')
		if not fb_link or not is_valid_url(fb_link):
			work['user__facebook'] = None 

	return render(request, 'country/detail.html',{'country':country, 'works':works, 'paginator':paginator, 'page':page, 'path_url':path_url})