from django.urls import path
from .views import send_message, message_list, get_messages

urlpatterns = [
    path('send/', send_message, name='send_message'),
    path('messages/', message_list, name='message_list'),
    path('get-messages/', get_messages, name='get_messages'),
]