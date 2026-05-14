from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
@login_required
def addBlog(request):
    if(request.method=="POST"):
        title=request.POST.get("title")
        description=request.POST.get("description")
        image=request.FILES.get("image")
        blog=Blog(title=title,description=description,user=request.user,image=image)
        blog.save()
        return redirect("/home")

    return render(request,"addblog.html")

@login_required
def allBlogs(request):
    srch=request.GET.get("srch")
    if(srch):
        blogs=Blog.objects.filter(title__icontains=srch)
        return render(request,"allblogs.html",{"blogs":blogs,"srch":srch})
    
    blogs=Blog.objects.all()
    return render(request,"allblogs.html",{"blogs":blogs})

@login_required
def myblogs(request):
    blogs=Blog.objects.filter(user=request.user)
    return render(request,"myblogs.html",{"blogs":blogs})

@login_required
def deleteBlog(request, id):
    blog = get_object_or_404(Blog, id=id, user=request.user)
    if request.method == "POST":
        blog.delete()
    return redirect(request.POST.get("next") or "/my-blogs")
