from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def games_list(request):
    return render(request, 'games_list.html')