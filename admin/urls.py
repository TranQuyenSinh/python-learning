from .views import *
from django.urls import path,include

urlpatterns = [
    path('', admin_view.dashboard, name='dashboard'),
    
    path('dang-nhap', auth_view.login, name='login'),
    
    path('loai-san-pham', loaisanpham_view.index, name='loaisanpham.index'),
    path('loai-san-pham/create', loaisanpham_view.create, name='loaisanpham.create'),
    path('loai-san-pham/<id>/delete', loaisanpham_view.delete, name='loaisanpham.delete'),
    
    path('san-pham', sanpham_view.index, name='sanpham.index'),
    path('san-pham/create', sanpham_view.create, name='sanpham.create'),
    path('san-pham/<id>/delete', sanpham_view.delete, name='sanpham.delete'),
]
