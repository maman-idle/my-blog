from django.http import request
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Article
from django.core.mail import send_mail
import math
from django.conf import settings

import dns
from dns import resolver

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

    paginatedItems = Article.objects.all().order_by('-date')[itemStart:itemEnd] #Slicing QuerySet to return specific set of items 

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

        domain_name = sender.split('@')[1]
        resolver = dns.resolver.Resolver()
        resolver.nameserver = ['8.8.8.8']
        try: #check wether the email domain is valid or not
            resolver.resolve(domain_name, 'MX')
        except:
            return redirect(reverse('feedback', kwargs={'info':'Invalid Domain'}))

        content = f"From: {sender}\n{message}"
        send_mail(subject, content, settings.EMAIL_HOST_USER, ['faturahman.ivan5@gmail.com',], fail_silently=False,)

        return redirect(reverse('feedback', kwargs={'info':"Thank You for Your Input",}))

    return render(request, 'spilled_bits/mail.html')

def Feedback(request, info):
    context = {
        'info':info
    }
    return render(request, 'spilled_bits/mail_respond.html', context)

def PageNotFound(request, exception):
    return render(request, 'common/404.html', status=404)