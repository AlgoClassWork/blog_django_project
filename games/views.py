from django.views.generic import ListView, DetailView, CreateView
from .models import Game

class GameListView(ListView):
    model = Game
    template_name = 'game_list.html'
    context_object_name = 'games'
    paginate_by = 2

class GameDetailView(DetailView):
    model = Game
    template_name = 'game_detail.html'
    context_object_name = 'game'

class GameCreateView(CreateView):
    model = Game
    template_name = 'game_form.html'
    fields = ['title', 'genre', 'release_year', 'description']
