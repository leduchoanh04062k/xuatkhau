from django.urls import path
from . import views
app_name = "blog"

urlpatterns = [
	path('blog/<slug:slug>', views.category, name='category'),
	path('blog/<slug:slug>/page-<int:page>', views.category, name='category_page'),
	path('blog/<slug:slug>/<slug:slug_blog>.html', views.detail, name='detail'),
]