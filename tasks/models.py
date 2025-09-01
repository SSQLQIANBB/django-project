from django.db import models
from django.urls import reverse

# Create your models here.
class Status(models.TextChoices):
    UNSTARTED = 'u', "Not started yet"
    ONGOING = 'o', "Ongoing"
    FINISHED = 'f', "Finished"
  
class Task(models.Model):
    name = models.CharField(verbose_name="Task name", max_length=65, unique=True)
    status = models.CharField(verbose_name="Task status", max_length=1, choices=Status.choices)

    def __str__(self):
        return self.name
    
class Publisher(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    add_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("books:book_detail", args=[self.id,])
    
class Article(models.Model):
    title = models.CharField('标题', max_length=100, unique=True)
    body = models.TextField('内容')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# 模型的Meta选项
# abstract=True: 指定该模型为抽象模型
# ordering=['-pub-date']: 自定义按哪个字段排序，-代表逆序
# verbose_name: 指定模型的单数名称
# verbose_name_plural: 指定模型的复数名称
# abstract=True: 指定该模型为抽象模型
# proxy=True: 指定该模型为代理模型
# db_table= xxx: 自定义数据表名
# permissions=[]: 为模型自定义权限
# managed=False: 默认为True，如果为False，Django不会为这个模型生成数据表
# indexes=[]: 为数据表设置索引，对于频繁查询的字段，建议设置索引
# constraints=: 给数据库中的数据表增加约束。