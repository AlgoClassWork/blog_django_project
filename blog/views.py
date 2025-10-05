from django.shortcuts import render, get_object_or_404

from .models import Post
from .forms import PostForm

# http://127.0.0.1:8000/
def home_page(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts' : posts})

# http://127.0.0.1:8000/detail/6
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_detail.html', {'post':post})


# http://127.0.0.1:8000/create/
def post_create(request):
    form = PostForm()
    return render(request, 'post_create.html', {'form':form})
