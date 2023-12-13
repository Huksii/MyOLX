from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from accounts.api import ProfileViewSet, UserViewSet
from ads.api import AdsViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

router.register(r'profiles', ProfileViewSet)
router.register(r"categories", CategoryViewSet)
router.register(r"ads", AdsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('', include('home.urls')),
    path('ads/', include('ads.urls')),
    path('api/', include(router.urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
