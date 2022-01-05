from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('all-posts/page/<int:page>/', views.AllPosts, name='all_posts'),
    path('new-post/<str:slug>/', views.NewArticleView, name='new_article'),
    path('post/<str:slug>/<int:pageNow>/', views.ArticleView, name='article'),
    path('about/', views.About, name="about"),
    path('mail/', views.SendMail, name="email"),
    path('mail/feedback/<info>/', views.Feedback, name="feedback")
]

