from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class TagModel(models.Model):
    name = models.CharField(max_length=64,verbose_name='标签')
    create_time = models.DateTimeField(default=now,verbose_name='创建时间')

    def __str__(self):
        return '标签名:{}'.format(self.name)
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签名称'


class BlogModel(models.Model):
    user = models.ForeignKey(to=User,related_name='blogs',on_delete=models.CASCADE)
    title = models.CharField(default='',max_length=64,verbose_name='标题')
    content = models.TextField(default='',verbose_name='内容')
    create_time = models.DateTimeField(default=now,verbose_name='创建时间')
    tags = models.ManyToManyField(to=TagModel,verbose_name='标签',related_name='bolgs')

    def __str__(self):
        return '作者:{} 标题:{} 标签:{}'.format(self.user.username,self.title)

    class Meta:
        verbose_name = '博客'
        verbose_name_plural = '博客名称'