from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Advisory, CandidateView
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.forms import CheckboxSelectMultiple
from django.db import models


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        ("Thông tin tài khoản", {"fields": ("username", "email", "password", "point")}),
        ("Thông tin vai trò", {"fields": ("role", "groups", "user_permissions")}),
        ("Cập nhật thông tin cá nhân", {"fields": ("ho_va_ten_dem", "ten_goi", "gioi_tinh", "nam_sinh", "phone", "zalo", "facebook", "sinh_song_tai", "dia_chi", "noi_lam_viec",
            "ten_viet_tat", "chuc_vu", "kinh_nghiem", "avata", "anh_bia", "tinh_thanh_pho", "tu_van", "ghi_chu")}),
        ("Quan tâm đến", {"fields": ("country", "nganh_nghe")}),
        ("Sức khỏe", {"fields": ("chieu_cao", "can_nang", "thi_luc", "hinh_xam", "viem_gan_b", "hut_thuoc", "uong_ruou", "benh_di_truyen")}),
        ("Học vấn", {"fields": ("tot_nghiep", "ngoai_ngu", "bang_nghe")}),
        ("Tự giới thiệu", {"fields": ("tinh_cach", "so_thich", "yeu_cau_khac")}),
        ("Kinh nghiệm", {"fields": ("tay_nghe", "da_di_xkld")}),
        ("Quyền hệ thống", {"fields": ("is_staff", "is_superuser", "is_active", "last_login", "date_joined")}),
    )

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "user_permissions":
            kwargs.pop("widget", None)
        return super().formfield_for_manytomany(db_field, request, **kwargs)
    search_fields = ('id', 'username')    
    list_display = ("id", "username", "ho_va_ten_dem", "ten_goi", "tinh_thanh_pho", "role", "is_staff", "is_active", 'point')
    list_editable = ['is_active', 'point']
    list_per_page = 50
    list_filter = ("role", "is_staff", "is_superuser")


class CandidateViewAdmin(admin.ModelAdmin):
    search_fields = ('employer', 'candidate')
    list_display = ('id', 'employer','candidate', 'viewed_at')

admin.site.register(CandidateView, CandidateViewAdmin)


class AdvisoryAdmin(admin.ModelAdmin):
    search_fields = ('name', 'phone')
    list_display = ('id', 'name','phone', 'work', 'active')
    list_editable = ['active',]
    list_filter = ('work','active')

admin.site.register(Advisory, AdvisoryAdmin)