from django.shortcuts import render

from .models import Post

# http://127.0.0.1:8000/
def home_page(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts' : posts})

# http://127.0.0.1:8000/detail/6
def post_detail(request, id):
    return render(request, 'post_detail.html')