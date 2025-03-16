from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse, HttpResponsePermanentRedirect
from django.core.cache import cache
import requests
from datetime import datetime, timedelta
import json
from .models import *
from page.pagination import paginate
from work.models import Work
from collections import defaultdict

PAGE_BLOG = 10

def category(request, slug, page=1):
	cate = get_object_or_404(Cate, slug=slug)
	total = Blog.actives.filter(cate_id = cate.id).all().count()
	paginator = paginate(page, total, PAGE_BLOG)
	start_index = paginator.number
	blogs = Blog.actives.filter(cate_id = cate.id).values('name', 'cate__slug', 'slug', 'image', 'description').order_by('-id')[(start_index-1)*PAGE_BLOG:start_index*PAGE_BLOG]
	return render(request, 'blog/index.html', {'cate':cate, 'blogs':blogs, 'paginator':paginator, 'page':page})


def detail(request, slug, slug_blog):
	cate = get_object_or_404(Cate, slug=slug)
	blog = get_object_or_404(Blog, slug=slug_blog, cate_id = cate.id)
	blogs = Blog.actives.filter(cate_id = cate.id).exclude(id = blog.id).values('name', 'cate__slug', 'slug', 'image', 'description').order_by('-priority')[0:3]
	return render(request, 'blog/detail.html', {'blog':blog, 'cate':cate, 'blogs':blogs})		