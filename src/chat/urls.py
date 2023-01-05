from django.urls import path
from django.http import HttpResponse

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('conversation/<int:conversation_id>/', views.app, name='app'),
]