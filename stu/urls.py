#coding =utf-8

from django.conf.urls import url
from stu import views


urlpatterns = [

    url('^$', views.index_view),
    url('^show/$', views.show_view),
    url('^login/$', views.login_view),
    # url('^login/', views.login_view)


]