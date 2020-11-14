from django.shortcuts import render
from .models import Article, Comment
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
def index(request):
    print(Article.objects.order_by('-pub_date'))
    latest = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html',{'latest': latest})

def detail(request, article_id):
    try:
        a = Article.objects.get( id = article_id )
    except:
        raise Http404("Статья не найдена")

    latest_comment_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'articles/detail.html', {'article':a, 'latest_comment_list':latest_comment_list})

def leave_comment(request, article_id):
    try:
        a = Article.objects.get( id = article_id )
    except:
        raise Http404("Статья не найдена")

    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'], )

    return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)))