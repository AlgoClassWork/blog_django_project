from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

from .models import Post
from .forms import PostForm, UserRegisterForm

# http://127.0.0.1:8000/
def home_page(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts' : posts})

# http://127.0.0.1:8000/detail/6
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    post.view_count += 1
    post.save( update_fields=['view_count'] )
    return render(request, 'post_detail.html', {'post':post})

# http://127.0.0.1:8000/create/
@login_required
def post_create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home_page')

    return render(request, 'post_create.html', {'form':form})

# http://127.0.0.1:8000/create/
@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if post.author == request.user:
        post.delete()
    return redirect('home_page')

# http://127.0.0.1:8000/register/
def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home_page')

    return render(request, 'register.html', {'form' : form})
