from django import forms
from django.utils.html import strip_tags
from utils.conts import Conts
from datetime import datetime

class ADDForm(forms.Form):
	name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Tiêu đề', 'class' : 'form-control', 'autocomplete':'off'}))
	country = forms.ChoiceField(
		required=False,
		widget=forms.Select(attrs={'class': 'form-select set-selected', 'id':'country'}),
		choices=[] 
	)
	province = forms.ChoiceField(
		required=False,
		choices=[],
		widget=forms.Select(attrs={'class': 'form-select set-selected', 'id':'province'})
	)
	cong_ty_nghiep_doan = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Công ty và nghiệp đoàn', 'class' : 'form-control', 'autocomplete':'off'}))
	nganh_nghe = forms.MultipleChoiceField(
		required=False,
		choices=[],
		widget=forms.CheckboxSelectMultiple(attrs={'class': 'set-selected'})
	)
	cong_viec_cu_the = forms.CharField(
		required=False, 
		widget=forms.Textarea(attrs={'rows': 6, 'class': 'form-control', 'placeholder': 'Công việc cụ thể', 'autocomplete':'off'})
	)
	noi_thi_tuyen = forms.MultipleChoiceField(
		required=False,
		choices=[],
		widget=forms.CheckboxSelectMultiple(attrs={'class': 'set-selected'})
	)
	thoi_gian_lam_viec = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Thời gian làm việc', 'class' : 'form-control', 'autocomplete':'off'}))
	luong_co_ban = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Lương cơ bản/tháng', 'class' : 'form-control', 'autocomplete':'off'}))
	luong_co_ban_menh_gia = forms.ChoiceField(choices=Conts.MENH_GIA, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	lam_them = forms.ChoiceField(choices=Conts.LAM_THEM, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	thu_nhap_du_kien = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Thu nhập dự kiến/tháng', 'class' : 'form-control', 'autocomplete':'off'}))
	thu_nhap_du_kien_menh_gia = forms.ChoiceField(choices=Conts.MENH_GIA, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	quyen_loi_khac = forms.CharField(
		required=False, 
		widget=forms.Textarea(attrs={'rows': 6, 'class': 'form-control', 'placeholder': 'Quyền lợi khác', 'autocomplete':'off'})
	)
	so_luong_tuyen = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Số lượng tuyển', 'class' : 'form-control', 'autocomplete':'off'}))
	hop_dong = forms.ChoiceField(choices=Conts.HOP_DONG, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	phi_xuat_canh = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Phí xuất cảnh', 'class' : 'form-control', 'autocomplete':'off'}))
	phi_xuat_canh_menh_gia = forms.ChoiceField(choices=Conts.MENH_GIA, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	chuong_trinh_ho_tro = forms.CharField(
		required=False, 
		widget=forms.Textarea(attrs={'rows': 6, 'class': 'form-control', 'placeholder': 'Chương trình hỗ trợ', 'autocomplete':'off'})
	)
	gioi_tinh = forms.MultipleChoiceField(
		required=False,
		choices=[],
		widget=forms.CheckboxSelectMultiple(attrs={'class': 'set-selected'})
	)
	nam_sinh = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'VD: 18', 'class' : 'form-control', 'id':'nam_sinh', 'autocomplete':'off'}))
	ket_thuc_nam_sinh = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'VD: 30', 'id':'ket_thuc_nam_sinh', 'class' : 'form-control', 'autocomplete':'off'}))
	trinh_do_hoc_van = forms.ChoiceField(choices=Conts.TRINH_DO_HOC_VAN_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	chuyen_nganh = forms.ChoiceField(choices=Conts.CHUYEN_NGANH_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	ngoai_ngu = forms.ChoiceField(choices=Conts.NGOAI_NGU_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	yeu_cau_hoc_tieng = forms.ChoiceField(choices=Conts.YEU_CAU_HOC_TIENG_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	tinh_trang_suc_khoe = forms.ChoiceField(choices=Conts.TINH_TRANG_SUC_KHOE_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	tay_nghe = forms.MultipleChoiceField(
		required=False,
		choices=[],
		widget=forms.CheckboxSelectMultiple(attrs={'class': 'set-selected'})
	)
	thi_luc = forms.ChoiceField(choices=Conts.THI_LUC_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	viem_gan_b = forms.ChoiceField(choices=Conts.VIEM_GAN_B_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	xam_hinh = forms.ChoiceField(choices=Conts.XAM_HINH_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	yeu_cau_khac = forms.CharField(
		required=False, 
		widget=forms.Textarea(attrs={'rows': 6, 'class': 'form-control', 'placeholder': 'Yêu cầu khác', 'autocomplete':'off'})
	)
	hinh_thuc_thi_tuyen = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Hình thức thi tuyển', 'class' : 'form-control', 'autocomplete':'off'}))
	ngay_thi_tuyen = forms.DateField(
		required=False,
		input_formats=["%d-%m-%Y", "%Y-%m-%d"],
		widget=forms.DateInput(attrs={'placeholder': 'DD-MM-YYYY', 'class': 'form-control', 'id': 'depart', 'autocomplete':'off'})
	)
	han_dang_ky = forms.DateField(
		required=False,
		input_formats=["%d-%m-%Y", "%Y-%m-%d"],
		widget=forms.DateInput(attrs={'placeholder': 'DD-MM-YYYY', 'class': 'form-control', 'id': 'retur', 'autocomplete':'off'})
	)
	du_kien_xuat_canh = forms.CharField(
		required=False,
		widget=forms.TextInput(attrs={'class': 'form-select set-selected'})
	)
	noi_dung_chi_tiet = forms.CharField(
		required=False, 
		widget=forms.Textarea(attrs={'rows': 10, 'class': 'form-control', 'id':'editor', 'placeholder': 'Nội dung chi tiết'})
	)
	image = forms.FileField(
		required=False,
		widget=forms.ClearableFileInput(attrs={'id': 'file-input-media', 'class': 'd-none'})
	)
	is_confirmed = forms.BooleanField(required=True, label="Tôi cam kết thông tin đúng sự thật")
	def __init__(self, *args, **kwargs):
		countries = kwargs.pop('countries', [])
		profess = kwargs.pop('profess', [])
		cities = kwargs.pop('cities', [])
		genders = kwargs.pop('genders', [])
		workmanships = kwargs.pop('workmanships', [])
		provinces = kwargs.pop('provinces', [])
		super(ADDForm, self).__init__(*args, **kwargs)
		self.fields['country'].choices = [(str(c['id']), c['name']) for c in countries]
		self.fields['nganh_nghe'].choices = [(str(c['id']), c['name']) for c in profess] 
		self.fields['noi_thi_tuyen'].choices = [(str(c['id']), c['name']) for c in cities] 
		self.fields['gioi_tinh'].choices = [(str(c['id']), c['name']) for c in genders] 
		self.fields['tay_nghe'].choices = [(str(c['id']), c['name']) for c in workmanships] 
		self.fields['province'].choices = [(str(c['id']), c['name']) for c in provinces]



class EditForm(forms.Form):
	name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Tiêu đề', 'class' : 'form-control', 'autocomplete':'off'}))
	country = forms.ChoiceField(
		required=False,
		widget=forms.Select(attrs={'class': 'form-select set-selected', 'id':'country'}),
		choices=[] 
	)
	province = forms.ChoiceField(
		required=False,
		choices=[],
		widget=forms.Select(attrs={'class': 'form-select set-selected', 'id':'province'})
	)
	cong_ty_nghiep_doan = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Công ty và nghiệp đoàn', 'class' : 'form-control', 'autocomplete':'off'}))
	nganh_nghe = forms.MultipleChoiceField(
		required=False,
		choices=[],
		widget=forms.CheckboxSelectMultiple(attrs={'class': 'set-selected'})
	)
	cong_viec_cu_the = forms.CharField(
		required=False, 
		widget=forms.Textarea(attrs={'rows': 6, 'class': 'form-control', 'placeholder': 'Công việc cụ thể', 'autocomplete':'off'})
	)
	noi_thi_tuyen = forms.MultipleChoiceField(
		required=False,
		choices=[],
		widget=forms.CheckboxSelectMultiple(attrs={'class': 'set-selected'})
	)
	thoi_gian_lam_viec = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Thời gian làm việc', 'class' : 'form-control', 'autocomplete':'off'}))
	luong_co_ban = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Lương cơ bản/tháng', 'class' : 'form-control', 'autocomplete':'off'}))
	luong_co_ban_menh_gia = forms.ChoiceField(choices=Conts.MENH_GIA, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	lam_them = forms.ChoiceField(choices=Conts.LAM_THEM, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	thu_nhap_du_kien = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Thu nhập dự kiến/tháng', 'class' : 'form-control', 'autocomplete':'off'}))
	thu_nhap_du_kien_menh_gia = forms.ChoiceField(choices=Conts.MENH_GIA, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	quyen_loi_khac = forms.CharField(
		required=False, 
		widget=forms.Textarea(attrs={'rows': 6, 'class': 'form-control', 'placeholder': 'Quyền lợi khác', 'autocomplete':'off'})
	)
	so_luong_tuyen = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Số lượng tuyển', 'class' : 'form-control', 'autocomplete':'off'}))
	hop_dong = forms.ChoiceField(choices=Conts.HOP_DONG, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	phi_xuat_canh = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Phí xuất cảnh', 'class' : 'form-control', 'autocomplete':'off'}))
	phi_xuat_canh_menh_gia = forms.ChoiceField(choices=Conts.MENH_GIA, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	chuong_trinh_ho_tro = forms.CharField(
		required=False, 
		widget=forms.Textarea(attrs={'rows': 6, 'class': 'form-control', 'placeholder': 'Chương trình hỗ trợ', 'autocomplete':'off'})
	)
	gioi_tinh = forms.MultipleChoiceField(
		required=False,
		choices=[],
		widget=forms.CheckboxSelectMultiple(attrs={'class': 'set-selected'})
	)
	nam_sinh = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'VD: 18', 'class' : 'form-control', 'id':'nam_sinh', 'autocomplete':'off'}))
	ket_thuc_nam_sinh = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'VD: 30', 'id':'ket_thuc_nam_sinh', 'class' : 'form-control', 'autocomplete':'off'}))
	trinh_do_hoc_van = forms.ChoiceField(choices=Conts.TRINH_DO_HOC_VAN_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	chuyen_nganh = forms.ChoiceField(choices=Conts.CHUYEN_NGANH_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	ngoai_ngu = forms.ChoiceField(choices=Conts.NGOAI_NGU_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	yeu_cau_hoc_tieng = forms.ChoiceField(choices=Conts.YEU_CAU_HOC_TIENG_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	tinh_trang_suc_khoe = forms.ChoiceField(choices=Conts.TINH_TRANG_SUC_KHOE_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	tay_nghe = forms.MultipleChoiceField(
		required=False,
		choices=[],
		widget=forms.CheckboxSelectMultiple(attrs={'class': 'set-selected'})
	)
	thi_luc = forms.ChoiceField(choices=Conts.THI_LUC_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	viem_gan_b = forms.ChoiceField(choices=Conts.VIEM_GAN_B_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	xam_hinh = forms.ChoiceField(choices=Conts.XAM_HINH_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	yeu_cau_khac = forms.CharField(
		required=False, 
		widget=forms.Textarea(attrs={'rows': 6, 'class': 'form-control', 'placeholder': 'Yêu cầu khác', 'autocomplete':'off'})
	)
	hinh_thuc_thi_tuyen = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Hình thức thi tuyển', 'class' : 'form-control', 'autocomplete':'off'}))
	ngay_thi_tuyen = forms.DateField(
		required=False,
		input_formats=["%d-%m-%Y", "%Y-%m-%d"],
		widget=forms.DateInput(attrs={'placeholder': 'DD-MM-YYYY', 'class': 'form-control', 'id': 'depart', 'autocomplete':'off'})
	)
	han_dang_ky = forms.DateField(
		required=False,
		input_formats=["%d-%m-%Y", "%Y-%m-%d"],
		widget=forms.DateInput(attrs={'placeholder': 'DD-MM-YYYY', 'class': 'form-control', 'id': 'retur', 'autocomplete':'off'})
	)
	du_kien_xuat_canh = forms.CharField(
		required=False,
		widget=forms.TextInput(attrs={'class': 'form-select set-selected'})
	)
	noi_dung_chi_tiet = forms.CharField(
		required=False, 
		widget=forms.Textarea(attrs={'rows': 10, 'class': 'form-control', 'id':'editor', 'placeholder': 'Nội dung chi tiết'})
	)
	image = forms.FileField(
		required=False,
		widget=forms.ClearableFileInput(attrs={'id': 'file-input-media', 'class': 'd-none'})
	)
	is_confirmed = forms.BooleanField(required=True, label="Tôi cam kết thông tin đúng sự thật")

	def __init__(self, *args, **kwargs):
		work = kwargs.pop('work', None)
		countries = kwargs.pop('countries', [])
		profess = kwargs.pop('profess', [])
		cities = kwargs.pop('cities', [])
		genders = kwargs.pop('genders', [])
		workmanships = kwargs.pop('workmanships', [])
		provinces = kwargs.pop('provinces', [])
		super(EditForm, self).__init__(*args, **kwargs)
		if work:
			current_year = datetime.now().year
			self.fields['name'].initial = work.name
			self.fields['country'].choices = [(str(c['id']), c['name']) for c in countries]
			if work and work.country:
				self.fields['country'].initial = str(work.country.id)

			self.fields['province'].choices = [(str(c['id']), c['name']) for c in provinces]
			if work and work.province:
				self.fields['province'].initial = str(work.province.id)

			self.fields['cong_ty_nghiep_doan'].initial = work.cong_ty_nghiep_doan
			self.fields['nganh_nghe'].choices = [(str(c['id']), c['name']) for c in profess]
			if work and work.nganh_nghe:
				self.fields['nganh_nghe'].initial = [str(c.id) for c in work.nganh_nghe.all()]
			self.fields['cong_viec_cu_the'].initial = work.cong_viec_cu_the
			self.fields['noi_thi_tuyen'].choices = [(str(c['id']), c['name']) for c in cities]
			if work and work.noi_thi_tuyen:
				self.fields['noi_thi_tuyen'].initial = [str(c.id) for c in work.noi_thi_tuyen.all()]
			self.fields['thoi_gian_lam_viec'].initial = work.thoi_gian_lam_viec
			self.fields['luong_co_ban'].initial = work.luong_co_ban
			self.fields['luong_co_ban_menh_gia'].initial = work.luong_co_ban_menh_gia
			self.fields['lam_them'].initial = work.lam_them
			self.fields['thu_nhap_du_kien'].initial = work.thu_nhap_du_kien
			self.fields['thu_nhap_du_kien_menh_gia'].initial = work.thu_nhap_du_kien_menh_gia
			self.fields['quyen_loi_khac'].initial = work.quyen_loi_khac
			self.fields['so_luong_tuyen'].initial = work.so_luong_tuyen
			self.fields['hop_dong'].initial = work.hop_dong
			self.fields['phi_xuat_canh'].initial = work.phi_xuat_canh
			self.fields['phi_xuat_canh_menh_gia'].initial = work.phi_xuat_canh_menh_gia
			self.fields['chuong_trinh_ho_tro'].initial = work.chuong_trinh_ho_tro
			self.fields['gioi_tinh'].choices = [(str(c['id']), c['name']) for c in genders]
			if work and work.gioi_tinh:
				self.fields['gioi_tinh'].initial = [str(c.id) for c in work.gioi_tinh.all()]
			if work.nam_sinh:
				self.fields['nam_sinh'].initial = current_year - int(work.nam_sinh)

			if work.ket_thuc_nam_sinh:
				self.fields['ket_thuc_nam_sinh'].initial = current_year - int(work.ket_thuc_nam_sinh)

			self.fields['trinh_do_hoc_van'].initial = work.trinh_do_hoc_van
			self.fields['chuyen_nganh'].initial = work.chuyen_nganh
			self.fields['ngoai_ngu'].initial = work.ngoai_ngu
			self.fields['yeu_cau_hoc_tieng'].initial = work.yeu_cau_hoc_tieng
			self.fields['tinh_trang_suc_khoe'].initial = work.tinh_trang_suc_khoe
			self.fields['tay_nghe'].choices = [(str(c['id']), c['name']) for c in workmanships]
			if work and work.tay_nghe:
				self.fields['tay_nghe'].initial = [str(c.id) for c in work.tay_nghe.all()]
			self.fields['thi_luc'].initial = work.thi_luc
			self.fields['viem_gan_b'].initial = work.viem_gan_b
			self.fields['xam_hinh'].initial = work.xam_hinh
			self.fields['yeu_cau_khac'].initial = work.yeu_cau_khac
			self.fields['hinh_thuc_thi_tuyen'].initial = work.hinh_thuc_thi_tuyen
			self.fields['ngay_thi_tuyen'].initial = work.ngay_thi_tuyen.strftime("%d-%m-%Y") if work.ngay_thi_tuyen else ""
			self.fields['han_dang_ky'].initial = work.han_dang_ky.strftime("%d-%m-%Y") if work.han_dang_ky else ""
			self.fields['du_kien_xuat_canh'].initial = work.du_kien_xuat_canh
			self.fields['noi_dung_chi_tiet'].initial = work.noi_dung_chi_tiet
			self.fields['is_confirmed'].initial = work.is_confirmed	
