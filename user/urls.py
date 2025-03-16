from django.urls import path
from . import views
app_name = "user"

urlpatterns = [
	path('hosoungvien/<int:id>', views.ungvien, name='ungvien'),
	path('hosotuyendung/<int:id>', views.nhatuyendung, name='nhatuyendung'),
	path('hosotuyendung/<int:id>/page-<int:page>', views.nhatuyendung, name='nhatuyendung_page'),
	path('candidates/myinfo', views.updateungvien, name='updateungvien'),
	path('employers/myinfo', views.updatenhatuyendung, name='updatenhatuyendung'),
	path('employers/add_job', views.add_job, name='add_job'),
	path('employers/list_job', views.list_job, name='list_job'),
	path('employers/list_job/page-<int:page>', views.list_job, name='list_job_page'),
	path('employers/add_fund', views.add_fund, name='add_fund'),
	path('employers/edit_job/<int:id>', views.edit_job, name='edit_job'),
	path('employers/remove_job/<int:id>', views.remove_job, name='remove_job'),
	path("employers/up_tin/", views.up_tin, name="up_tin"),
	path('employers/expired_job', views.expired_job, name='expired_job'),
	path('employers/expired_job/page-<int:page>', views.expired_job, name='expired_job_page'),
	path("employers/set_hot_tin", views.set_hot_tin, name="set_hot_tin"),
	path("employers/candidate_list", views.candidate_search, name="candidate_search"),
	path("employers/candidate_saved", views.candidate_saved, name="candidate_saved"),
	path("employers/view_candidate", views.view_candidate, name="view_candidate"),
	path("employers/candidate_recruitment", views.candidate_recruitment, name="candidate_recruitment"),
	path('confirm-payment/<int:candidate_id>', views.confirm_payment, name='confirm_payment'),
	path('getProvinces', views.getProvinces, name='getProvinces'),
]