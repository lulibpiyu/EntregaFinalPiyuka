from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.games_list, name='games_list'),
    path('games/<int:game_id>/', views.game_detail, name='game_detail'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('announcements/', views.announcements, name='announcements'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('games/create/', views.create_game, name='create_game'),
    path('games/<str:nivel>/', views.games_list, name='games_list_filtrados'), 
    path('modificar_contenido/<int:game_id>/', views.modificar_contenido, name='modificar_contenido'),
    path('modificar_contenido/', views.modificar_contenido, name='modificar_contenido'),
]
