from django.shortcuts import render
from .models import Post
# Create your views here.
def index(requst):
    posts = Post.objects.all()

    return render(requst,'/Users/sangeetha/Downloads/project1/blog/templates/index.html',{'posts' : posts})

def post(request,pk):
    posts = Post.objects.get(id=pk)
    return render(request,'/Users/sangeetha/Downloads/project1/blog/templates/post.html',{'posts' : posts})   