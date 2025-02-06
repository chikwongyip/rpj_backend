from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户管理'


class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = '品牌管理'


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand.name} - {self.name}"

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品管理'


class CompanyProfile(models.Model):
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '公司简介'
        verbose_name_plural = '公司简介'


class UserManual(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='manuals/videos/')
    document = models.FileField(upload_to='manuals/docs/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '使用手册'
        verbose_name_plural = '使用手册管理'
