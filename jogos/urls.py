from django.urls import path

from . import views

app_name = 'jogos'

urlpatterns = [
    path('', views.home, name="home"),
    path('jogos/<category_id>/', views.category, name="category"),
    path('jogos/category/<int:category_id>/', views.category, name="category"),
    path('jogos/<int:id>/', views.jogos, name="jogos"),
   
    
]
