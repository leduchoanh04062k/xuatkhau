from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from sorl.thumbnail import ImageField
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from utils.conts import Conts
from city.models import Country, City
from work.models import Work
from profession.models import Profession
import random
from django.utils.timezone import now
from datetime import timedelta
from django.contrib.auth import get_user_model

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class CustomUser(AbstractUser):
	otp_code = models.CharField(max_length=6, blank=True, null=True, verbose_name="Mã OTP")
	otp_created_at = models.DateTimeField(blank=True, null=True, verbose_name="Thời gian tạo OTP")
	point = models.PositiveIntegerField(default=0, verbose_name=u'Giá tiền')
	free_posts_today = models.IntegerField(default=2, verbose_name=u'Đăng miễn phí')
	last_reset_date = models.DateField(null=True, blank=True)
	ho_va_ten_dem = models.CharField(max_length=250, verbose_name='Họ và Tên đệm', blank=True, null=True)
	ten_goi = models.CharField(max_length=250, verbose_name='Tên gọi', blank=True, null=True)
	gioi_tinh = models.CharField(max_length=250,blank=True, null=True, choices=Conts.GIOI_TINH_CHOICES, verbose_name='Giới tính')
	nam_sinh = models.CharField(max_length=250,blank=True, null=True, verbose_name='Năm sinh')
	avata = ImageField(upload_to='user', verbose_name='Ảnh', blank=True, null=True)
	anh_bia = ImageField(upload_to='user', verbose_name='Ảnh bìa', blank=True, null=True)
	phone = models.CharField(max_length=250, blank=True, null=True, verbose_name='Điện thoại')
	zalo = models.CharField(max_length=250, blank=True, null=True, verbose_name='Zalo')
	facebook = models.CharField(max_length=250,blank=True, null=True, verbose_name='Facebook')
	dia_chi = models.CharField(max_length=250, blank=True, null=True, verbose_name='Địa chỉ')
	sinh_song_tai = models.CharField(max_length=250, blank=True, null=True, verbose_name='Sinh sống tại')
	noi_lam_viec = models.CharField(max_length=250, blank=True, null=True, verbose_name='Nơi làm việc')
	ten_viet_tat = models.CharField(max_length=250, blank=True, null=True, verbose_name='Tên viết tắt')
	chuc_vu = models.CharField(max_length=250, blank=True, null=True, verbose_name='Chức vụ')
	kinh_nghiem = models.CharField(max_length=250, blank=True, null=True, verbose_name='Kinh nghiệm')
	tinh_thanh_pho = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Tỉnh/ Thành phố', blank=True, null=True)
	tu_van = RichTextUploadingField(blank=True, null=True, verbose_name='Tư Vấn')
	ghi_chu = RichTextUploadingField(blank=True, null=True, verbose_name='Ghi chú')

	country = models.ManyToManyField(Country, related_name='userprofile_country', verbose_name='Xklđ các nước', blank=True, null=True)
	nganh_nghe = models.ManyToManyField(Profession, related_name='userprofile_nganh_nghe', verbose_name='Ngành nghề', blank=True, null=True)
	
	chieu_cao = models.CharField(max_length=250, blank=True, null=True, verbose_name='Chiều cao (cm)')
	can_nang = models.CharField(max_length=250, blank=True, null=True, verbose_name='Cân nặng (kg)')
	thi_luc = models.CharField(max_length=250, blank=True, null=True, verbose_name='Thị lực (1 - 10)')
	hinh_xam = models.CharField(max_length=250, blank=True, null=True, choices=Conts.XAM_CHOICES, verbose_name='Hình Xăm')
	viem_gan_b = models.CharField(max_length=250, blank=True, null=True, choices=Conts.XAM_CHOICES, verbose_name='Viêm gan B')
	hut_thuoc = models.CharField(max_length=250, blank=True, null=True, choices=Conts.XAM_CHOICES, verbose_name='Hút thuốc')
	uong_ruou = models.CharField(max_length=250, blank=True, null=True, choices=Conts.XAM_CHOICES, verbose_name='Uống rượu')
	benh_di_truyen = models.CharField(max_length=250, blank=True, null=True, choices=Conts.XAM_CHOICES, verbose_name='Bệnh di truyền')

	tot_nghiep = models.CharField(max_length=250, blank=True, null=True, choices=Conts.TRINH_DO_HOC_VAN_CHOICES, verbose_name='Tốt nghiệp')
	ngoai_ngu = models.CharField(max_length=250, blank=True, null=True, choices=Conts.NGOAI_NGU_CHOICES, verbose_name='Ngoại ngữ')
	bang_nghe = models.CharField(max_length=250, blank=True, null=True,choices=Conts.XAM_CHOICES, verbose_name='Bằng nghề')
	

	tay_nghe = models.CharField(max_length=250, blank=True, null=True, verbose_name='Tay nghề')
	da_di_xkld = models.CharField(max_length=250, blank=True, null=True, verbose_name='Đã đi xklđ')

	tinh_cach = models.CharField(max_length=250, blank=True, null=True, verbose_name='Tính cách')
	so_thich = models.CharField(max_length=250, blank=True, null=True, verbose_name='Sở thích')
	yeu_cau_khac = models.CharField(max_length=250, blank=True, null=True, verbose_name='Yêu cầu khác')

	role = models.CharField(max_length=20,choices=Conts.ROLE_CHOICES, verbose_name="Vai trò")

	groups = models.ManyToManyField(Group, related_name="customuser_groups", blank=True)
	user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions", blank=True)


	class Meta:
		ordering = ('-id',)
		verbose_name_plural = "Tài khoản người dùng"	
		
	def __str__(self):
		return f"{self.username}"


class Advisory(models.Model):
	work = models.ForeignKey(Work, on_delete=models.CASCADE, verbose_name='Việc làm', blank=True, null=True)
	name = models.CharField(max_length=127)
	phone = models.CharField(max_length=155)
	active = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	is_paid = models.BooleanField(default=False, verbose_name="Đã thanh toán")
	class Meta:
		ordering = ('-id',)
		verbose_name_plural = "Sđt cần tư vấn"	

	objects = models.Manager() 
	actives = ActiveManager()

	def __str__(self):
		return str(self.name)

	def get_price(self):
		if self.work and "nhật" in self.work.name.lower():
			return 80000
		return 20000	

User = get_user_model()
class CandidateView(models.Model):
    employer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="viewed_candidates", verbose_name="Nhà tuyển dụng")
    candidate = models.ForeignKey(User, on_delete=models.CASCADE, related_name="viewed_by_employers", verbose_name="Ứng viên")
    viewed_at = models.DateTimeField(auto_now_add=True, verbose_name="Thời gian xem")

    class Meta:
        unique_together = ('employer', 'candidate')
        ordering = ['-viewed_at']
        verbose_name = "Lịch sử xem ứng viên"

    def __str__(self):
        return f"{self.employer.username} đã xem {self.candidate.username}"
