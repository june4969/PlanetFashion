
from .models import Category
from django.shortcuts import render
from .models import Product




def shop(request):
    categories = Category.objects.all()  # 모든 카테고리 데이터를 쿼리합니다.
    products = Product.objects.all()  # 모든 상품 데이터를 쿼리합니다.
    return render(request, 'shop.html', {'categories': categories, 'products': products})



def mypage(request):
    return render(request, 'my_page.html')
