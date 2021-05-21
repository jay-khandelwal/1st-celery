from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
   # path('', views.GenerateRandomUserView.as_view()),
]
