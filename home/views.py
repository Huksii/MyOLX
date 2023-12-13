from django.shortcuts import render
from ads.models import Ads, Category
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    ads = Ads.objects.all()
    context = {
        'context_ads': ads,
    }
    return render(request, 'index.html', context)

