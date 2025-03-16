from django import forms
from django.utils.html import strip_tags
from utils.conts import Conts

class TuVanForm(forms.Form):
	name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Nhập họ tên (*)', 'class' : 'form-control',  'id': 'advisory_name', 'autocomplete':'off'}))
	phone = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Số điện thoại (*)', 'class' : 'form-control', 'id': 'advisory_phone', 'autocomplete':'off'}))


class UpdateUVForm(forms.Form):
	ho_va_ten_dem = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Họ và Tên đệm', 'class' : 'form-control',  'autocomplete':'off'}))
	ten_goi = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Tên gọi', 'class' : 'form-control', 'autocomplete':'off'}))
	avata = forms.FileField(
		required=False,
		widget=forms.ClearableFileInput(attrs={'id': 'file-input-media', 'class': 'd-none'})
	)
	gioi_tinh = forms.ChoiceField(
		choices=Conts.GIOI_TINH_CHOICES,
		required=False,
		widget=forms.Select(attrs={'class': 'form-select set-selected'})
	)
	nam_sinh = forms.IntegerField(
		required=True, 
		widget=forms.NumberInput(attrs={'class': 'form-control', 'autocomplete':'off', 'value': 0})
	)
	ghi_chu = forms.CharField(
		required=False, 
		widget=forms.Textarea(attrs={'rows': 6, 'class': 'form-control', 'placeholder': 'Ghi chú', 'autocomplete':'off'})
	)
	phone = forms.CharField(
		required=False, 
		widget=forms.TextInput(attrs={'placeholder': 'Số điện thoại', 'class': 'form-control', 'autocomplete':'off'})
	)
	zalo = forms.CharField(
		required=False, 
		widget=forms.TextInput(attrs={'placeholder': 'Số Zalo', 'class': 'form-control', 'autocomplete':'off'})
	)
	facebook = forms.CharField(
		required=False, 
		widget=forms.TextInput(attrs={'placeholder': 'Facebook', 'class': 'form-control', 'autocomplete':'off'})
	)
	dia_chi = forms.CharField(
		required=False, 
		widget=forms.TextInput(attrs={'placeholder': 'Địa chỉ', 'class': 'form-control', 'autocomplete':'off'})
	)
	tinh_thanh_pho = forms.ChoiceField(
		required=False,
		choices=[],
		widget=forms.Select(attrs={'class': 'form-select set-selected'})
	)
	country = forms.MultipleChoiceField(
		required=False,
		choices=[],
		widget=forms.CheckboxSelectMultiple(attrs={'class': 'set-selected'})
	)

	nganh_nghe = forms.MultipleChoiceField(
		required=False,
		choices=[],
		widget=forms.CheckboxSelectMultiple(attrs={'class': 'set-selected'})
	)
	
	tot_nghiep = forms.ChoiceField(choices=Conts.TRINH_DO_HOC_VAN_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	ngoai_ngu = forms.ChoiceField(choices=Conts.NGOAI_NGU_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	bang_nghe = forms.ChoiceField(choices=Conts.XAM_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	tay_nghe = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete':'off'}))
	da_di_xkld = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete':'off'}))
	chieu_cao = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'value': 0}))
	can_nang = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'value': 0}))
	thi_luc = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'value': 0}))
	hinh_xam = forms.ChoiceField(choices=Conts.XAM_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	viem_gan_b = forms.ChoiceField(choices=Conts.XAM_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	hut_thuoc = forms.ChoiceField(choices=Conts.XAM_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	uong_ruou = forms.ChoiceField(choices=Conts.XAM_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	benh_di_truyen = forms.ChoiceField(choices=Conts.XAM_CHOICES, widget=forms.Select(attrs={'class': 'form-select set-selected'}))
	tinh_cach = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete':'off'}))
	so_thich = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete':'off'}))
	yeu_cau_khac = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete':'off'}))



	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user', None)
		cities = kwargs.pop('cities', [])
		countries = kwargs.pop('countries', [])
		profess = kwargs.pop('profess', [])
		super(UpdateUVForm, self).__init__(*args, **kwargs)

		if user:
			self.fields['ho_va_ten_dem'].initial = user.ho_va_ten_dem
			self.fields['ten_goi'].initial = user.ten_goi
			self.fields['gioi_tinh'].initial = user.gioi_tinh
			self.fields['nam_sinh'].initial = user.nam_sinh
			self.fields['ghi_chu'].initial = strip_tags(user.ghi_chu) if user.ghi_chu else ""
			self.fields['phone'].initial = user.phone if user.phone else user.username
			self.fields['zalo'].initial = user.zalo
			self.fields['facebook'].initial = user.facebook
			self.fields['dia_chi'].initial = user.dia_chi
			self.fields['avata'].initial = user.avata

			self.fields['tot_nghiep'].initial = user.tot_nghiep
			self.fields['ngoai_ngu'].initial = user.ngoai_ngu
			self.fields['bang_nghe'].initial = user.bang_nghe
			self.fields['tay_nghe'].initial = user.tay_nghe
			self.fields['da_di_xkld'].initial = user.da_di_xkld
			self.fields['chieu_cao'].initial = user.chieu_cao
			self.fields['can_nang'].initial = user.can_nang
			self.fields['thi_luc'].initial = user.thi_luc
			self.fields['hinh_xam'].initial = user.hinh_xam
			self.fields['viem_gan_b'].initial = user.viem_gan_b
			self.fields['hut_thuoc'].initial = user.hut_thuoc
			self.fields['uong_ruou'].initial = user.uong_ruou
			self.fields['benh_di_truyen'].initial = user.benh_di_truyen
			self.fields['tinh_cach'].initial = user.tinh_cach
			self.fields['so_thich'].initial = user.so_thich
			self.fields['yeu_cau_khac'].initial = user.yeu_cau_khac

		self.fields['tinh_thanh_pho'].choices = [("", "Vui lòng chọn")] +[(str(c["id"]), c["name"]) for c in cities]
		if user and user.tinh_thanh_pho:
			self.fields['tinh_thanh_pho'].initial = user.tinh_thanh_pho.id

		self.fields['country'].choices = [(c["id"], c["name"]) for c in countries]
		if user and user.country:
			self.fields['country'].initial = [str(c.id) for c in user.country.all()]

		self.fields['nganh_nghe'].choices = [(p["id"], p["name"]) for p in profess]
		if user and user.nganh_nghe:
			self.fields['nganh_nghe'].initial = [str(c.id) for c in user.nganh_nghe.all()]



class UpdateNTDForm(forms.Form):
	ho_va_ten_dem = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Họ và Tên đệm', 'class' : 'form-control',  'autocomplete':'off'}))
	ten_goi = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Tên gọi', 'class' : 'form-control', 'autocomplete':'off'}))			
	tu_van = forms.CharField(
		required=False, 
		widget=forms.Textarea(attrs={'rows': 6, 'class': 'form-control', 'placeholder': 'Giới thiệu ngắn'})
	)
	phone = forms.CharField(
		required=False, 
		widget=forms.TextInput(attrs={'placeholder': 'Số điện thoại', 'class': 'form-control', 'autocomplete':'off'})
	)
	zalo = forms.CharField(
		required=False, 
		widget=forms.TextInput(attrs={'placeholder': 'Số Zalo', 'class': 'form-control', 'autocomplete':'off'})
	)
	avata = forms.FileField(
	required=False,
	widget=forms.ClearableFileInput(attrs={'id': 'file-input-media', 'class': 'd-none'})
	)
	anh_bia = forms.FileField(
	required=False,
	widget=forms.ClearableFileInput(attrs={'id': 'file-input-media', 'class': 'd-none'})
	)
	facebook = forms.CharField(
		required=False, 
		widget=forms.TextInput(attrs={'placeholder': 'Facebook', 'class': 'form-control', 'autocomplete':'off'})
	)

	gioi_tinh = forms.ChoiceField(
		choices=[('', 'Vui lòng chọn'), ('Nam', 'Nam'), ('Nữ', 'Nữ')],
		required=False,
		widget=forms.Select(attrs={'class': 'form-select set-selected'})
	)
	nam_sinh = forms.IntegerField(
		required=False, 
		widget=forms.NumberInput(attrs={'class': 'form-control', 'autocomplete':'off', 'value': 0})
	)
	
	sinh_song_tai = forms.CharField(
		required=False, 
		widget=forms.TextInput(attrs={'placeholder': 'Sinh sống tại', 'class': 'form-control'})
	)

	noi_lam_viec = forms.CharField(
		required=False, 
		widget=forms.TextInput(attrs={'placeholder': 'Nơi làm việc', 'class': 'form-control'})
	)

	ten_viet_tat = forms.CharField(
		required=False, 
		widget=forms.TextInput(attrs={'placeholder': 'Tên viết tắt', 'class': 'form-control'})
	)

	dia_chi = forms.CharField(
		required=False, 
		widget=forms.TextInput(attrs={'placeholder': 'Địa chỉ', 'class': 'form-control'})
	)
	chuc_vu = forms.CharField(
		required=False, 
		widget=forms.TextInput(attrs={'placeholder': 'Chức vụ', 'class': 'form-control'})
	)

	kinh_nghiem = forms.CharField(
		required=False, 
		widget=forms.TextInput(attrs={'placeholder': 'Kinh nghiệm', 'class': 'form-control'})
	)
	ghi_chu = forms.CharField(
		required=False, 
		widget=forms.Textarea(attrs={'rows': 10, 'class': 'form-control', 'id':'editor', 'placeholder': 'Ghi chú'})
	)
	

	def __init__(self, *args, **kwargs):
		user = kwargs.pop('user', None)
		super(UpdateNTDForm, self).__init__(*args, **kwargs)

		if user:
			self.fields['ho_va_ten_dem'].initial = user.ho_va_ten_dem
			self.fields['ten_goi'].initial = user.ten_goi
			self.fields['tu_van'].initial = strip_tags(user.tu_van) if user.ghi_chu else ""
			self.fields['phone'].initial = user.phone if user.phone else user.username
			self.fields['zalo'].initial = user.zalo
			self.fields['facebook'].initial = user.facebook
			self.fields['gioi_tinh'].initial = user.gioi_tinh
			self.fields['nam_sinh'].initial = user.nam_sinh
			self.fields['sinh_song_tai'].initial = user.sinh_song_tai
			self.fields['noi_lam_viec'].initial = user.noi_lam_viec
			self.fields['ten_viet_tat'].initial = user.ten_viet_tat
			self.fields['dia_chi'].initial = user.dia_chi
			self.fields['chuc_vu'].initial = user.chuc_vu
			self.fields['kinh_nghiem'].initial = user.kinh_nghiem
			self.fields['avata'].initial = user.avata
			self.fields['ghi_chu'].initial = strip_tags(user.ghi_chu) if user.ghi_chu else ""
