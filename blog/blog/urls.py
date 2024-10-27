from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    #include the blog_app urls.py
    path('', include('blog_app.urls')),
    
]
 