from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('', views.home, name=''),
    path('about', views.about, name='about'),
    path('artworks', views.artwork, name='artworks'),
    path('blog/', include('blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
