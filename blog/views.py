from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from blog.models import Blog
from django.core.paginator import Paginator

#Search
def search_view(request):
  query = request.GET.get('s', '')
  blog_lst = Blog.objects.filter(title__icontains=query) if query else Blog.objects.none
  context = {
    'blog_lst': blog_lst,
    's': query,
  }
  return render(request, template_name='blog.html', context=context)







def blog_detail(request, id):
  if request.method == 'GET':
    blog_id = get_object_or_404(Blog, id=id)
    context = {
      'blog_id': blog_id
    }
    return render(request, template_name='blog_detail.html', context=context)
  


def blog_list(request):
  if request.method == 'GET':
    blog_list = Blog.objects.all().order_by('-id')
    paginator = Paginator(blog_list, 2)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {

      'blog_lst': page_obj
      #'blog_lst': blog_list,
    }
    return render(request, template_name='blog.html', context=context)












def first_page(request):
  if request.method == 'GET':
    return HttpResponse('Привет это мой первый проект на Django!')

def text_page(request):
  if request.method == 'GET':
    return HttpResponse('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum')