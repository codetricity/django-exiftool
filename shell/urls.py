from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),
    path('watermark/', views.watermark),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
