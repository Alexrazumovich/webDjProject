from django.shortcuts import render
from .models import News_post,News_post_about_Django

# Create your views here.
def home(request):
    news = News_post.objects.all()

    return render(request, 'news/news.html',{'news':news})

def news_about_Django(request):
    news = News_post_about_Django.objects.all()

    return render(request, 'news/news_about_Django.html',{'news':news})
