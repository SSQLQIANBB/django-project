from django.urls import path, re_path
from . import views

 # namespace
app_name = 'tasks'

urlpatterns = [
    # Create a task
    path('create/', views.task_create, name='task_create'),

    # Retrieve task list
    path('', views.task_list, name='task_list'),

    # Retrieve single task object
    re_path(r'^(?P<pk>\d+)/$', views.task_detail, name='task_detail'),

    # Update a task
    re_path(r'^(?P<pk>\d+)/update/$', views.task_update, name='task_update'),

    # Delete a task
    re_path(r'^(?P<pk>\d+)/delete/$', views.task_delete, name='task_delete'),

    # path('article/')/

    # path('blog/<int:id>/', views.blog_detail, name='blog_detail'),  # Example of using path with type converter
    # re_path(r'^blog/(?P<id>\d+)/$', views.bog_detail, name='blog_detail_re'),  # Example of using re_path with named group


    # from django.urls import include, re_path

    # urlpatterns = [
    #     re_path(r'^blog/', include('blog.urls')), # include添加子路由
    #     ...
    # ]
]

# 更多URL配置示例
# path支持匹配的数据类型只有str,int, slug, uuid四种。一般来说re_path更强大，但写起来更复杂一些，我们来看看更多案例。

# # 示例一，PATH
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('articles/2003/', views.special_case_2003),
#     path('articles/<int:year>/', views.year_archive),
#     path('articles/<int:year>/<int:month>/', views.month_archive),
#     path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
# ]

# # 示例二：RE_PATH，与上例等同
# from django.urls import path, re_path
# from . import views

# urlpatterns = [
#     path('articles/2003/', views.special_case_2003),
#     re_path(r'^articles/(?P<year>[0-9]{4})/$', views.year_archive),
#     re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
#     re_path(r'^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$', views.article_detail),
# ]