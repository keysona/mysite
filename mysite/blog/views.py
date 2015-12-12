from django.shortcuts import render
from django.http import Http404,HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Article,Tag

# Create your views here.
def direct_to_template(requests,template_name,**kwargs):
    objects = kwargs.get('objects',None)
    if not objects:
        raise Http404("你来到了一片荒芜之地")
    elif hasattr(objects,'__len__'):
        paginator = Paginator(objects,5)
        page = requests.GET.get('page')
        try:
            print(1)
            objects = paginator.page(page)
            print(objects.object_list)
            print(2)
        except PageNotAnInteger:
            objects = paginator.page(1)
            print(objects.object_list)
        except EmptyPage:
            objects = paginator.page(paginator.num_pages)
    kwargs['objects'] = objects
    return render(requests,template_name,kwargs)

def get_args(requests,*args,**kwargs):
    title = kwargs.get('title',None)
    tag = kwargs.get('tag',None)
    template_name = kwargs.get('template_name')
    objects = None
    tags = None
    try:
        if title:
                objects = Article.objects.get(title=title)
                objects.hit_count += 1
                objects.save()
        elif tag:
                objects = Tag.objects.get(name=tag).article_set.all()
                tags = Tag.objects.all()
        else:
            objects = Article.objects.all()
            tags = Tag.objects.all()
    except ObjectDoesNotExist as e:
        raise Http404("你来到了一片荒芜之地")
    return direct_to_template(requests,template_name,**{'objects':objects,'tags':tags})

def handler404(requests):
    return render(reuqests,"404.html",{})

def handler500(requests):
    return render(reuqests,"500.html",{})
