from django.shortcuts import render, redirect
from .forms import InscriptionForm
from django.contrib.auth import authenticate, login

def accueil(request):
    return render(request, 'acceuil.html')

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
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
                error_message = "Nom d'utilisateur ou mot de passe incorrect."
                return render(request, 'connexion.html', {'error_message': error_message})
        else:
            # Si l'username ou le mot de passe est manquant, afficher un message d'erreur
            error_message = "Veuillez entrer un nom d'utilisateur et un mot de passe."
            return render(request, 'connexion.html', {'error_message': error_message})
    else:
        return render(request, 'connexion.html')
