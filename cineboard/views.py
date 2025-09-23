from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models, forms
from django.http import HttpResponse


#пункт 2 
class CreateFilmView(generic.CreateView):
    model = models.Films
    form_class = forms.FilmsForm
    template_name = 'cineboard/createFilm.html'
    success_url = '/all_films/'












#пункт 1 с регистрацией
class RegisterView(generic.View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, template_name='cineboard/register_cine.html', context={'form':form})
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login_cine/')
        return render(request, template_name='cineboard/register_cine.html', context={'form': form})
    

class AuthLoginView(generic.View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'cineboard/login_cine.html', {'form':form})
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('cineboard:all_films')
        return render(request, 'cineboard/login_cine.html', {'form':form})


class AllFilmsListView(LoginRequiredMixin, generic.ListView):
    model = models.Films
    template_name = 'cineboard/tv_list.html'
    context_object_name = 'tv_lst'


class AuthLogoutView(generic.View):
    def get(self, request):
        logout(request)
        return redirect('cineboard:login_cine')
