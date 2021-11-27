from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from .models import Article
from django.core.mail import send_mail
import math
from django.conf import settings

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

def About(request):
    return render(request, 'spilled_bits/about.html')

def SendMail(request):

    if request.method == "POST":
        sender = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        content = f"From: {sender}\n{message}"
        send_mail(subject, content, settings.EMAIL_HOST_USER, ['faturahman.ivan5@gmail.com',], fail_silently=False,)

        return redirect('home')

    return render(request, 'spilled_bits/mail.html')