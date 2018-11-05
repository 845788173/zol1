from django.db import models


class Carousel(models.Model):
    c_img=models.CharField(max_length=50)

class User(models.Model):
    # id=models.IntegerField(primary_key=True,auto_created=True)
    u_username=models.CharField(max_length=50)
    u_password=models.CharField(max_length=60)

class Detailed(models.Model):
    d_bigimg=models.CharField(max_length=60)
    d_smallimg=models.CharField(max_length=50)
    d_color=models.CharField(max_length=60)
    d_tc=models.CharField(max_length=30)
    d_price=models.IntegerField()
    d_num=models.IntegerField(default=0)



