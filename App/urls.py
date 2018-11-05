from django.conf.urls import url
from .views import *
urlpatterns=[
    #首页
    url(r'^index/$',index,name='index'),

    url(r'^login/$',login,name='login'),
    url(r'^register/$',register,name='register'),
    url(r'^verifycode/$',verifycode,name='verifycode'),
    url(r'^detailed/(\d+)/(\d+)/(\d+)/(\d+)/$',detailed,name='detailed'),
    url(r'^shopcar/$',shopcar,name='shopcar')
]