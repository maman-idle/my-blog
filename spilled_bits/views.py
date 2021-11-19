from django.http import request
from django.shortcuts import get_object_or_404, render
from .models import Article
import math

def Home(request):

    articles = Article.objects.order_by('-date')[:3]
    context = {
        'articles':articles,
    }

    return render(request, 'spilled_bits/home.html', context)


def ArticleView(request, slug):

    post = get_object_or_404(Article, slug=slug)
    context = {
        "post": post,
    }


    return render(request, 'spilled_bits/article.html', context)


def AllPosts(request, page):

    posts = Article.objects.all().count()
    itemSizePerPage = 5
    itemStart = (page-1) * itemSizePerPage
    itemEnd = itemStart + itemSizePerPage
    pageSize = math.ceil(posts/itemSizePerPage)

    paginatedItems = Article.objects.all()[itemStart:itemEnd] #Slicing QuerySet to return specific set of items 

    context = {
        'pageSize':pageSize,
        'paginatedItems': paginatedItems
    }

    return render(request, 'spilled_bits/all_posts.html', context)