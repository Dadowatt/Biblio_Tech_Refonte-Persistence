from bibliothecaire import Bibliothecaire
from bibliotheque import Bibliotheque
from gestion_emprunt import GestionEmprunt
from membre import Membre
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
    
    """ Crée la bibliothèque et le service de gestion des emprunts """
    biblio_obj = Bibliotheque()
    biblio_obj.charger_documents()
    biblio_obj.charger_membres()
    biblio_obj.charger_emprunts()
    gestion_emprunt = GestionEmprunt()
    biblio = Bibliothecaire(biblio_obj, gestion_emprunt)

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
                    if titre_valide(titre):
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
                    nom_membre = input("Saisir le nom du membre : ").strip()
                    if nom_valide(nom_membre):
                        break
                    print("Nom invalide, veuillez ressayer")
                nouveau_membre = Membre(nom_membre)
                biblio.inscrire_membre(nouveau_membre)
                print("Membre inscrit avec succès")

            case "3": 
                while True:
                    nom_membre = input("Saisissez le nom du membre : ").strip()
                    if nom_valide(nom_membre):
                        break
                    print("Nom invalide, saisissez des lettres uniquement")

                while True:
                    titre_doc = input("Saisissez le titre du document : ").strip()
                    if titre_valide(titre_doc):
                        break
                    print("Titre invalide, caractères interdits ou champ vide")

                try:
                    biblio.valider_pret(nom_membre, titre_doc)
                    print("Prêt validé")
                except ValueError as e:
                    print("Erreur :", e)

            case "4": 
                while True:
                    nom_membre = input("Saisir le nom du membre : ").strip()
                    if nom_valide(nom_membre):
                        break
                    print("Nom invalide, caractères interdits ou champ vide")

                while True:
                    titre_doc = input("Saisir le titre du document : ").strip()
                    if titre_valide(titre_doc):
                        break
                    print("Titre invalide, champ vide interdit")

                try:
                    biblio.retour_document(nom_membre, titre_doc)
                    print("Document retourné avec succès")
                except ValueError as e:
                    print("Erreur :", e)

            case "6":
                """Afficher tous les documents"""
                biblio.bibliotheque.afficher_documents()

            case "7":
                """Afficher tous les membres et leurs emprunts"""
                biblio.bibliotheque.afficher_membres()

            case "5":  
                print("Au revoir !")
                break

            case _: 
                print("Choix invalide")