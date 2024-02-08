from django.urls import path
from . import views
from .views import accueil
from .views import connexion 

urlpatterns = [ path('', views.accueil, name='accueil'),
path('inscription/', views.inscription, name='inscription'),
path('connexion/', connexion, name='connexion'),

]


