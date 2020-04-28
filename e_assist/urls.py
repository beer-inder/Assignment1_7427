from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='e_assist-home'),
    path('about/', views.about, name='e_assist-about'),
]