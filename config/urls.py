from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from home.views import about
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('home.urls')),
                  path('about/', about, name='about'),
                  path('', include('shop.urls')),
                  path('', include('article.urls')),
                  path('', include('accounts.urls'))

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
