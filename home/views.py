from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def shop(request):
    return render(request, 'shop/shop.html')

def article(request):
    return render(request, 'article/article.html')


def login(request):
    return render(request, 'accounts/login.html')


