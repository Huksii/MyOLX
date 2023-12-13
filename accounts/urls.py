from django.urls import path
from .views import SignInUser, SignUpUser, SignOutUser, user_ads, UserProfile, EditProfile
from rest_framework import routers
from .api import ProfileViewSet, UserViewSet

urlpatterns = [
    path('signin/', SignInUser, name='login'),
    path('signup/', SignUpUser, name='register'),
    path('signout/', SignOutUser, name='logout'),
    
    path('myads/', user_ads, name='myads'),
    
    path('profile/<int:user_id>/', UserProfile, name='profile'),
    path('edit-profile/<int:user_id>/', EditProfile, name='edit_profile'),
]

router = routers.DefaultRouter()
router.register(r"api/profiles", ProfileViewSet, basename="profiles")
router.register(r"api/users", UserViewSet, basename="users")
urlpatterns += router.urls