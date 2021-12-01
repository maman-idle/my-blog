from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('all-posts/page/<int:page>/', views.AllPosts, name='all_posts'),
    path('post/<str:slug>/', views.ArticleView, name='article'),
    path('about/', views.About, name="about"),
    path('mail/', views.SendMail, name="email"),
    path('mail/feedback/<info>/', views.Feedback, name="feedback")
]

