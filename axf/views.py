from django.shortcuts import render

# Create your views here.
from axf.models import Lunbo


def home(request):

    #轮播图
    wheels = Lunbo.objects.all()
    data = {
        'wheels':wheels
    }



    return render(request,'home/home.html',context=data)


def market(request):
    return render(request,'market/market.html')


def cart(request):
    return render(request,'cart/cart.html')


def mine(request):
    return render(request,'mine/mine.html')