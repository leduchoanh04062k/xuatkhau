from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from sorl.thumbnail import ImageField
from city.models import Country, City, Province
from profession.models import Profession
from utils.conts import Conts
from datetime import timedelta, date
import calendar
from smart_selects.db_fields import ChainedForeignKey
from django.conf import settings
from django.utils.text import slugify
from unidecode import unidecode


class ActiveManager(models.Manager):
	def get_queryset(self):
		return super().get_queryset().filter(active=True)


class Gender(models.Model):
	name = models.CharField(max_length=50)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		verbose_name_plural = "Giới tính"

	def __str__(self):
		return self.name


class Workmanship(models.Model):
	name = models.CharField(max_length=50)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name',)
		verbose_name_plural = "Tay Nghề"

	def __str__(self):
		return self.name


class Work(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
	name = models.CharField(max_length=250, verbose_name='Tên đơn hàng')
	slug = models.SlugField(max_length=127, unique = True, blank=True)
	country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='work_country', verbose_name='Quốc gia')
	province = ChainedForeignKey(Province, 
		chained_field="country",
		chained_model_field="country", 
		show_all=False, 
		auto_choose=True,
		sort=True,
		blank=True, null=True,
		related_name='work_id',
		verbose_name='Tỉnh, khu vực', on_delete=models.CASCADE)
	cong_ty_nghiep_doan = models.CharField(max_length=250, verbose_name='Công ty, nghiệp đoàn', blank=True, null=True)
	nganh_nghe = models.ManyToManyField(Profession, blank=True, null=True, related_name='work_nganh_nghe', verbose_name='Ngành nghề')
	cong_viec_cu_the = RichTextUploadingField(blank=True, verbose_name='Công việc cụ thể')
	noi_thi_tuyen = models.ManyToManyField(City, verbose_name='Nơi thi tuyển', blank=True, null=True)
	thoi_gian_lam_viec = models.CharField(max_length=250, verbose_name='Thời gian làm việc')
	luong_co_ban = models.CharField(max_length=250, verbose_name='Lương cơ bản')
	luong_co_ban_menh_gia = models.CharField(max_length=250, choices=Conts.MENH_GIA, blank=True, null=True, verbose_name='Mệnh giá lương cơ bản')
	lam_them = models.CharField(max_length=250,choices=Conts.LAM_THEM, blank=True, null=True, verbose_name='Làm thêm')
	thu_nhap_du_kien = models.CharField(max_length=250, verbose_name='Thu nhập dự kiến')
	thu_nhap_du_kien_menh_gia = models.CharField(choices=Conts.MENH_GIA, blank=True, null=True, verbose_name='Mệnh giá thu nhập dự kiến')
	quyen_loi_khac = RichTextUploadingField(blank=True, null=True, verbose_name='Quyền lợi khác')
	so_luong_tuyen = models.CharField(max_length=250, default=0, verbose_name='Số lượng tuyển')
	hop_dong = models.CharField(max_length=250,choices=Conts.HOP_DONG, blank=True, null=True, verbose_name='Hợp đồng')
	phi_xuat_canh = models.CharField(max_length=250,blank=True, null=True, verbose_name='Phí xuất cảnh')
	phi_xuat_canh_menh_gia = models.CharField(max_length=250, choices=Conts.MENH_GIA, blank=True, null=True, verbose_name='Phí xuất cảnh mệnh giá')
	chuong_trinh_ho_tro = RichTextUploadingField(blank=True, null=True, verbose_name='Chương trình hỗ trợ')
	image = ImageField(upload_to='work', verbose_name='Ảnh',blank=True, null=True,)
	noi_dung_chi_tiet = RichTextUploadingField(blank=True, verbose_name='Nội dung chi tiết')
	hot_expiry = models.DateTimeField(null=True, blank=True, verbose_name='Ngày hết hạn tin HOT')
	view = models.PositiveIntegerField(default=0, verbose_name='Lượt xem')


	gioi_tinh = models.ManyToManyField(Gender, verbose_name='Giới tính',  related_name='require_gioi_tinh', blank=True, null=True)
	nam_sinh = models.CharField(max_length=250, default=0, verbose_name='Năm sinh bắt đầu')
	ket_thuc_nam_sinh = models.CharField(max_length=250, default=0, verbose_name='Năm sinh kết thúc')
	trinh_do_hoc_van = models.CharField(max_length=250, choices=Conts.TRINH_DO_HOC_VAN_CHOICES, blank=True, null=True, verbose_name='Trình độ học vấn')
	chuyen_nganh = models.CharField(max_length=250, choices=Conts.CHUYEN_NGANH_CHOICES, blank=True, null=True, verbose_name='Chuyên ngành')
	tay_nghe = models.ManyToManyField(Workmanship, verbose_name='Tay Nghề', related_name='require_tay_nghe', blank=True, null=True)
	ngoai_ngu = models.CharField(max_length=250, choices=Conts.NGOAI_NGU_CHOICES, blank=True, null=True, verbose_name='Ngoại ngữ')
	yeu_cau_hoc_tieng = models.CharField(max_length=250, choices=Conts.YEU_CAU_HOC_TIENG_CHOICES, blank=True, null=True, verbose_name='Yêu cầu tiếng anh')
	tinh_trang_suc_khoe = models.CharField(max_length=250, choices=Conts.TINH_TRANG_SUC_KHOE_CHOICES, blank=True, null=True, verbose_name='Tình trạng sức khoẻ')
	thi_luc = models.CharField(max_length=250, choices=Conts.THI_LUC_CHOICES, blank=True, null=True, verbose_name='Thị lực')
	viem_gan_b = models.CharField(max_length=250, choices=Conts.VIEM_GAN_B_CHOICES, blank=True, null=True, verbose_name='VGB')
	xam_hinh = models.CharField(max_length=250, choices=Conts.XAM_HINH_CHOICES, blank=True, null=True, verbose_name='Xăm hình')
	yeu_cau_khac = RichTextUploadingField(blank=True, verbose_name='Yêu cầu khác')
	hinh_thuc_thi_tuyen = models.CharField(max_length=250, blank=True, null=True, verbose_name='Hình thức thi tuyển')
	ngay_thi_tuyen = models.DateField(blank=True, null=True, verbose_name='Ngày thi tuyển')
	han_dang_ky =models.DateField(verbose_name='Hạn đăng ký', blank=True, null=True)
	du_kien_xuat_canh = models.CharField(max_length=250, blank=True, null=True, verbose_name='Dự kiến xuất cảnh')
	is_confirmed = models.BooleanField(default=False)
	priority = models.IntegerField(default=1)
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)


	class Meta:
		ordering = ('-id',)
		verbose_name_plural = "Đơn hàng"

	objects = models.Manager() 
	actives = ActiveManager()
	
	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(unidecode(self.name)) 
		super().save(*args, **kwargs)

	def __str__(self):
		return self.name	

	
	@property
	def is_hot(self):
		if self.hot_expiry and self.hot_expiry > timezone.now():
			return True
		return False	
	

class Image(models.Model):
	work = models.ForeignKey(Work, related_name='image_work', on_delete=models.CASCADE)
	image = ImageField(upload_to='work')

	class Meta:
		ordering = ('id',)
		verbose_name_plural = "Images"

	def __str__(self):
		return self.work.name	
	


class Price(models.Model):
	price = models.PositiveIntegerField(max_length=250, default=0, verbose_name='Giá tiền')
	khuyen_mai = models.CharField(max_length=250, verbose_name='Khuyến mại', blank=True, null=True)
	active = models.BooleanField(default=True)
	priority = models.IntegerField(default=1)
	updated = models.DateTimeField(auto_now=True)

	objects = models.Manager() 
	actives = ActiveManager()

	class Meta:
		ordering = ('id',)
		verbose_name_plural = "Tiền nạp tài khoản"


