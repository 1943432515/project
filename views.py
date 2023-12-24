from django.shortcuts import render, redirect
from .models import *
from DS.forms import loginform


# Create your views here.
def index(request):
    return render(request, 'index.html')


def customer_register(request):
    information = ""
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        re_password = request.POST.get("re_password")
        if password != re_password:
            information = "前后密码不同！"
            return render(request, 'customer_register.html', {"information": information})
        if username == None or email == None or password == None or re_password == None:
            information = "信息不能为空！"
            return render(request, 'customer_register.html', {"information": information})
        if customerinfo.objects.filter(user_name=username).count() > 0:
            information = "账号已存在！"
            return render(request, 'customer_register.html', {"information": information})
        customerinfo.objects.create(user_name=username, user_email=email, user_password=password)
        return redirect("/customer_login/")
    return render(request, 'customer_register.html', {"information": information})


def customer_login(request):
    if request.method == 'POST':
        login_form = loginform(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("password")
            user = customerinfo.objects.filter(user_name=username, user_password=password).first()
            if user:
                request.session["customer_login"] = True
                request.session["customer_name"] = user.user_name
                request.session["customer_email"] = user.user_email
                return redirect("/homepage/")
            else:
                information = "用户名或密码错误！"
                return render(request, 'customer_login.html', locals())
        else:
            information = "信息填写不合理!"
            return render(request, 'customer_login.html', locals())
    login_form = loginform()
    return render(request, 'customer_login.html', locals())


def seller_register(request):
    information = ""
    if request.method == "POST":
        username = request.POST.get("username")
        id_number = request.POST.get("id_number")
        email = request.POST.get("username")
        password = request.POST.get("password")
        re_password = request.POST.get("re_password")
        if password != re_password:
            information = "前后密码不同！"
            return render(request, 'seller_register.html', {"information": information})
        if username == None or email == None or password == None or re_password == None or id_number == None:
            information = "信息不能为空！"
            return render(request, 'seller_register.html', {"information": information})
        if sellerinfo.objects.filter(user_name=username).count() > 0:
            information = "账号已存在！"
            return render(request, 'seller_register.html', {"information": information})
        sellerinfo.objects.create(user_name=username, id_number=id_number, user_email=email, user_password=password)
        return redirect("/seller_login/")
    return render(request, 'seller_register.html', {"information": information})


def seller_login(request):
    if request.method == 'POST':
        login_form = loginform(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get("username")
            password = login_form.cleaned_data.get("password")
            user = sellerinfo.objects.filter(user_name=username, user_password=password).first()
            if user:
                request.session["seller_login"] = True
                request.session["seller_name"] = user.user_name
                request.session["seller_email"] = user.user_email
                request.session["id_number"] = user.id_number
                return redirect("/homepage1/")
            else:
                information = "用户名或密码错误！"
                return render(request, 'seller_login.html', locals())
        else:
            information = "信息填写不合理!"
            return render(request, 'seller_login.html', locals())
    login_form = loginform()
    return render(request, 'seller_login.html', locals())


def homepage(request):
    if request.session.get("customer_login"):
        return render(request, 'homepage.html')
    else:
        information = "请先登录，否则无法购物！"
        return render(request, 'homepage.html', {"information": information})


def homepage1(request):
    return render(request, 'homepage1.html')


def individual_center(request):
    if request.session.get("customer_login"):
        name = request.session.get("customer_name")
        if len(Image.objects.filter(name=name)) > 0:
            image = Image.objects.filter(name=name)[0].image
        else:
            image = "无头像"
        return render(request, 'individual_center.html', {"image": image})
    else:
        return redirect('/')


def individual_center1(request):
    if request.session.get("seller_login"):
        name = request.session.get("seller_name")
        if len(Image.objects.filter(name=name)) > 0:
            image = Image.objects.filter(name=name)[0].image
        else:
            image = "无头像"
        return render(request, 'individual_center1.html', {"image": image})
    else:
        return redirect('/')


def image(request):
    if request.session.get("customer_login"):
        name = request.session.get("customer_name")
        id = False
        if request.method == 'POST':
            image = request.FILES.get('image')
            Image.objects.filter(name=name).delete()
            images = Image(name=name, image=image)
            images.save()
            return redirect("/individual_center/")
    elif request.session.get("seller_login"):
        name = request.session.get("seller_name")
        id = True
        if request.method == 'POST':
            image = request.FILES.get('image')
            Image.objects.filter(name=name).delete()
            images = Image(name=name, image=image)
            images.save()
            return redirect('/individual_center1/')
    else:
        return redirect('/')
    return render(request, 'image.html', locals())


def info(request):
    if request.session.get("customer_login"):
        username = request.session.get("customer_name")
        email = request.session.get("customer_email")
        id = False
        if customerinfo.objects.filter(user_name=username, user_email=email).count() > 0:
            user = customerinfo.objects.filter(user_name=username, user_email=email)[0]
            tel_number = user.tel_number
            gender = user.gender
            name = user.true_name
            address = user.address
            return render(request, 'info.html', locals())
        else:
            return render(request, 'info.html', locals())
    elif request.session.get("seller_login"):
        username = request.session.get("seller_name")
        email = request.session.get("seller_email")
        id = True
        if sellerinfo.objects.filter(user_name=username, user_email=email).count() > 0:
            user = sellerinfo.objects.filter(user_name=username, user_email=email)[0]
            gender = user.gender
            tel_number = user.tel_number
            name = user.true_name
            address = user.address
            id_number = user.id_number
            return render(request, 'info.html', locals())
        else:
            return render(request, 'info.html', locals())
    else:
        return redirect("/")


def change(request):
    if request.session.get("customer_login"):
        if request.method == 'POST':
            gender = False
            name = request.POST.get("name", False)
            email = request.POST.get("email", False)
            if request.POST.get("male"):
                gender = "男"
            elif request.POST.get("female"):
                gender = "女"
            tel_number = request.POST.get("tel_number", False)
            address = request.POST.get("address", False)
            password = request.POST.get("password", False)
            if name and email and gender and tel_number and address and password:
                customerinfo.objects.filter(user_name=request.session.get("customer_name")).update(user_email=email,
                                                                                                   gender=gender,
                                                                                                   tel_number=tel_number,
                                                                                                   true_name=name,
                                                                                                   address=address,
                                                                                                   uer_password=password)
                return redirect('/info/')
            else:
                information = "信息不能为空！！"
                return render(request, 'change.html', {"information": information})
        return render(request, 'change.html')
    elif request.session.get("seller_login"):
        if request.method == 'POST':
            name = request.POST.get("name", False)
            email = request.POST.get("email", False)
            if request.POST.get("male", False):
                gender = "男"
            elif request.POST.get("female", False):
                gender = "女"
            else:
                gender = False
            tel_number = request.POST.get("tel_number", False)
            address = request.POST.get("address", False)
            password = request.POST.get("password", False)
            if name and email and gender and tel_number and address and password:
                sellerinfo.objects.filter(user_name=request.session.get("seller_name")).update(user_email=email,
                                                                                               gender=gender,
                                                                                               tel_number=tel_number,
                                                                                               true_name=name,
                                                                                               address=address,
                                                                                               uer_password=password)
                return redirect('/info/')
            else:
                information = "信息不能为空！！"
                return render(request, 'change.html', {"information": information})
        return render(request, 'change.html')
    else:
        return redirect("/")


def list(request):
    return render(request, 'list.html')


def wallet(request):
    money = customerinfo.objects.filter(user_name=request.session.get("customer_name"))[0].money
    return render(request, 'wallet.html', {"money": money})


def add(request):
    if request.session.get("customer_login") == True:
        if request.method == 'POST':
            add_money = float(request.POST.get("money"))
            money = float(customerinfo.objects.filter(user_name=request.session.get("customer_name"),
                                                      user_email=request.session.get("customer_email"))[0].money)
            money += add_money
            customerinfo.objects.filter(user_name=request.session.get("customer_name"),
                                        user_email=request.session.get("customer_email")).update(money=money)
            return render(request, 'wallet.html')
    else:
        redirect('index')
    return render(request, 'add.html')


def shop(request):
    good_list = []
    if request.session.get("seller_login") == True:
        if request.POST.get("delete", False) != False:
            goodinfo.objects.filter(name=request.POST.get("delete")).delete()
        if request.POST.get("ON",False):
            goodinfo.objects.filter(name=request.POST.get("ON")).update(status="ON")
        elif request.POST.get("OFF",False):
            goodinfo.objects.filter(name=request.POST.get("OFF")).update(status="OFF")
        goods = goodinfo.objects.all()
        for i in goods:
            good_list.append([i.name, i.image, i.price, i.introduction, i.number, i.label, i.get_status_display()])
    else:
        redirect('/index/')
    return render(request, 'shop.html', {"good_list": good_list})


def add_goods(request):
    if request.session.get("seller_login") == True:
        if request.method == 'POST':
            good_name = request.POST.get("good_name")
            good_image = request.FILES.get("good_image")
            good_price = request.POST.get("price")
            introduction = request.POST.get("introduction")
            good_number = request.POST.get("number")
            good_label = request.POST.get("label")
            good_status = "OFF"
            if request.POST.get("on", False):
                good_status = request.POST.get("on")
            elif request.POST.get("off", False):
                good_status = request.POST.get("off")
            seller_id = sellerinfo.objects.filter(user_name=request.session.get("seller_name"))[0].id
            goodinfo.objects.create(name=good_name, image=good_image, price=good_price, introduction=introduction,
                                    number=good_number, label=good_label, good_status=good_status, seller_id=seller_id)
            return redirect('/shop/')
    else:
        return redirect('/index/')
    return render(request, 'add_goods.html')


def good_change(request):
    if request.session.get("seller_login") == True:
        if request.method == 'POST':
            good_name = request.POST.get("good_name")
            good_image = request.FILES.get("good_image")
            good_price = request.POST.get("price")
            introduction = request.POST.get("introduction")
            good_number = request.POST.get("number")
            good_label = request.POST.get("label")
            seller_id = sellerinfo.objects.filter(user_name=request.session.get("seller_name"))[0].id
            goodinfo.objects.filter(seller_id=seller_id).update(name=good_name, image=good_image, price=good_price,
                                                                introduction=introduction, number=good_number,
                                                                label=good_label)
            return redirect('/shop/')
    else:
        return redirect('/index/')
    return render(request, 'good_change.html')


def logout(request):
    request.session.flush()
    return render(request, 'logout.html')
