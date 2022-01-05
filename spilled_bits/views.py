from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Article
from django.core.mail import send_mail
import math
from django.conf import settings
import dns

def Home(request):

    articles = Article.objects.filter(status='Publish').order_by('-date')[:3]
    context = {
        'articles':articles,
    }

    return render(request, 'spilled_bits/home.html', context)

def ArticleView(request, slug, pageNow):

    post = get_object_or_404(Article, slug=slug)

    context = {
        "post": post,
        "page": pageNow
    }

    return render(request, 'spilled_bits/article.html', context)

def NewArticleView(request, slug):
    post = get_object_or_404(Article, slug=slug)

    context = {
        "post": post,
    }

    return render(request, 'spilled_bits/article.html', context)

def AllPosts(request, page):

    #Putting articles in pages
    posts = Article.objects.filter(status='Publish').count()
    itemSizePerPage = 5
    itemStart = (page-1) * itemSizePerPage
    itemEnd = itemStart + itemSizePerPage
    totalPageSize = math.ceil(posts/itemSizePerPage)
    paginatedItems = Article.objects.filter(status='Publish').order_by('-date')[itemStart:itemEnd] #Slicing QuerySet to return specific set of items 

    #Limiting pages to show
    limitPage = math.floor(page/5)
    if page%5 == 0:
        limitPage = limitPage-1

    startingPage = limitPage*5+1
    showedPages = (limitPage+1)*5 #last page for this page cluster

    nextShowedPages = 0 #Check if there is still more pages to show
    if showedPages < totalPageSize:
        nextShowedPages = showedPages+1

    prevShowedPages = 0 #Check if there is more pages in the previous
    if limitPage != 0:
        prevShowedPages = startingPage-1

    listPages = list() #Indexing showed cluster of pages
    if showedPages < totalPageSize:
        for startingPage in range(startingPage-1, showedPages):
            listPages.append(startingPage+1)
    elif showedPages > totalPageSize:
        for startingPage in range(startingPage-1, totalPageSize):
            listPages.append(startingPage+1)

    context = {
        'showedPages':showedPages,
        'nextShowedPages':nextShowedPages,
        'prevShowedPages':prevShowedPages,    
        'limitPage':limitPage,
        'listPages':listPages,
        'totalPageSize':totalPageSize,
        'paginatedItems': paginatedItems,
        'pageNow': page,
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