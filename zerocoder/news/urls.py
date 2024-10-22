from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='news_home'),
    path('news_about_Django',views.news_about_Django,name='news_Django'),
]