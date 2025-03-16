from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse, HttpResponsePermanentRedirect
from django.core.cache import cache
import requests
from datetime import datetime, timedelta, date
from django.db import transaction
from django.utils import timezone
import json
from .models import *
from city.models import Country, City, Province
from profession.models import Profession
from work.models import Work, Gender, Workmanship, Price
from collections import defaultdict
from page.pagination import paginate
from django.contrib.auth.decorators import login_required
from page.forms import UpdateUVForm, UpdateNTDForm
from django.utils.text import slugify
from django.contrib import messages
from user.forms import ADDForm, EditForm
from page.check_url import is_valid_url, generate_month_choices
from django.db.models import Count, Prefetch
from django.core.paginator import Paginator
from django.shortcuts import render

PAGE_NUMBER = 30
PAGE_list_job = 20




def ungvien(request, id):
	uv = get_object_or_404(CustomUser, pk=id)
	is_japan = uv.country.filter(name__icontains="Nhật").exists()
	cost = 80000 if is_japan else 20000
	employer = request.user if request.user.is_authenticated else None
	has_enough_points = employer.point >= cost if employer and employer.role == 'employer' else False
	countries = CustomUser.objects.filter(id = uv.id).values('country__name').order_by("id")
	profess = CustomUser.objects.filter(id = uv.id).values('nganh_nghe__name').order_by("id")
	return render(request, 'ungvien/ungvien.html',{'uv':uv, 'countries':countries, 'profess':profess,'cost': cost,
		'is_japan': is_japan,
		'has_enough_points': has_enough_points
	})


def nhatuyendung(request, id, page=1):
	nhatuyendung = get_object_or_404(CustomUser, pk=id)
	if nhatuyendung.facebook and not is_valid_url(nhatuyendung.facebook):
		nhatuyendung.facebook = None
	total = Work.actives.filter(user__id = nhatuyendung.id).all().count()
	paginator = paginate(page, total,PAGE_NUMBER)
	start_index = paginator.number
	path_url = "/hosotuyendung/{0}".format(nhatuyendung.id)
	works = Work.actives.filter(user_id= nhatuyendung.id).select_related('country', 'user').values(
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
	return render(request, 'nhatuyendung/index.html',{'path_url':path_url, 'nhatuyendung':nhatuyendung, 'works':works, 'paginator':paginator, 'page':page})	



@login_required
def updateungvien(request):
	user = request.user
	countries = Country.actives.values('id','name').order_by('-priority')
	profess = Profession.actives.values('id','name').order_by('-priority')
	cities = City.actives.values('id','name').order_by('-priority')
	genders = Gender.objects.values('id', 'name').order_by('-id')
	current_year = datetime.now().year
	min_year = current_year - 18
	years = range(min_year, 1972, -1)
	if request.method == "POST":
		form = UpdateUVForm(request.POST, request.FILES, user=user, cities=cities, countries=countries, profess=profess)
		if form.is_valid():
			user.ho_va_ten_dem=form.cleaned_data['ho_va_ten_dem']
			user.ten_goi=form.cleaned_data['ten_goi']
			user.gioi_tinh=form.cleaned_data['gioi_tinh']
			user.nam_sinh=form.cleaned_data['nam_sinh']
			user.ghi_chu=form.cleaned_data['ghi_chu']
			user.phone=form.cleaned_data['phone']
			user.zalo=form.cleaned_data['zalo']
			user.avata=form.cleaned_data['avata']
			user.facebook=form.cleaned_data['facebook']
			user.dia_chi=form.cleaned_data['dia_chi']
			user.tot_nghiep=form.cleaned_data['tot_nghiep']
			user.ngoai_ngu=form.cleaned_data['ngoai_ngu']
			user.bang_nghe=form.cleaned_data['bang_nghe']
			user.tay_nghe=form.cleaned_data['tay_nghe']
			user.da_di_xkld=form.cleaned_data['da_di_xkld']
			user.chieu_cao=form.cleaned_data['chieu_cao']
			user.can_nang=form.cleaned_data['can_nang']
			user.thi_luc=form.cleaned_data['thi_luc']
			user.hinh_xam=form.cleaned_data['hinh_xam']
			user.viem_gan_b=form.cleaned_data['viem_gan_b']
			user.hut_thuoc=form.cleaned_data['hut_thuoc']
			user.uong_ruou=form.cleaned_data['uong_ruou']
			user.benh_di_truyen=form.cleaned_data['benh_di_truyen']
			user.tinh_cach=form.cleaned_data['tinh_cach']
			user.so_thich=form.cleaned_data['so_thich']
			user.yeu_cau_khac=form.cleaned_data['yeu_cau_khac']
			tinh_thanh_pho = form.cleaned_data.get('tinh_thanh_pho')
			user.tinh_thanh_pho = City.objects.get(id=tinh_thanh_pho) if tinh_thanh_pho else None
			country_selected = form.cleaned_data.get('country', [])
			nganh_nghe_selected = form.cleaned_data.get('nganh_nghe', [])
			user.country.set(Country.objects.filter(id__in=country_selected))
			user.nganh_nghe.set(Profession.objects.filter(id__in=nganh_nghe_selected))
			user.save()
			return JsonResponse({"success": True})
		else:
			return JsonResponse({"success": False, "errors": form.errors})
	else:
		form = UpdateUVForm(user=user, cities=cities, countries=countries, profess=profess)
	return render(request, 'ungvien/capnhatungvien.html',{'countries': countries, 'profess':profess, 'cities':cities, 'genders':genders,
	'years':years, 'user': user, 'form':form})



@login_required
def updatenhatuyendung(request):
	user = request.user
	if request.method == "POST":
		form = UpdateNTDForm(request.POST, request.FILES, user=user)
		if form.is_valid():
			user.ho_va_ten_dem = form.cleaned_data['ho_va_ten_dem']
			user.ten_goi = form.cleaned_data['ten_goi']
			user.tu_van = form.cleaned_data['tu_van']
			user.phone = form.cleaned_data['phone']
			user.zalo = form.cleaned_data['zalo']
			user.facebook = form.cleaned_data['facebook']
			user.gioi_tinh = form.cleaned_data['gioi_tinh']
			user.avata = form.cleaned_data['avata']
			user.nam_sinh = form.cleaned_data['nam_sinh']
			user.sinh_song_tai = form.cleaned_data['sinh_song_tai']
			user.noi_lam_viec = form.cleaned_data['noi_lam_viec']
			user.ten_viet_tat = form.cleaned_data['ten_viet_tat']
			user.dia_chi = form.cleaned_data['dia_chi']
			user.chuc_vu = form.cleaned_data['chuc_vu']
			user.kinh_nghiem = form.cleaned_data['kinh_nghiem']
			if 'anh_bia' in request.FILES:
				user.anh_bia = form.cleaned_data['anh_bia']
			user.ghi_chu = form.cleaned_data['ghi_chu']
			user.save()
			return JsonResponse({"success": True})
		else:
			return JsonResponse({"success": False, "errors": form.errors})
	else:
		form = UpdateNTDForm(user=user)
	return render(request, 'nhatuyendung/capnhatnhatuyendung.html', {'user': user, 'form': form})


def getProvinces(request):
	if request.method == "GET":
		country_id = request.GET.get("country_id", "")
		provinces = Province.objects.filter(country_id=country_id).values('id', 'name').order_by('-priority')
		province_list = {province['id']: province['name'] for province in provinces}
		return JsonResponse(province_list)


def add_job(request):
	user = request.user
	if not user.is_authenticated:
		return JsonResponse({"success": False, "message": "Bạn cần đăng nhập để đăng tin."})
	countries = Country.actives.values('id', 'name').order_by('-priority')
	profess = Profession.actives.values('id', 'name').order_by('-priority')
	cities = City.actives.values('id', 'name').order_by('-priority')
	genders = Gender.objects.values('id', 'name').order_by('-id')
	workmanships = Workmanship.objects.values('id', 'name').order_by('id')
	provinces = Province.objects.values('id', 'name').order_by('-priority')
	month_choices = generate_month_choices()
	form = ADDForm(countries=countries, provinces=provinces, profess=profess, cities=cities, genders=genders, workmanships=workmanships )  
	if request.method == 'POST':
		form = ADDForm(request.POST, request.FILES, countries=countries, provinces=provinces, profess=profess, cities=cities, genders=genders, workmanships=workmanships) 
		if form.is_valid():
			if user.free_posts_today > 0:
				user.free_posts_today -= 1
			elif user.point >= 10000:
				user.point -= 10000
			else:
				return JsonResponse({
				"success": False, 
				"message": "Bạn đã hết lượt đăng tin miễn phí và không đủ số dư!",
				"redirect_url": "/employers/add_fund"
				})
			data = form.cleaned_data
			work = Work(
				user=user,
				name=data['name'],
				country=Country.objects.get(id=int(data['country'])),
				province=Province.objects.get(id=int(data['province'])) if data['province'] else None,
				cong_ty_nghiep_doan=data['cong_ty_nghiep_doan'],
				cong_viec_cu_the=data['cong_viec_cu_the'],
				thoi_gian_lam_viec=data['thoi_gian_lam_viec'],
				luong_co_ban=data['luong_co_ban'],
				luong_co_ban_menh_gia=data['luong_co_ban_menh_gia'],
				lam_them=data['lam_them'],
				thu_nhap_du_kien=data['thu_nhap_du_kien'],
				thu_nhap_du_kien_menh_gia=data['thu_nhap_du_kien_menh_gia'],
				quyen_loi_khac=data['quyen_loi_khac'],
				so_luong_tuyen=data['so_luong_tuyen'],
				hop_dong=data['hop_dong'],
				phi_xuat_canh=data['phi_xuat_canh'],
				phi_xuat_canh_menh_gia=data['phi_xuat_canh_menh_gia'],
				chuong_trinh_ho_tro=data['chuong_trinh_ho_tro'],
				nam_sinh=data['nam_sinh'],
				ket_thuc_nam_sinh=data['ket_thuc_nam_sinh'],
				trinh_do_hoc_van=data['trinh_do_hoc_van'],
				chuyen_nganh=data['chuyen_nganh'],
				ngoai_ngu=data['ngoai_ngu'],
				yeu_cau_hoc_tieng=data['yeu_cau_hoc_tieng'],
				tinh_trang_suc_khoe=data['tinh_trang_suc_khoe'],
				thi_luc=data['thi_luc'],
				viem_gan_b=data['viem_gan_b'],
				xam_hinh=data['xam_hinh'],
				yeu_cau_khac=data['yeu_cau_khac'],
				hinh_thuc_thi_tuyen=data['hinh_thuc_thi_tuyen'],
				ngay_thi_tuyen=data.get('ngay_thi_tuyen'),
				han_dang_ky=data.get('han_dang_ky'),
				du_kien_xuat_canh=data.get('du_kien_xuat_canh'),
				noi_dung_chi_tiet=data['noi_dung_chi_tiet'],
				image=data.get('image', None),
				is_confirmed=data.get('is_confirmed', False)
			)
			work.save()
			nganh_nghe_selected = data.get('nganh_nghe', [])
			noi_thi_tuyen_selected = data.get('noi_thi_tuyen', [])
			gioi_tinh_selected = data.get('gioi_tinh', [])
			tay_nghe_selected = data.get('tay_nghe', [])
			work.nganh_nghe.set(Profession.objects.filter(id__in=nganh_nghe_selected))
			work.noi_thi_tuyen.set(City.objects.filter(id__in=noi_thi_tuyen_selected))
			work.gioi_tinh.set(Gender.objects.filter(id__in=gioi_tinh_selected))
			work.tay_nghe.set(Workmanship.objects.filter(id__in=tay_nghe_selected))
			user.save()
			return JsonResponse({
				"success": True, 
				"message": "Đăng tin thành công!",
				"redirect_url": "/employers/list_job"
				})
		else:
			return JsonResponse({"success": False, "errors": form.errors})

	return render(request, 'nhatuyendung/dangtin.html', {
		'countries': countries,
		'profess': profess,
		'cities': cities,
		'genders': genders,
		'form': form,
		'workmanships': workmanships,
		'month_choices': month_choices,
		'user': user
	})


def list_job(request, page= 1):
	user = request.user
	total = Work.actives.filter(user__id = user.id).all().count()
	paginator = paginate(page, total,PAGE_list_job)
	start_index = paginator.number
	path_url = "/employers/list_job"
	works = Work.actives.filter(user__id = user.id).values(
		'id', 'country__name', 'name', 'slug', 'country__slug','image', 'view', 'created', 'updated'
	).order_by('-id')[(start_index-1)*PAGE_list_job:start_index*PAGE_list_job]
	return render(request, 'nhatuyendung/list_job.html', {'works':works, 'paginator':paginator,
		'path_url':path_url, 'total':total})


def edit_job(request, id):
	user = request.user
	work = get_object_or_404(Work, id=id, user=user)
	countries = Country.actives.values('id', 'name').order_by('-priority')
	profess = Profession.actives.values('id', 'name').order_by('-priority')
	cities = City.actives.values('id', 'name').order_by('-priority')
	genders = Gender.objects.values('id', 'name').order_by('-id')
	workmanships = Workmanship.objects.values('id', 'name').order_by('id')
	provinces = Province.objects.values('id', 'name').order_by('-priority')
	month_choices = generate_month_choices()
	form = EditForm(work=work, countries=countries, provinces=provinces, profess=profess, cities=cities, genders=genders, workmanships=workmanships )  
	if request.method == 'POST':
		form = EditForm(request.POST, request.FILES, work=work, countries=countries, provinces=provinces, profess=profess, cities=cities, genders=genders, workmanships=workmanships) 
		if form.is_valid():
			data = form.cleaned_data
			work.name = data['name']
			work.country = Country.objects.get(id=int(data['country']))
			work.province = Province.objects.get(id=int(data['province'])) if data['province'] else None
			work.cong_ty_nghiep_doan = data['cong_ty_nghiep_doan']
			work.cong_viec_cu_the = data['cong_viec_cu_the']
			work.thoi_gian_lam_viec = data['thoi_gian_lam_viec']
			work.luong_co_ban = data['luong_co_ban']
			work.luong_co_ban_menh_gia = data['luong_co_ban_menh_gia']
			work.lam_them = data['lam_them']
			work.thu_nhap_du_kien = data['thu_nhap_du_kien']
			work.thu_nhap_du_kien_menh_gia = data['thu_nhap_du_kien_menh_gia']
			work.quyen_loi_khac = data['quyen_loi_khac']
			work.so_luong_tuyen = data['so_luong_tuyen']
			work.hop_dong = data['hop_dong']
			work.phi_xuat_canh = data['phi_xuat_canh']
			work.phi_xuat_canh_menh_gia = data['phi_xuat_canh_menh_gia']
			work.chuong_trinh_ho_tro = data['chuong_trinh_ho_tro']
			work.nam_sinh = data['nam_sinh']
			work.ket_thuc_nam_sinh = data['ket_thuc_nam_sinh']
			work.trinh_do_hoc_van = data['trinh_do_hoc_van']
			work.chuyen_nganh = data['chuyen_nganh']
			work.ngoai_ngu = data['ngoai_ngu']
			work.yeu_cau_hoc_tieng = data['yeu_cau_hoc_tieng']
			work.tinh_trang_suc_khoe = data['tinh_trang_suc_khoe']
			work.thi_luc = data['thi_luc']
			work.viem_gan_b = data['viem_gan_b']
			work.xam_hinh = data['xam_hinh']
			work.yeu_cau_khac = data['yeu_cau_khac']
			work.hinh_thuc_thi_tuyen = data['hinh_thuc_thi_tuyen']
			work.ngay_thi_tuyen = data.get('ngay_thi_tuyen')
			work.han_dang_ky = data.get('han_dang_ky')
			work.du_kien_xuat_canh = data.get('du_kien_xuat_canh')
			work.noi_dung_chi_tiet = data['noi_dung_chi_tiet']
			if 'image' in request.FILES:
				work.image = form.cleaned_data['image']
			work.is_confirmed = data.get('is_confirmed', False)
			work.save()
			work.nganh_nghe.set(data.get('nganh_nghe', []))
			work.noi_thi_tuyen.set(data.get('noi_thi_tuyen', []))
			work.gioi_tinh.set(data.get('gioi_tinh', []))
			work.tay_nghe.set(data.get('tay_nghe', []))
			return JsonResponse({
				"success": True,
				"message": "Sửa tin thành công!",
				"redirect_url": "/employers/list_job"
			})
		else:
			return JsonResponse({"success": False, "errors": form.errors})

	return render(request, 'nhatuyendung/edit_job.html', {
		'countries': countries,
		'profess': profess,
		'cities': cities,
		'genders': genders,
		'form': form,
		'workmanships': workmanships,
		'month_choices': month_choices,
		'user': user,
		'work':work
	})	

@csrf_exempt
def remove_job(request, id):
    if request.method == "POST":
        user = request.user  
        work = get_object_or_404(Work, id=id, user=user)  
        work.delete()  
        return JsonResponse({"success": True, "message": "Xóa tin thành công!"})

    return JsonResponse({"success": False, "message": "Yêu cầu không hợp lệ!"})


@login_required
def up_tin(request):
    job_id = request.GET.get("id")
    if not job_id:
        return JsonResponse({"success": False, "message": "Thiếu ID tin cần up!"}, status=400)
    user = request.user
    work = get_object_or_404(Work, id=job_id, user=user)
    up_point = 10000
    profile = get_object_or_404(CustomUser, id=user.id)
    if profile.point < up_point:
        return JsonResponse({
            "success": False,
            "message": "Số dư không đủ! Hãy nạp tiền.",
            "redirect_url": "/employers/add_fund"
        })
    try:
        with transaction.atomic():
            profile.point -= up_point
            profile.save()
            work.updated = timezone.now()
            work.save()
        return JsonResponse({"success": True, "message": "Up tin thành công!"})
    except Exception as e:
        return JsonResponse({"success": False, "message": f"Lỗi: {str(e)}"}, status=500)


@login_required
def set_hot_tin(request):
    Work.objects.filter(hot_expiry__gt=timezone.now())
    job_id = request.GET.get("id")
    if not job_id:
        return JsonResponse({"success": False, "message": "Thiếu ID tin cần nâng HOT!"}, status=400)

    user = request.user
    work = get_object_or_404(Work, id=job_id, user=user)
    hot_price_per_day = 100000
    profile = get_object_or_404(CustomUser, id=user.id)

    if profile.point < hot_price_per_day:
        return JsonResponse({
            "success": False,
            "message": "Số dư không đủ! Hãy nạp tiền.",
            "redirect_url": "/employers/add_fund"
        })

    try:
        with transaction.atomic():
            profile.point -= hot_price_per_day 
            profile.save()
            work.hot = True
            work.hot_expiry = timezone.now() + timezone.timedelta(days=1)
            work.save()
        return JsonResponse({"success": True, "message": "Tin đã được nâng thành HOT!"})
    except Exception as e:
        return JsonResponse({"success": False, "message": f"Lỗi: {str(e)}"}, status=500)


def expired_job(request, page= 1):
	today = timezone.now().date()
	user = request.user
	total = Work.actives.filter(han_dang_ky__lt=today, user__id = user.id).all().count()
	paginator = paginate(page, total,PAGE_list_job)
	start_index = paginator.number
	path_url = "/employers/expired_job"
	works = Work.actives.filter(han_dang_ky__lt=today, user__id = user.id).values(
		'id', 'country__name', 'name', 'slug', 'country__slug','image', 'view', 'created', 'updated'
	).order_by('-id')[(start_index-1)*PAGE_list_job:start_index*PAGE_list_job]
	return render(request, 'nhatuyendung/expired_job.html', {'works':works, 'paginator':paginator,
		'path_url':path_url, 'total':total})


def add_fund(request):
	user = request.user
	prices = Price.actives.values('id','price').order_by('-priority')
	return render(request, 'nhatuyendung/add_fund.html', {'prices':prices, 'user':user})


def candidate_search(request):
	employer = request.user 
	viewed_candidates = CandidateView.objects.filter(employer=employer).values_list("candidate_id", flat=True)
	candidates = CustomUser.objects.filter(role="applicant").order_by('-id')
	gender = request.GET.get("gioi_tinh", "")
	if gender and gender != "Giới tính":
		candidates = candidates.filter(gioi_tinh=gender)
	nam_sinh = request.GET.get("nam_sinh", "")
	if nam_sinh and nam_sinh.isdigit():
		candidates = candidates.filter(nam_sinh=nam_sinh)
	tinh_thanh_pho = request.GET.get("tinh_thanh_pho", "")
	if tinh_thanh_pho and tinh_thanh_pho.isdigit():
		candidates = candidates.filter(tinh_thanh_pho_id=tinh_thanh_pho)
	country_id = request.GET.getlist("quoc_gia")
	country_id = [q for q in country_id if q.isdigit()]
	if country_id:
		candidates = candidates.filter(country__id__in=country_id)
	nganh_nghe = request.GET.getlist("nganh_nghe")
	nganh_nghe = [n for n in nganh_nghe if n.isdigit()]
	if nganh_nghe:
		candidates = candidates.filter(nganh_nghe__id__in=nganh_nghe)
	paginator = Paginator(candidates, 30)
	page = request.GET.get('page')
	paginated_candidates = paginator.get_page(page)
	return render(request, 'nhatuyendung/candidate_list.html', {
		'candidates': paginated_candidates,
		'viewed_candidates':viewed_candidates,
		'gender': gender,
		'nam_sinh': nam_sinh,
		'tinh_thanh_pho': tinh_thanh_pho,
		'quoc_gia': country_id,
		'nganh_nghe': nganh_nghe,
	})


def view_candidate(request):
    if request.method == "POST":
        employer = request.user
        candidate_id = request.POST.get("uv_id")
        candidate = get_object_or_404(CustomUser, id=candidate_id)
        is_japan = candidate.country.filter(name__icontains="Nhật").exists()
        cost = 80000 if is_japan else 20000
        if employer.point < cost:
            return JsonResponse({"success": False, "message": "Bạn không đủ điểm để xem thông tin ứng viên. Hãy nạp thêm điểm!"}, status=400)
        employer.point -= cost
        employer.save()
        CandidateView.objects.get_or_create(employer=employer, candidate=candidate)
        
        return JsonResponse({
            "success": True,
            "phone": candidate.username,
            "zalo": candidate.zalo,
            "facebook": candidate.facebook
        })
    return JsonResponse({"success": False, "message": "Yêu cầu không hợp lệ."}, status=400)  


def candidate_saved(request):
    employer = request.user
    viewed_candidates = CandidateView.objects.filter(employer=employer).select_related("candidate")
    candidates = CustomUser.objects.filter(id__in=viewed_candidates.values_list("candidate_id", flat=True)).order_by('-id')
    gender = request.GET.get("gioi_tinh", "")
    if gender and gender != "Giới tính":
        candidates = candidates.filter(gioi_tinh=gender)
    nam_sinh = request.GET.get("nam_sinh", "")
    if nam_sinh.isdigit():
        candidates = candidates.filter(nam_sinh=nam_sinh)
    tinh_thanh_pho = request.GET.get("tinh_thanh_pho", "")
    if tinh_thanh_pho.isdigit():
        candidates = candidates.filter(tinh_thanh_pho_id=tinh_thanh_pho)
    country_id = request.GET.getlist("quoc_gia")
    country_id = [q for q in country_id if q.isdigit()]
    if country_id:
        candidates = candidates.filter(country__id__in=country_id)
    nganh_nghe = request.GET.getlist("nganh_nghe")
    nganh_nghe = [n for n in nganh_nghe if n.isdigit()]
    if nganh_nghe:
        candidates = candidates.filter(nganh_nghe__id__in=nganh_nghe)
    paginator = Paginator(candidates, 30)
    page = request.GET.get("page")
    paginated_candidates = paginator.get_page(page)

    return render(request, "nhatuyendung/candidate_saved.html", {
        "candidates": paginated_candidates
    })


def candidate_recruitment(request):
	user = request.user
	works = Work.objects.filter(user=user)
	candidates = Advisory.objects.filter(work__in=works).select_related("work")
	paginator = Paginator(candidates, 30)
	page = request.GET.get("page")
	paginated_candidates = paginator.get_page(page)
	if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
		return JsonResponse({"balance": user.point})
	return render(request, "nhatuyendung/candidate_recruitment.html", {'candidates':paginated_candidates})



from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def confirm_payment(request, candidate_id):
    if request.method == "POST":
        user = request.user
        data = json.loads(request.body)
        price = data.get("price")
        if user.point >= price:
            user.point -= price 
            user.save()
            candidate = Advisory.objects.get(id=candidate_id)
            candidate.is_paid = True
            candidate.save()

            return JsonResponse({"success": True, "new_balance": user.point})
        else:
            return JsonResponse({"success": False, "error": "Số dư không đủ."})

    return JsonResponse({"success": False, "error": "Yêu cầu không hợp lệ."})
