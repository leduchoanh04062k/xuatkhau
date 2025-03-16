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
from django.contrib.postgres.search import SearchQuery
from work.models import Work, Image
from city.models import Country, City
from profession.models import Profession
from collections import defaultdict
from django.db.models import Count
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from .pagination import paginate
from django.db.models import Q
from unidecode import unidecode
from user.models import Advisory
from django.utils.timezone import now
from user.models import CustomUser
from django.utils.timezone import timedelta
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from page.check_url import is_valid_url, is_valid_phone, generate_otp

PAGE_NUMBER = 30


def home(request, page=1):
    total = Work.actives.all().count()
    paginator = paginate(page, total,PAGE_NUMBER)
    start_index = paginator.number
    works = Work.actives.select_related('country', 'user').values(
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
    print        
    return render(request, 'home/home.html',{'works':works, 'paginator':paginator, 'page':page})


def search(request):
    keywork = request.GET.get('q', '').strip().lower()
    keywork_no_accent = unidecode(keywork)
    where = (
        Q(country__name__icontains=keywork) |
        Q(country__name__icontains=keywork_no_accent) |
        Q(country__slug__icontains=keywork) |
        Q(country__slug__icontains=keywork_no_accent) |
        Q(name__icontains=keywork) |
        Q(name__icontains=keywork_no_accent) |
        Q(slug__icontains=keywork) |
        Q(slug__icontains=keywork_no_accent)
    )

    country_names = [c.strip() for c in request.GET.getlist("quoc_gia") if c.strip()]
    profession_names = [p.strip() for p in request.GET.getlist("nganh_nghe") if p.strip()]
    city_names = [c.strip() for c in request.GET.getlist("noi_tuyen") if c.strip()]
    genders = [g.strip() for g in request.GET.getlist("gioi_tinh") if g.strip()]
    thi_luc_names = [g.strip() for g in request.GET.getlist("thi_luc") if g.strip()]
    viem_gan_names = [g.strip() for g in request.GET.getlist("viem_gan_b") if g.strip()]
    xam_hinh_names = [g.strip() for g in request.GET.getlist("xam_hinh") if g.strip()]
    birth_years = [y.strip() for y in request.GET.getlist("nam_sinh") if y.strip().isdigit()]
    birth_years = [int(year) for year in birth_years]
    if country_names:
        where &= Q(country__name__in=country_names)
    if profession_names:
        where &= Q(nganh_nghe__name__in=profession_names)
    if city_names:
        where &= Q(noi_thi_tuyen__name__in=city_names)
    if genders:
        where &= Q(gioi_tinh__name__in=genders)
    if thi_luc_names:
        where &= Q(thi_luc__in=thi_luc_names)  
    if viem_gan_names:
        where &= Q(viem_gan_b__in=viem_gan_names)  
    if xam_hinh_names:
        where &= Q(xam_hinh__in=xam_hinh_names)         
    if birth_years:
        where &= Q(nam_sinh__lte=max(birth_years), ket_thuc_nam_sinh__gte=min(birth_years))

    works = Work.actives.filter(where).values(
        'id', 
        'country__name', 'country__image', 'country__slug',
        'name', 'slug', 'image', 'luong_co_ban', 'luong_co_ban_menh_gia',
        'nam_sinh', 'ket_thuc_nam_sinh',
        'user__avata', 'user__id', 'user__ho_va_ten_dem', 'user__phone',
        'user__facebook', 'user__zalo', 'view', 'ngay_thi_tuyen',
        'user__ten_goi'
    ).order_by('-id')

    require_gioi_tinh_map = defaultdict(list)
    for work in Work.actives.prefetch_related('gioi_tinh'):
        for gioi_tinh in work.gioi_tinh.all():
            require_gioi_tinh_map[work.id].append(gioi_tinh.name)

    for work in works:
        work['gioi_tinh'] = require_gioi_tinh_map.get(work['id'], [])

        fb_link = work.get('user__facebook', '')
        if not fb_link or not is_valid_url(fb_link):
            work['user__facebook'] = None 

    page_number = request.GET.get('page', 1)
    paginator = Paginator(works, PAGE_NUMBER)

    try:
        data = paginator.get_page(int(page_number))
    except (EmptyPage, InvalidPage):
        data = paginator.get_page(1)

    return render(request, 'home/search.html', {'data': data})

@csrf_exempt
def ajaxAdvisory(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        work_id = request.POST.get("work_id")
        if name and phone:
            Advisory.objects.create(
                name=name,
                phone=phone,
                work_id=work_id
            )
            return JsonResponse({"status": "OK"})
        else:
            return JsonResponse({"status": "Error", "message": "Thiếu thông tin!"})
    return JsonResponse({"status": "Error", "message": "Phương thức không hợp lệ!"})

def detailPage(request, slug_page):
    page = get_object_or_404(Page, slug=slug_page)
    pages = Page.actives.values('name', 'slug').order_by('name')
    return render(request, 'page/page.html', {'page':page, 'pages':pages})       



def detailWork(request, slug, slug_work, page = 1 ):
    country = get_object_or_404(Country, slug=slug)
    work = get_object_or_404(Work, slug=slug_work, country_id = country.id)
    fb_link = getattr(work.user, "facebook", "") or ""
    workfacebook = is_valid_url(fb_link)
    path_url = "/{0}/{1}.html".format(country.slug, work.slug)  
    work.view += 1
    work.save()
    total = Work.actives.filter(country_id = country.id).all().exclude(id=work.id).count()
    paginator = paginate(page, total,PAGE_NUMBER)
    start_index = paginator.number
    nganh_nghe = Work.actives.filter(id = work.id).values('nganh_nghe__name').order_by('name')
    noi_thi_tuyen = Work.actives.filter(id = work.id).values('noi_thi_tuyen__name').order_by('name')
    genders = Work.actives.filter(id = work.id).values('gioi_tinh__name').order_by('name')
    taynghe = Work.actives.filter(id = work.id).values('tay_nghe__name').order_by('name')
    images = Image.objects.filter(work_id = work.id).values('image').order_by('id') 
    works = Work.actives.filter(country_id = country.id).exclude(id=work.id).select_related('country', 'user').values(
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
    for work1 in Work.actives.prefetch_related('gioi_tinh'):
        for gioi_tinh in work1.gioi_tinh.all():
            require_gioi_tinh_map[work1.id].append(gioi_tinh.name)

    for work1 in works:
        work1['gioi_tinh'] = require_gioi_tinh_map.get(work1['id'], [])
        fb_link = work1.get('user__facebook', '')
        if not fb_link or not is_valid_url(fb_link):
            work1['user__facebook'] = None 
    return render(request, 'home/detail.html', {'country':country, 'work':work, 'nganh_nghe':nganh_nghe, 
        'genders':genders, 'taynghe':taynghe, 'images':images, "works":works, 'page':page, 'paginator':paginator, 'path_url':path_url,
        'noi_thi_tuyen':noi_thi_tuyen, 'workfacebook':workfacebook})           



def login_view(request):
    if request.method == "POST":
        phone_number = request.POST.get("username")
        password = request.POST.get("password")
        remember_me = request.POST.get("rememberme")
        try:
            user = CustomUser.objects.get(username=phone_number)
            if not user.is_active:
                return JsonResponse({
                    "success": False,
                    "message": "Tài khoản đang bị KHÓA vĩnh viễn! Thời gian mở khóa: Không xác định. Vui lòng liên hệ admin."
                })
        except CustomUser.DoesNotExist:
            return JsonResponse({"success": False, "message": "Số điện thoại hoặc mật khẩu không đúng!"})
        user = authenticate(request, username=phone_number, password=password)
        if user is not None:
            login(request, user)
            request.session["role"] = user.role
            request.session["ho_va_ten_dem"] = user.ho_va_ten_dem
            request.session.modified = True 
            if remember_me:
                request.session.set_expiry(30 * 24 * 60 * 60)
            else:
                request.session.set_expiry(0) 
            user_profile = get_object_or_404(CustomUser, id=user.id)
            is_missing_info = (
                not user_profile.ho_va_ten_dem or
                not user_profile.nam_sinh or
                not user_profile.tinh_thanh_pho
            )
            show_update_modal = user_profile.role == "applicant" and is_missing_info
            return JsonResponse({
                "success": True,
                "message": "Đăng nhập thành công!" if not show_update_modal else "Đăng nhập thành công, vui lòng cập nhật thông tin!",
                "show_update_modal": show_update_modal,
                "role": user.role
            })

        return JsonResponse({"success": False, "message": "Số điện thoại hoặc mật khẩu không đúng!"})

    return JsonResponse({"success": False, "message": "Phương thức không hợp lệ!"})



def register_view(request):
    if request.method == "POST":
        phone = request.POST.get("user_name")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        role = request.POST.get("role")

        if not is_valid_phone(phone):
            return JsonResponse({"success": False, "message": "Số điện thoại không hợp lệ!"})

        if password != password2:
            return JsonResponse({"success": False, "message": "Mật khẩu nhập lại không khớp!"})

        if CustomUser.objects.filter(username=phone).exists():
            return JsonResponse({"success": False, "message": "Số điện thoại đã tồn tại!"})

        user = CustomUser(username=phone, role=role)
        user.set_password(password)

        if role == "applicant":
            user.save()
            return JsonResponse({"success": True, "message": "Đăng ký thành công! Vui lòng đăng nhập.", "showLoginForm": True})

        elif role == "employer":
            otp_code = generate_otp()
            user.otp_code = otp_code
            user.otp_created_at = timezone.now()
            user.save()
            return JsonResponse({"success": True, "message": "Mã OTP đã được gửi", "showOtpForm": True, "otp_code":otp_code})
    return JsonResponse({"success": False, "message": "Yêu cầu không hợp lệ."})        



def verify_otp(request):
    if request.method == "POST":
        phone = request.POST.get("username")
        otp_input = request.POST.get("otp")

        try:
            user = CustomUser.objects.get(username=phone, role="employer")

            if user.otp_code == otp_input and user.otp_created_at + timedelta(minutes=5) > now():
                user.otp_code = None
                user.save()
                return JsonResponse({"success": True, "message": "Xác nhận OTP thành công! Vui lòng đăng nhập.", "showLoginForm": True})
            else:
                return JsonResponse({"success": False, "message": "OTP không hợp lệ hoặc đã hết hạn!"})

        except CustomUser.DoesNotExist:
            return JsonResponse({"success": False, "message": "Không tìm thấy người dùng!"})



def send_otp_reset_password(request):
    if request.method == "POST":
        phone_number = request.POST.get("username") 
        try:
            user = CustomUser.objects.get(username=phone_number)
        except CustomUser.DoesNotExist:
            return JsonResponse({"success": False, "message": "Số điện thoại chưa đăng ký!"})
        if user.role != "employer":
            return JsonResponse({"success": False, "message": "Bạn không có quyền đổi mật khẩu!"})
        otp_code = generate_otp()
        user.otp_code = otp_code
        user.otp_created_at = now()
        user.save()
        return JsonResponse({
            "success": True,
            "message": "Mã OTP đã được gửi!",
            "showVerifyForm": True,
            "otp_code": otp_code 
        })
    return JsonResponse({"success": False, "message": "Lỗi không xác định!"})


def verify_otp_reset_password(request):
    if request.method == "POST":
        phone_number = request.POST.get("username")
        otp_code = request.POST.get("verify_code")
        new_password = request.POST.get("new_password")
        try:
            user = CustomUser.objects.get(username=phone_number, otp_code=otp_code)
        except CustomUser.DoesNotExist:
            return JsonResponse({"success": False, "message": "Mã OTP không hợp lệ hoặc số điện thoại không đúng!"})
        if user.role != "employer":
            return JsonResponse({"success": False, "message": "Bạn không có quyền đổi mật khẩu!"})
        user.password = make_password(new_password)
        user.otp_code = None 
        user.save()
        return JsonResponse({"success": True, "message": "Mật khẩu đã được cập nhật! Vui lòng đăng nhập."})
    return JsonResponse({"success": False, "message": "Lỗi không xác định!"})    



@login_required
@csrf_exempt
def update_user_info_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user = request.user
            user_profile = get_object_or_404(CustomUser, id=user.id)
            user_profile.ho_va_ten_dem = data.get("ho_va_ten_dem", user_profile.ho_va_ten_dem)
            user_profile.gioi_tinh = data.get("gioi_tinh", user_profile.gioi_tinh)
            user_profile.nam_sinh = data.get("nam_sinh", user_profile.nam_sinh)
            city_id = data.get("tinh_thanh_pho")
            if city_id:
                user_profile.tinh_thanh_pho = City.objects.get(id=city_id)
            country_ids = data.get("countries", [])
            if country_ids:
                selected_countries = Country.objects.filter(id__in=country_ids)
                user_profile.country.set(selected_countries)
            profession_ids = data.get("professions", [])
            if profession_ids:
                selected_professions = Profession.objects.filter(id__in=profession_ids)
                user_profile.nganh_nghe.set(selected_professions)

            user_profile.save()
            return JsonResponse({"success": True, "message": "Cập nhật thông tin thành công!"})

        except City.DoesNotExist:
            return JsonResponse({"success": False, "message": "Thành phố không hợp lệ!"})
        except Exception as e:
            return JsonResponse({"success": False, "message": f"Lỗi: {str(e)}"})

    return JsonResponse({"success": False, "message": "Phương thức không hợp lệ!"})

@csrf_exempt
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"success": True, "message": "Đăng xuất thành công!"})
    return JsonResponse({"success": False, "message": "Phương thức không hợp lệ!"}, status=400)

