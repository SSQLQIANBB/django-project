from .models import Article
from django.shortcuts import get_object_or_404
import datetime
from django.db.models import Q, F

def execute():
    art_list = Article.objects.all()

    values = art_list.values_list('id', 'title', 'body')

    titles = art_list.values_list('title', flat=True) # flat=True: 如果只取一个字段，可以设置flat=True，返回一个扁平化列表['art1', 'art2']

    titles_distinct = art_list.values_list('title', flat=True).distinct() # distinct(): 去重

    titles_not_flat = art_list.values_list('title') # 不设置flat=True，返回一个元组列表[('art1',), ('art2',)] 

    key_values = art_list.values('id', 'title') # values(): 返回一个字典列表[{'id': 1, 'title': 'art1'}, {'id': 2, 'title': 'art2'}]

    Article.objects.get(id=1) # get(): 获取单个对象，如果不存在或存在多个会报错 <Article: art1>

    Article.objects.filter(id=1).values('id', 'title') # filter(): 获取符合条件的对象列表 <QuerySet [{'id': 7, 'title': 'art1'}]>

    art = get_object_or_404(Article, id=7) # get_object_or_404(): 获取单个对象，如果不存在返回404错误 <Article: art1>

    Article.objects.filter(id__gte=3).filter(id__lte=7) # gte: 大于等于, lte: 小于等于 <QuerySet [<Article: art3>, <Article: art4>, <Article: art5>, <Article: art6>, <Article: art7>]>

    Article.objects.exclude(id__gte=3, id__lte=7) # exclude(): 排除符合条件的对象 <QuerySet [<Article: art1>, <Article: art2>, <Article: art8>, <Article: art9>, <Article: art10>]>

    # 按范围查询
    Article.objects.filter(id__range=(3, 7)) # range: 在某个范围内 <QuerySet [<Article: art3>, <Article: art4>, <Article: art5>, <Article: art6>, <Article: art7>]>

    Article.objects.filter(id__in=[1,3,5,7,8]) # in: 在某个列表内 <QuerySet [<Article: art1>, <Article: art3>, <Article: art5>, <Article: art7>, <Article: art8>]>

    # 字符串模糊查询
    Article.objects.filter(title_icontains='art') # icontains: 包含，忽略大小写 <QuerySet [<Article: art1>, <Article: art2>, <Article: art3>, <Article: art4>, <Article: art5>, <Article: art6>, <Article: art7>, <Article: art8>, <Article: art9>, <Article: art10>]>
    Article.objects.filter(title__contains='Art') # contains: 包含，区分大小写 <QuerySet []>

    Article.objects.filter(title__startswith='art1')  # startswith: 以...开头，区分大小写 <QuerySet [<Article: art1>]>
    Article.objects.filter(title__istartswith='Art1') # istartswith: 以...开头，忽略大小写 <QuerySet [<Article: art1>]>

    Article.objects.filter(title__endswith='1') # endswith: 以...结尾，区分大小写 <QuerySet [<Article: art1>]>

    # 时间查询
    Article.objects.filter(create_time__year=2024) # year: 年 <QuerySet [<Article: art1>, <Article: art2>, <Article: art3>, <Article: art4>, <Article: art5>, <Article: art6>, <Article: art7>, <Article: art8>, <Article: art9>, <Article: art10>]>
    Article.objects.filter(create_time__month=6) # month: 月 <QuerySet [<Article: art1>, <Article: art2>, <Article: art3>, <Article: art4>, <Article: art5>, <Article: art6>, <Article: art7>, <Article: art8>, <Article: art9>, <Article: art10>]>
    Article.objects.filter(create_time__day=24) # day: 日 <QuerySet [<Article: art1>, <Article: art2>, <Article: art3>, <Article: art4>, <Article: art5>, <Article: art6>, <Article: art7>, <Article: art8>, <Article: art9>, <Article: art10>]>
    Article.objects.filter(create_time__hour=10) # hour: 时 <QuerySet [<Article: art1>, <Article: art2>, <Article: art3>, <Article

    Article.objects.filter(create_time__date=datetime.date(2025, 6, 24)) # date: 日期 <QuerySet [<Article: art1>, <Article: art2>, <Article: art3>, <Article: art4>, <Article: art5>, <Article: art6>, <Article: art7>, <Article: art8>, <Article: art9>, <Article: art10>]>
    Article.objects.filter(create_time__gt=datetime.date(2021, 1, 1)) # gt: 大于 <QuerySet [<Article: art1>, <Article: art2>, <Article: art3>, <Article: art4>, <Article: art5>, <Article: art6>, <Article: art7>, <Article: art8>, <Article: art9>, <Article: art10>]>
    Article.objects.filter(create_time__lt=datetime.date(2026, 1, 1)) # lt: 小于 <QuerySet [<Article: art1>, <Article: art

    Article.objects.filter(create_time__gte=datetime.date(2025, 7, 30), update_time__lte=datetime.date(2025, 8, 1)) # gte: 大于等于, lte: 小于等于

    # 排序
    Article.objects.all().order_by('id') # 按id升序
    Article.objects.all().order_by('-id') # 按id降序
    Article.objects.all().order_by('create_time', '-id') # 先按create_time升序，再按id降序

    # 计数
    Article.objects.count() # 计数 10

    # 切片
    Article.objects.all()[:1] # 切片，获取前1个对象 <QuerySet [<Article: art1>]>
    Article.objects.order_by('-id')[:1]

    # 去重
    Article.objects.values('body').distinct() # distinct(): 去重 <QuerySet [{'body': 'content1'}, {'body': 'content2'}, {'body': 'content3'}, {'body': 'content4'}, {'body': 'content5'}]>

    Article.objects.values('body').distinct()

    # 复杂查询
    Article.objects.filter(Q(id__gt=3) & Q(id__lt=7))
    Article.objects.filter(Q(title__contains='art2') | Q(title__contains='art1'))
    Article.objects.filter(~Q(id__gt=7)) # ~Q(): 非
    Article.objects.filter(~Q(id=7))

    Article.objects.filter(id__gt=F('count') + 2) # F(): 字段间比较 id__gt=F('count') + 2 