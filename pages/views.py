from django.shortcuts import render, get_object_or_404, redirect
from .models import CodingGame
from .forms import CodingGameForm
from django.contrib.auth.decorators import login_required


def home(request):
    #games = CodingGame.objects.filter(is_enabled=True)
    games = CodingGame.objects.filter(is_enabled=True).order_by('-created_at')[:5]
    return render(request, 'home.html', {'games': games})
    #return render(request, 'pages/home.html', {'games': games})

def games_list(request):
    games = CodingGame.objects.filter(is_enabled=True) 

    difficulty = request.GET.get('difficulty')
    if difficulty:
        games = games.filter(difficulty=difficulty)

    if 'date' in request.GET:
        games = games.order_by('-created_at')

    if 'rating' in request.GET:
        games = games.order_by('-rating')

    context = {
        'games': games,
    }
    return render(request, 'pages/games_list.html', context)

def game_detail(request, game_id):
    game = get_object_or_404(CodingGame, id=game_id)
    return render(request, 'pages/games_detail.html', {'game': game}) 

@login_required 
def create_game(request):
    if request.method == 'POST':
        form = CodingGameForm(request.POST)
        if form.is_valid():
            coding_game = form.save(commit=False)
            coding_game.author = request.user
            coding_game.save()
            return redirect('some_view_name')
    else:
        form = CodingGameForm()
    
    return render(request, 'pages/create_game.html', {'form': form})

def leaderboard(request):
    return render(request, 'pages/leaderboard.html')

def announcements(request):
    return render(request, 'pages/announcements.html')

def blog(request):
    return render(request, 'pages/blog.html')

def about(request):
    return render(request, 'pages/about.html')

def juegos_nivel_facil(request):
    return render(request, 'pages/nivel_facil.html')

def juegos_nivel_intermedio(request):
    return render(request, 'pages/nivel_intermedio.html')

def juegos_nivel_avanzado(request):
    return render(request, 'pages/nivel_avanzado.html')

def modificar_contenido(request, game_id=None):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect('login') 

    game = None
    if game_id:
        game = get_object_or_404(CodingGame, id=game_id)

    form = CodingGameForm(request.POST or None, request.FILES or None, instance=game)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('games_list')

    context = {
        'form': form,
        'coding_games': CodingGame.objects.all(),
    }
    return render(request, 'media/modif_media.html', context)
