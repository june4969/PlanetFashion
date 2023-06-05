
from django.contrib import admin
from django.urls import include, path
from home.views import about



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('about/', about, name='about'),
]
