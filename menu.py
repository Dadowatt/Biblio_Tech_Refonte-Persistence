from bibliothecaire import Bibliothecaire
from livre import Livre
from magazine import Magazine

def menu():
    """Crée un objet bibliothèque vide et gère le menu utilisateur"""
    biblio = Bibliothecaire()

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
                type_doc = input("Saisir le type (livre/magazine) : ").strip().lower()
                if type_doc not in ["livre", "magazine"]:
                    print("Type invalide")
                    continue

                titre = input("Saisir le titre : ").strip()
                if not titre or not titre.replace(" ", "").isalpha():
                    print("Titre invalide, saisissez des lettres uniquement, et pas vide")
                    continue

                if type_doc == "livre":
                    auteur = input("Saisir le nom de l'auteur : ").strip()
                    if not auteur or not auteur.replace(" ", "").isalpha():
                        print("Auteur invalide, saisir des lettres uniquement")
                        continue
                    doc = Livre(titre, auteur)
                else:
                    numero = input("Saisir le numéro : ").strip()
                    if not numero.isdigit():
                        print("Le numéro doit être un entier")
                        continue
                    doc = Magazine(titre, int(numero))

                biblio.ajouter_document(doc)
                print("Document ajouté avec succès")

            case "2": 
                nom = input("Saisir le nom du membre : ").strip()
                if not nom or not nom.replace(" ", "").isalpha():
                    print("Nom invalide, saisissez des lettres uniquement, et pas vide")
                    continue

                biblio.inscrire_membre(nom)
                print("Membre inscrit avec succès")

            case "3": 
                nom = input("Saisissez le nom du membre : ").strip()
                titre = input("Saisissez le titre du document : ").strip()

                if not nom or not titre:
                    print("Champs vides interdits")
                    continue

                if not nom.replace(" ", "").isalpha():
                    print("Nom invalide")
                    continue

                if not titre.replace(" ", "").isalpha():
                    print("Titre invalide")
                    continue

                try:
                    biblio.valider_pret(nom, titre)
                    print("Prêt validé")
                except ValueError as e:
                    print("Erreur :", e)

            case "4": 
                nom = input("Saisir le nom du membre : ").strip()
                titre = input("Saisir le titre du document : ").strip()

                if not nom or not titre:
                    print("Champs vides interdits")
                    continue

                if not nom.replace(" ", "").isalpha():
                    print("Nom invalide")
                    continue

                if not titre.replace(" ", "").isalpha():
                    print("Titre invalide")
                    continue

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