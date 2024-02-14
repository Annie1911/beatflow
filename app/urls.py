from django.urls import path
from . import views
from .views import accueil
from .views import connexion
from .views import deconnexion
from .views import interface
from .views import profils 
from .views import create_content

urlpatterns = [ path('', views.accueil, name='accueil'),
path('inscription/', views.inscription, name='inscription'),
path('connexion/', connexion, name='connexion'),
path('deconnexion/', deconnexion, name='deconnexion'),
path('interface/', interface, name='interface'),
path('profils/', profils, name='profils'),
path('create_content/', create_content, name='create_content'),
]


