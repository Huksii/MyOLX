from django.urls import path
from .views import ads_detail, ads_add, ads_delete
from rest_framework import routers
from .api import CategoryViewSet, AdsViewSet

urlpatterns = [
    path("ads_detail/<int:ads_id>/", ads_detail, name="ads_detail"),
    path("add/", ads_add, name="ads_add"),
    path("delete/<int:ads_id>/", ads_delete, name="ads_delete")
]

router = routers.DefaultRouter()
router.register(r"api/categories", CategoryViewSet, basename="categories")
router.register(r"api/ads", AdsViewSet, basename="ads")
urlpatterns += router.urls
