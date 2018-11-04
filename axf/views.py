from django.shortcuts import render

# Create your views here.
from axf.models import Lunbo, Nav, Mustbuy, Shop, MainShow, Foodtypes, Goods


def home(request):

    #轮播图
    wheels = Lunbo.objects.all()

    #导航
    navs = Nav.objects.all()

    #每日必购
    mustbuy = Mustbuy.objects.all()

    #商品部分
    shop = Shop.objects.all()

    shoptab = shop[1:3]
    shopclass = shop[3:7]
    shopcommend = shop[7:11]

    #首页主体部分
    mainshow = MainShow.objects.all()



    data = {
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuy,
        'shops':shop,
        'shoptabs':shoptab,
        'shopclass':shopclass,
        'shopcommends':shopcommend,
        'mainshows':mainshow,


    }



    return render(request,'home/home.html',context=data)


def market(request,categoryid):
    # 　闪购超市　商品侧边分类
    foodtypes = Foodtypes.objects.all()

    #当在闪购超市页面点击分类侧边栏时，能显示对应的分类商品；但当点击首页
    #再次回到闪购超市页面时，显示的不是你刚点击的分类的商品，而是打开闪购超市页面
    # 默认显示第一栏热销榜的商品(在base.html中设置了默认参数)，这是因为用cookie
    #获取到的typeIndex并未与商品进行关联；
    #所以需要在这里获取到cookie保存的typeIndex来与商品id进行关联

    #这里需要给个默认下标值，因为进入闪购超市时，还未点击，cookie也就没有值，
    #刚进入时让其默认显示第一栏，所以这里需要给个默认下标值０
    #注意数据类型，获取到的值都是字符串类型，所以用int转换为数字类型
    typeIndex = int(request.COOKIES.get('typeIndex',0))

    #商品id(typeid)在模型类Foodtypes里面
    #点击哪个分类时，cookie获取到分类下标，通过这个下标取到具体点击的一个商品，获取这个商品的分类id
    #这就将typeIndex与typeid关联起来了
    categoryid = foodtypes[typeIndex].typeid



    #顶部导航栏，子类信息
    #childtypenames:全部分类:0#进口水果:103534#国产水果:103533
    childtypenames = foodtypes.get(typeid=categoryid).childtypenames

    #将每个子类拆分出来
    childtypeList = []
    for item in childtypenames.split("#"):
        list1 = item.split(":")
        dict1 = {
            'childname':list1[0],   #子类名称  全部分类   进口水果  国产水果
            'childid':list1[1]      #子类id    0        103534   103533

        }
        childtypeList.append(dict1)

    # 通过点击分类侧边栏，a标签的路由指向market，并在后面带参分类id（typeid），这个分类id
    # 在foodtype里面，然后传到url，url再把参数传到对应视图函数，这个categoryid
    # 接收传过来的typeid，然后根据这个id来过滤商品
    # 商品信息(过滤根据分类id)

    goods = Goods.objects.filter(categoryid=categoryid)


    data = {
        'foodtypes':foodtypes,
        'goods':goods,
        'childtypeList':childtypeList,
    }


    return render(request,'market/market.html',context=data)


def cart(request):
    return render(request,'cart/cart.html')


def mine(request):
    return render(request,'mine/mine.html')