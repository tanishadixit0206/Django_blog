from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# from .models import User
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Create your views here.
# "@csrf_protect
# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('blog_app:post_list')
#         else: print("error")
#     return render(request, 'authentication/login.html')
# @csrf_protect
# def signup_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = User.objects.create(username=username, password=password)
#         if not User.objects.filter(username=username).exists():
#             user.save()
#         return redirect('authentication:login')
#     return render(request, 'authentication/signup.html')"

class login_view(LoginView):
    template_name = 'authentication/login.html'

class signup_view(CreateView):
    template_name = 'authentication/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Assuming the URL name for the login page is 'login'

    def form_valid(self, form):
        response = super().form_valid(form)
        if response.status_code == 200:
            return HttpResponseRedirect(self.get_success_url())
        return response