from django.shortcuts import render, redirect
from .forms import MediaFileForm
from .models import MediaFile, Media
from django.contrib.auth.decorators import user_passes_test

# Vista para subir archivos
def upload_media(request):
    if request.method == 'POST':
        form = MediaFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('media_list')
    else:
        form = MediaFileForm()
    return render(request, 'media/upload.html', {'form': form})

# Vista para listar archivos
def media_list(request):
    files = MediaFile.objects.all()
    return render(request, 'media/list.html', {'files': files})

@user_passes_test(lambda u: u.is_superuser)
def modify_media(request):
    if request.method == 'POST':
        media_id = request.POST.get('media_id') 
        title = request.POST.get('title')
        image = request.FILES.get('image')

        try:
            media = Media.objects.get(id=media_id)
            media.title = title
            if image:
                media.image = image
            media.save()  

            return redirect('success_page') 

        except Media.DoesNotExist:
            return render(request, 'pages/error.html', {'message': 'Medio no encontrado'})
        
    else:
        media_id = request.GET.get('media_id') 
        try:
            media = Media.objects.get(id=media_id)
            return render(request, 'pages/modify_media.html', {'media': media})
        except Media.DoesNotExist:
            return render(request, 'pages/error.html', {'message': 'Medio no encontrado'})
