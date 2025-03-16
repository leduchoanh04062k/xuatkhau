from django.urls import path
from . import views
app_name = "page"

urlpatterns = [
	path('', views.home, name='home'),
	path('', views.home, name='register_view'),
	path('page-<int:page>', views.home, name='index'),
	path('<slug:slug>/<slug:slug_work>.html/page-<int:page>', views.detailWork, name='detailWork'),
	path('<slug:slug>/<slug:slug_work>.html', views.detailWork, name='detailWork'),
	path('tim-kiem', views.search, name='search'),
	path('ajaxAdvisory', views.ajaxAdvisory, name="ajaxAdvisory"),
	path('page/<slug:slug_page>', views.detailPage, name='detailPage'),

	path("login_view", views.login_view, name="login_view"),
	path("logout_view", views.logout_view, name="logout_view"),
	path("verify-otp", views.verify_otp, name="verify_otp"),
	path("register", views.register_view, name="register"),
	path("send_otp_reset_password", views.send_otp_reset_password, name="send_otp_reset_password"),
	path("verify_otp_reset_password", views.verify_otp_reset_password, name="verify_otp_reset_password"),

	path("update_user_info", views.update_user_info_view, name="update_user_info_view"),
	
]