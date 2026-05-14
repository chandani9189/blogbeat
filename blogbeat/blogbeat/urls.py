from django.contrib import admin
from django.urls import path
from userapp import views as u
from blogapp import views as b
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",u.indexView),
    path('admin/', admin.site.urls),
    path("register",u.register),
    path("accounts/login/",u.loginUser),
    path("logout",u.logoutUser),
    path("home",u.home),
    path("add-blog",b.addBlog),
    path("all-blogs",b.allBlogs),
    path("my-blogs",b.myblogs),
    path("delete-blog/<int:id>",b.deleteBlog)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
