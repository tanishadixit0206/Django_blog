from django.urls import path
from . import views

app_name="authentication"
urlpatterns = [
    path('login/', views.login_view.as_view(), name='login'),
    path('signup/', views.signup_view.as_view(), name='signup'),
]