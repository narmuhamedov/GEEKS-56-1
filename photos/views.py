from django.shortcuts import render
from photos.models import Tag, Photo


def all_photo(request):
  if request.method == 'GET':
    all_photo = Photo.objects.all()
    context = {
      'all_photo': all_photo
    }
  return render(request, template_name='all_photo.html', context=context)


def picknick(request):
  if request.method == 'GET':
    picknick = Photo.objects.filter(tags__name='#Пикник')
    context = {
      'picknick': picknick,
    }
  return render(request, template_name='picknick.html', context=context)