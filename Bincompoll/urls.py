from django.contrib import admin
from django.urls import path
from poll import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('pu-result/', views.pu_result, name='pu-result'),
    path('lga-page/', views.lga_page, name='lga-page'),
    path('lga-result/', views.lga_result, name='lga-result'),
    path('create-pu/', views.create_pu, name='create-pu'),
    path('store-apu-result/', views.store_apu_result, name='store'),
    path('store-result-apu/<int:unique_id>/', views.store_result_apu, name='store_new'),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
