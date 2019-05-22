"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'),
    path('blog/home/', blog.views.home, name='home'),
    path('blog/new/', blog.views.new, name='new'),
    path('blog/create/', blog.views.create, name='create'),
    path('blog/newblog/', blog.views.blogform, name='newblog'),
    path('blog/<int:pk>/edit/', blog.views.edit, name='edit'),
    path('blog/<int:pk>/remove/', blog.views.remove, name='remove'),
    path("blog/<int:title_id>/detail", blog.views.detail, name="detail"),
    path("blog/<int:title_id>/detail/edit_comm/", blog.views.edit_comm, name="edit_comm"),
    path('blog/<int:pk>/remove_comm/', blog.views.remove_comm, name='remove_comm'),
]
