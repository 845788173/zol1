import os

import random

from PIL import Image, ImageDraw, ImageFont
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from zol.settings import MEDIA_ROOT
from .models import *


def index(request):
    carousels = Carousel.objects.all()
    # carou=Carousel.objects.get()?
    data = {
        'carousels': carousels,
    }



    return render(request, 'index/index.html', data)


# def generate_icon():
#     uid=str(uuid.uuid4())
#     return my_md5(uid)
#
#
# def my_md5(string):
#     m=hashlib.md5()
#     m.update(string.encode())
#     return m.hexdigest()
def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        users = User.objects.filter(u_username=username, u_password=password)
        if users.exists():
            request.session['userid'] = users.first().id
            return render(request, 'index/index.html')
            # return HttpResponse('')
        else:
            return render(request, 'login/login.html')


def register(request):


    if request.method=='POST':


        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User()
        user.u_username = username
        user.u_password = password

        user.save()
        request.session['userid'] = user.id
        return redirect('ZOL:index')
        # return HttpResponse('')


    else:
        return render(request,'register/register.html')


def verifycode(request):
    # 图片基本设置
    # RGB: 0~255
    bgcolor = (random.randint(10, 200), random.randint(10, 200), random.randint(10, 200))
    # bgcolor = (120,120,120)
    width = 100
    height = 50

    # 创建图片
    image = Image.new('RGB', (width, height), bgcolor)

    # 画笔对象
    draw = ImageDraw.Draw(image)

    # 添加噪点
    for i in range(0, 1000):
        # 坐标
        xy = (random.randint(0, width), random.randint(0, height))
        # 颜色
        fill = (random.randint(0, 255), 255, random.randint(0, 255))
        draw.point(xy, fill=fill)

    # 添加验证码
    str = '1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'

    # 产生随机数
    rand_str = ''
    for i in range(0, 4):
        rand_str += str[random.randint(0, len(str) - 1)]

    # 保存验证码

    # 指定字体类型
    font = ImageFont.truetype('static/fonts/华康棒棒体繁W5.ttc', 35)

    # 字体颜色
    font_color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    font_color2 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    font_color3 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    font_color4 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # 绘制字体
    draw.text((5, 2), rand_str[0], font=font, fill=font_color1)
    draw.text((25, 2), rand_str[1], font=font, fill=font_color2)
    draw.text((45, 2), rand_str[2], font=font, fill=font_color3)
    draw.text((65, 2), rand_str[3], font=font, fill=font_color4)

    # 释放画笔
    del draw

    # 文件操作
    # icon_name = generate_icon() + os.path.splitext(icon.name)[-1]

    icon_name = rand_str + ".png"

    icon_path = os.path.join(MEDIA_ROOT, icon_name)

    # with open(icon_path, 'wb') as fp:
    # for part in image.chunks():
    image.save(icon_path)
    # fp.write(image)
    # fp.flush()

    # image.save(fp, 'png')
    icon_path1 = "/static/img_lunbo/" + icon_name
    data = {
        'icon_path1': icon_path1,
        'rand_str': rand_str
    }
    return JsonResponse(data)


def detailed(request ,d_smallimg,d_price,d_color,d_num):
    detaileds=Detailed.objects.all()

    detailed=Detailed.objects.first()
    data={
        'detaileds':detaileds,
        'detailed':detailed,

}

    return render(request,'detailed/detailed.html',data)


def shopcar(request):
    return render(request,'shopcar/shopCar.html')
