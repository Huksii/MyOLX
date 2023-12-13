from django.shortcuts import render, redirect
from .models import Ads
from .forms import AdsForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required(login_url='login')
def ads_detail(request, ads_id):
    ads = Ads.objects.get(id=ads_id)
    # SELECT * FROM ads WHERE id = ads_id
    
    context = {
        "ads_detail": ads
    }
    return render(request, 'ads_detail.html', context)
    
@login_required(login_url='login')    
def ads_add(request):
    if request.method == "POST":
        form = AdsForm(request.POST, request.FILES)
        if form.is_valid():
            new_ads = form.save(commit=False)
            new_ads.user = request.user
            new_ads.save()
            return redirect("myads")
        else:
            messages.error(request, form.errors)
            return redirect("ads_add")
    else:
        form = AdsForm()
    context = {
        "ads_form": form
    }
    return render(request, 'ads_add.html', context)

@login_required(login_url='login')
def ads_delete(request, ads_id):
    ads = Ads.objects.get(id=ads_id)
    if ads.user == request.user:
        ads.delete()
        return redirect("myads")
    else:
        messages.error(request, "Это не ваше объявление")
        return redirect("myads")