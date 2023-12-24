from django.db import models


class customerinfo(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20)
    user_email = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    gender = models.CharField(max_length=20, default="未填写")
    tel_number = models.CharField(max_length=20, default="未填写")
    address = models.CharField(max_length=100, default="未填写")
    true_name = models.CharField(max_length=20, default="未填写")
    money = models.CharField(max_length=20, default="0")


class sellerinfo(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20)
    user_email = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    id_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=20, default="未填写")
    tel_number = models.CharField(max_length=20, default="未填写")
    address = models.CharField(max_length=100, default="未填写")
    true_name = models.CharField(max_length=20, default="未填写")


class Image(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='static/form')


STATUS_CHOICES = [
    ('ON', '上架'),
    ('OFF', '下架')
]


class goodinfo(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='static/form')
    price = models.CharField(max_length=20)
    introduction = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    label = models.CharField(max_length=20)
    seller = models.ForeignKey("sellerinfo", on_delete=models.CASCADE)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES,default='下架')
