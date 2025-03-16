from django.contrib import admin
from .models import *
from django.forms import CheckboxSelectMultiple


class ImageInline(admin.StackedInline):
    model = Image
    extra = 0


class PriceInline(admin.ModelAdmin):
    search_fields = ('price', )
    list_display = ('price', 'priority', 'updated')
    list_editable = ['priority']

admin.site.register(Price, PriceInline)

class WorkmanshipInline(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', 'updated')
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

admin.site.register(Workmanship, WorkmanshipInline)


class GenderAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', 'updated')
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

admin.site.register(Gender, GenderAdmin)

class WorkAdmin(admin.ModelAdmin):
    search_fields = ('name', 'id')
    list_display = ('name', 'slug', 'country', 'province', 'active', 'user')
    list_select_related = True
    list_per_page = 100
    list_filter = ('country', 'noi_thi_tuyen')
    fieldsets = (
        (None, {"fields": ("name", "slug",
             "country", "province", "cong_ty_nghiep_doan", "nganh_nghe",
            "cong_viec_cu_the", "noi_thi_tuyen", "thoi_gian_lam_viec", "luong_co_ban",
            "luong_co_ban_menh_gia", "lam_them", "thu_nhap_du_kien", "thu_nhap_du_kien_menh_gia",
            "quyen_loi_khac", "so_luong_tuyen", "hop_dong", "phi_xuat_canh", "phi_xuat_canh_menh_gia",
            "chuong_trinh_ho_tro", "image", "noi_dung_chi_tiet", 'hot_expiry', 'view', 'is_confirmed')}),
        ("Yêu Cầu", {"fields": ("gioi_tinh", "nam_sinh", "ket_thuc_nam_sinh", "trinh_do_hoc_van",
            "chuyen_nganh", "tay_nghe", "ngoai_ngu", "yeu_cau_hoc_tieng", "tinh_trang_suc_khoe", 
            "thi_luc", "viem_gan_b", "xam_hinh", "yeu_cau_khac")}),
        ("Thi tuyển", {"fields": ("hinh_thuc_thi_tuyen", "ngay_thi_tuyen", "han_dang_ky", "du_kien_xuat_canh")}),
    )
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
    inlines = (ImageInline, )

    exclude = ('user',)

    def save_formset(self, request, form, formset, change):
        formset.save()
        if not change:
            for f in formset.forms:
                obj = f.instance 
                obj.user = request.user
                obj.save()
                
    def save_model(self, request, obj, form, change):
        if obj.user == None:
            obj.user = request.user
        obj.save() 

admin.site.register(Work, WorkAdmin)

