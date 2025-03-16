from django.urls import path
from . import views
app_name = "city"

urlpatterns = [
	path('<slug:slug>', views.detail, name='detail'),
	path('<slug:slug>/page-<int:page>', views.detail, name='detailCountry'),
]