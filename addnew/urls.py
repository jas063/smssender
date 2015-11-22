__author__ = 'Jasmeet'
from django.conf.urls import url
from addnew import views

urlpatterns=[url(r'^adduser/$',views.adduserview,name="add_user"),
             url(r'^index/$',views.indexview,name="index_view"),
             url(r'^delete/(?P<id>\d+)/$', views.delete, name='delete'),
             url(r'^sms/$',views.smsview,name="sms_view"),
              url(r'^api/$',views.apikeyview,name="apikey_view"),
             url(r'^notifications/$',views.notifyview,name="notify_view"),
              url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit_view'),
             url(r'^login/$', views.login_user),
             url(r'^passchange/(?P<user>\w+)/$', views.changepassword),
             url(r'^logout/$', views.logout_user),
             url(r'^scheduler/$', views.scheduler),

]