from django.conf.urls import url
from .views import *
urlpatterns=[
    #首页
    url(r'^index/$',index,name='index')
]