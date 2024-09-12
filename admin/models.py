from djongo import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    phone = models.CharField(max_length=15, blank=True, null=True)
    
    @property
    def id(self):
        return str(self._id)

class KhachHang(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=False)
    ten = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    
   
class LoaiSanPham(models.Model):
    _id = models.ObjectIdField()
    ten = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)
    
    @property
    def id(self):
        return str(self._id)
    
    @property
    def ImageURL(seld):
        try:
            url = seld.image.url
        except:
            url = ""
        return url

class DonViTinh(models.Model):
    _id = models.ObjectIdField()
    donvitinh = models.CharField(max_length=200, null=True)
    gia = models.IntegerField()
    
class SanPham(models.Model):
    _id = models.ObjectIdField()
    ten = models.CharField(max_length=200, null=True)
    loaisanpham = models.ForeignKey(LoaiSanPham, on_delete=models.SET_NULL, null=True, blank=True)
    trangthai = models.BooleanField(default=True, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    donvitinh = models.ArrayField(
        model_container=DonViTinh
    )

    @property
    def id(self):
        return str(self._id)
    
    @property
    def ImageURL(seld):
        try:
            url = seld.image.url
        except:
            url = ""
        return url



class Order(models.Model):
    user = models.ForeignKey(KhachHang, on_delete=models.SET_NULL, null=True, blank=True)
    ngaydat = models.DateTimeField(auto_now_add=True)
    hoanthanh = models.BooleanField(default=False, null=True, blank=False)
    giaodich_id = models.CharField(max_length=200, null=True)


class OrderItem(models.Model):
    sanpham = models.ForeignKey(SanPham, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    soluong = models.IntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
