from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('about', views.about_page, name='about_page'),
    path('contact', views.contact_page, name='contact_page'),


    
    path('thank-you/', views.thank_you, name='thank_you'),

    
    path('article/<int:article_id>/', views.article_page, name='article_page'),     
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
]

#<int:article_id>/ obtain the specific pk in the httprequest and passed it to view
#it also redirect the view to so when you click the link/article, the application redirect you to that directory