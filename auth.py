import bcrypt
from database import get_cursor

def authentification():
    """Demande l'email et le mot de passe, et vérifie dans la table bibliothecaire.
    Retourne True si authentification réussie, False sinon."""

    email = input("Email : ").strip()
    mdp = input("Mot de passe : ").strip().encode("utf-8")

    with get_cursor(dictionary=True) as curseur:
        curseur.execute(
            "SELECT mot_de_passe_hash FROM bibliothecaire WHERE email=%s",
            (email,)
        )
        result = curseur.fetchone()

        if not result:
            print("Accès refusé : email incorrect")
            return False

        hashed = result["mot_de_passe_hash"].encode("utf-8")

        if not bcrypt.checkpw(mdp, hashed):
            print("Accès refusé : mot de passe incorrect")
            return False

    return True


def creer_utilisateur(email, mot_de_passe):
    """Crée un administrateur uniquement si aucun admin n'existe.
    Retourne True si création réussie, False sinon."""
    
    mot_de_passe = mot_de_passe.encode("utf-8")
    hashed = bcrypt.hashpw(mot_de_passe, bcrypt.gensalt()).decode()

    with get_cursor(dictionary=True) as curseur:
        # Vérifier si un admin existe déjà
        curseur.execute("SELECT COUNT(*) AS total FROM bibliothecaire")
        result = curseur.fetchone()

        if result["total"] >= 1:
            print("Un administrateur existe déjà.")
            return False

        curseur.execute(
            "INSERT INTO bibliothecaire (email, mot_de_passe_hash) VALUES (%s, %s)",
            (email, hashed)
        )

    print("Administrateur créé avec succès.")
    return True