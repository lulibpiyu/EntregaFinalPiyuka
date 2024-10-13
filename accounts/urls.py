from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    #path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
]