from django.shortcuts import render
from .models import Article


def article(request):
    articles = Article.objects.all()
    return render(request, 'article.html', {'articles': articles})
