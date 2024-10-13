from django.shortcuts import render, redirect
from .models import UserMessage
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

@method_decorator(csrf_exempt, name='dispatch')
def send_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        recipient_username = data['recipient']
        message_content = data['message']
        recipient = User.objects.get(username=recipient_username)
        UserMessage.objects.create(sender=request.user, recipient=recipient, message=message_content)
        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'}, status=400)

@login_required
def message_list(request):
    messages = UserMessage.objects.filter(recipient=request.user)
    return render(request, 'message_list.html', {'messages': messages})

@login_required
def get_messages(request):
    messages = UserMessage.objects.filter(recipient=request.user).order_by('timestamp')
    return JsonResponse({'messages': list(messages.values('sender__username', 'message', 'timestamp'))})