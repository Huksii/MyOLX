from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# class User(models.Model):
    # """
    # username = models.CharFields()
    # password = models.CharField()
    # password1 = models.CharField()
    
    # first_name = models.CharField()
    # last_name = models.CharField()
    # email = models.EmailField()
    
    # date_joined = models.DateTimeField()
    # created_at = models.DateTimeField()
    
    # is active = models.BooleanField()
    
    # is_staff = models.BooleanField()
    # is superuser = models.BooleanField()
    # """
    # pass

class Profile(models.Model):
    image = models.ImageField(upload_to='profile_pics/', verbose_name="Изображения", blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self) -> str:
        return self.user.username
    
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Учёные записи"

