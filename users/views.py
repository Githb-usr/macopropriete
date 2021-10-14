from django.shortcuts import render

def ValidateUserAccountView(request):
    # récupérer le user à partir du pk
    # vérifier si le user existe et s'il existe, vérifier si son statut est bien "pending"
        # si compte n'existe pas, rediriger vers une page vers une page "échec de la validation de votre compte"
        # si statut déjà validé, rediriger sur la page de login
    # faire passer le statut de pending à validated
    # enregistrer la maj du user
    # rediriger vers la page de validation du compte
    # à partir de cette page, rediriger vers la page de login après qq secondes (JS)
    pass
