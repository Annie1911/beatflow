from django.shortcuts import render, redirect
from .forms import InscriptionForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


def accueil(request):
    return render(request, 'acceuil.html')

def interface(request):
    return render(request, 'interface.html')

def profils(request):
    return render(request, 'profile.html')

def create_content(request):
    return render(request, 'create_content.html')


def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            # Enregistrez l'utilisateur et ses informations supplémentaires ici
            # Assurez-vous d'importer les modèles nécessaires
            form.save()
            return redirect('accueil')  
    else:
        form = InscriptionForm()
    return render(request, 'inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Vérifier si l'username et le mot de passe sont rentrés
        if username and password:
            # Authentification de l'utilisateur
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Si l'authentification réussit, connecter l'utilisateur
                login(request, user)
                return redirect('accueil')  # Rediriger l'utilisateur vers la page d'accueil
            else:
                # Si l'authentification échoue, afficher un message d'erreur
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
                return render(request, 'connexion.html')
        else:
            # Si l'username ou le mot de passe est manquant, afficher un message d'erreur
            messages.error(request, "Veuillez entrer un nom d'utilisateur et un mot de passe.")
            return render(request, 'connexion.html')
    else:
        return render(request, 'connexion.html')
        
def deconnexion(request):
    logout(request)
    return redirect('accueil')



