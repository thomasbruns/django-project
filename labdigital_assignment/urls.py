from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('export/', views.export_products, name='export_products'),
]



