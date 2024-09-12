from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from bson import ObjectId
from ..models import *

# Create your views here.
def index(request):
    loaisanpham = LoaiSanPham.objects.all()
    paginator = Paginator(loaisanpham, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, 'danhmuc/loaisanpham/index.html', {'page_obj': page_obj})

def create(request):
    if request.method == 'POST':
        ten = request.POST.get('ten')
        image = request.FILES.get('image') 
        loai = LoaiSanPham.objects.create(ten=ten, image=image)
        loai.save()
        return redirect('loaisanpham.index')
    else:
        return render(request, 'danhmuc/loaisanpham/create.html')
    
def delete(request, id):
    loai = LoaiSanPham.objects.get(_id=ObjectId(id))
    if loai.image:
        loai.image.delete()
    loai.delete()
    return redirect('loaisanpham.index')