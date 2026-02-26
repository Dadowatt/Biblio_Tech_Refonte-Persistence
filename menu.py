from bibliothecaire import Bibliothecaire
from livre import Livre
from magazine import Magazine

def nom_valide(nom):
    if not nom:
        return False

    # doit commencer et finir par une lettre
    if not nom[0].isalpha() or not nom[-1].isalpha():
        return False

    for c in nom:
        if not (c.isalpha() or c in " -'"):
            return False
    return True

def titre_valide(titre):
    if not titre:
        return False

    # doit commencer par lettre ou chiffre
    if not titre[0].isalnum():
        return False

    # doit finir par lettre ou chiffre
    if not titre[-1].isalnum():
        return False
    
    for c in titre:
        if not (c.isalnum() or c in " .'-"):
            return False
    return True


def menu():
    """Crée un objet bibliothèque vide et gère le menu utilisateur"""
    biblio = Bibliothecaire()

    # Charger les données depuis la base
    biblio.charger_documents()
    biblio.charger_membres()
    biblio.charger_emprunts()

    while True:
        print("\n=== BIBLIOTHÈQUE ===")
        print("1. Ajouter document")
        print("2. Inscrire membre")
        print("3. Prêter document")
        print("4. Retourner document")
        print("5. Quitter")
        print("6. Afficher tous les documents")
        print("7. Afficher tous les membres et leurs emprunts")

        choix = input("Choix : ").strip()

        match choix:

            case "1":
                while True:
                    type_doc = input("Saisir le type (livre/magazine) : ").strip().lower()
                    if type_doc in ["livre", "magazine"]:
                        break
                    print("Type invalide, veuillez ressayer")
        
                while True:
                    titre = input("Saisir le titre : ").strip()
                    if nom_valide(titre):
                        break
                    print("Titre invalide, veuillez ressayer")

                if type_doc == "livre":
                    while True:
                        auteur = input("Saisir le nom de l'auteur : ").strip()
                        if nom_valide(auteur):
                            break
                        print("Auteur invalide, veuillez saisir un nom valide")     
                    doc = Livre(titre, auteur)
                else:
                    while True:
                        numero = input("Saisir le numéro : ").strip()
                        if numero.isdigit():
                            numero = int(numero)
                            break
                        print("Le numéro doit être un entier")
                           
                    doc = Magazine(titre, int(numero))

                biblio.ajouter_document(doc)
                print("Document ajouté avec succès")

            case "2": 
                while True:
                    nom = input("Saisir le nom du membre : ").strip()
                    if nom_valide(nom):
                        break
                    print("Nom invalide, veuillez ressayer")

                biblio.inscrire_membre(nom)
                print("Membre inscrit avec succès")

            case "3": 
                while True:
                    nom = input("Saisissez le nom du membre : ").strip()
                    if nom_valide(nom):
                        break
                    print("Nom invalide, saisissez des lettres uniquement")

                while True:
                    titre = input("Saisissez le titre du document : ").strip()
                    if nom_valide(titre):
                        break
                    print("Titre invalide, caractères interdits ou champ vide")

                try:
                    biblio.valider_pret(nom, titre)
                    print("Prêt validé")
                except ValueError as e:
                    print("Erreur :", e)

            case "4": 
                while True:
                    nom = input("Saisir le nom du membre : ").strip()
                    if nom_valide(nom):
                        break
                    print("Nom invalide, caractères interdits ou champ vide")

                while True:
                    titre = input("Saisir le titre du document : ").strip()
                    if nom_valide(titre):
                        break
                    print("Titre invalide, champ vide interdit")

                try:
                    biblio.retour_document(nom, titre)
                    print("Document retourné avec succès")
                except ValueError as e:
                    print("Erreur :", e)

            case "6":
                """Afficher tous les documents"""
                biblio.afficher_documents()

            case "7":
                """Afficher tous les membres et leurs emprunts"""
                biblio.afficher_membres()

            case "5":  
                print("Au revoir !")
                break

            case _: 
                print("Choix invalide")