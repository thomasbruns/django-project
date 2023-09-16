from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('export/', views.export_products, name='export_products'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
