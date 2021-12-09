from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_posts),
    path('comments/', views.comments),
]
