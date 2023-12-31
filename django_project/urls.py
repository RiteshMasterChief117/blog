"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns #new
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #path("", include("pages.urls")),
    path("",views.starting_page,name="starting-page"),
    path("posts",views.posts ,name="posts-page"),
    path("posts/<slug:slug>",views.post_detail ,name="post-detail-page"), #posts/my first post
]

urlpatterns += staticfiles_urlpatterns() # new
