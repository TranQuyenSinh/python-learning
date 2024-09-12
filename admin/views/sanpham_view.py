from django.core.paginator import Paginator
from django.shortcuts import render,redirect, HttpResponse
from ..models import *
from bson import ObjectId
from django.contrib import messages
# Create your views here.
def index(request):
    sanpham = SanPham.objects.all()
    paginator = Paginator(sanpham, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'danhmuc/sanpham/index.html', {'page_obj': page_obj})

def create(request):
    if request.method == 'POST':
        loaisanpham = LoaiSanPham.objects.get(_id=ObjectId(request.POST.get('loaisanpham_id')))
        ten = request.POST.get('ten')
        trangthai = request.POST.get('trangthai')
        image = request.FILES.get('image')
        donvitinh = []
        units = request.POST.getlist('donvitinh')
        prices = request.POST.getlist('gia')
        for i in range(len(prices)):
            donvitinh.append({'_id': ObjectId(), 'donvitinh':units[i], 'gia':prices[i]})
        sanpham = SanPham.objects.create(loaisanpham=loaisanpham, ten=ten, image=image, donvitinh=donvitinh, trangthai=trangthai)
        sanpham.save()
        messages.success(request, 'Sản phẩm đã được thêm thành công!')
        return redirect('sanpham.index')
    else:
        loaisanpham = LoaiSanPham.objects.all()
        print(len(loaisanpham))
        return render(request, 'danhmuc/sanpham/create.html', {"loaisanpham": loaisanpham})
    
def delete(request, id):
    sanpham = SanPham.objects.get(_id=ObjectId(id))
    if sanpham.image:
        sanpham.image.delete()
    sanpham.delete()
    return redirect('sanpham.index')