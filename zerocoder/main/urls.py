from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='home'),
    path('new',views.new,name='page2'),
    path('data', views.data,name='info'),
    path('test', views.test,name='test'),

]