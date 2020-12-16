from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.

def all_post(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'post/all_post.html', context)

def post_detail(request,year,month,day,slug):
    post= get_object_or_404(Post,created__year=year,created__month=month,created__day=day,slug=slug)
    return render(request,'post/post_detail.html',{'post':post})

