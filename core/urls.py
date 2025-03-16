from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('chaining/', include('smart_selects.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]
urlpatterns += i18n_patterns (
    path('qlyadmin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', include('user.urls')),
    path('', include('page.urls')),
    path('', include('city.urls')),
    path('', include('blog.urls')),
    prefix_default_language=False
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if not settings.DEBUG:
    urlpatterns += static("/media/", document_root=settings.MEDIA_ROOT)
