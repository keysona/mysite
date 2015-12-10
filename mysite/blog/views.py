from django.shortcuts import render
from django.http import Http404,HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Article,Tag



# Create your views here.
def index(requests):
    articles = Article.objects.all()
    paginator = Paginator(articles,5)
    page = requests.GET.get('page')
    try:
        articles_list = paginator.page(page)
    except PageNotAnInteger:
        articles_list = paginator.page(1)
    except EmptyPage:
        articles_list = paginator.page(paginator.num_pages)
    return render(requests,'base.html',{'articles_list':articles_list})

def article(requests,title):
    try:
        article = Article.objects.get(title=title)
        article.hit_count += 1
        article.save()
    except ObjectDoesNotExist as e:
        raise Http404("没有这篇文章")
    return render(requests,'article.html',{'article':article})

def tags(requests,tag_name):
    try:
        articles = Tag.objects.get(name=tag_name).article_set.all()
    except ObjectDoesNotExist:
        raise Http404("没有这个标签！")
    paginator = Paginator(articles,5)
    page = requests.GET.get('page')
    try:
        articles_list = paginator.page(page)
    except PageNotAnInteger:
        articles_list = paginator.page(1)
    except EmptyPage:
        articles_list = paginator.page(paginator.num_pages)
    return render(requests,'base.html',{'articles_list':articles_list})
