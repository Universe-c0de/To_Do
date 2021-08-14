from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('create', views.create, name='create'),
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
]