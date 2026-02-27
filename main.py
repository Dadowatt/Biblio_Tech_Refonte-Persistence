from auth import authentification, creer_utilisateur
from menu import menu
from database import get_cursor

if __name__ == "__main__":
    # Vérifier si un administrateur existe dans la base
    with get_cursor(dictionary=True) as curseur:
        curseur.execute("SELECT COUNT(*) AS total FROM bibliothecaire")
        result = curseur.fetchone()

    if result["total"] == 0:
        print("Aucun administrateur trouvé, veuillez Créer un compte admin.")
        email = input("Email admin : ").strip()
        mdp = input("Mot de passe admin : ").strip()
        creer_utilisateur(email, mdp)

    print("=== Connexion Bibliothécaire ===")

    while True:
        if authentification():
            print("Connexion réussie !")
            menu() 
            break
        else:
            print("Identifiants incorrects, veuillez réessayer.")