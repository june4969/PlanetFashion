from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def mypage(request):

    return render(request, 'my_page.html')
