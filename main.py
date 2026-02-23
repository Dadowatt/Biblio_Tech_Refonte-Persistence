from abc import ABC

# Class abstraite document
class Document(ABC):
    def __init__(self, titre):
        self.titre = titre
        self.__disponible = True

    @property
    def disponible(self):
        return self.__disponible

    def emprunter(self):
        if not self.__disponible:
            raise ValueError(f"le document '{self.titre}' est déjà emprunté")
        self.__disponible = False

    def retourner(self):
        if self.__disponible:
            raise ValueError(f"le document '{self.titre}' n'a pas été emprunté")
        self.__disponible = True

# class livre
class Livre(Document):
    def __init__(self, titre, auteur):
        super().__init__(titre)
        self.auteur = auteur

# class magazine
class Magazine(Document):
    def __init__(self, titre, numero):
        super().__init__(titre)
        self.numero = numero

# class membre
class Membre:
    def __init__(self, nom):
        self.nom = nom
        self.liste_emprunts = []

    def emprunter(self, document):
        self.liste_emprunts.append(document)

    def retourner(self, document):
        if document in self.liste_emprunts:
            self.liste_emprunts.remove(document)
        else:
            raise ValueError("ce document n'est pas dans la liste des emprunts")

# class bibliothèque
class Bibliothecaire:
    def __init__(self):
        self.catalogue = []
        self.membres = []

    def ajouter_document(self, document):
        self.catalogue.append(document)

    def inscrire_membre(self, nom):
        membre = Membre(nom)
        self.membres.append(membre)

    def trouver_document(self, titre):
        for document in self.catalogue:
            if document.titre == titre:
                return document
        return None

    def trouver_membre(self, nom):
        for membre in self.membres:
            if membre.nom == nom:
                return membre
        return None

    def valider_pret(self, nom_membre, titre_document):
        membre = self.trouver_membre(nom_membre)
        if membre is None:
            raise ValueError("membre introuvable")

        document = self.trouver_document(titre_document)
        if document is None:
            raise ValueError("document introuvable")

        if not document.disponible:
            raise ValueError("document déjà emprunté")

        document.emprunter()
        membre.emprunter(document)

    def retour_document(self, nom_membre, titre_document):
        membre = self.trouver_membre(nom_membre)
        if membre is None:
            raise ValueError("membre introuvable")

        document = self.trouver_document(titre_document)
        if document is None:
            raise ValueError("document introuvable")

        if document not in membre.liste_emprunts:
            raise ValueError("de document n'a pas été emprunté par ce membre")

        document.retourner()
        membre.retourner(document)

# Menu
def menu():
    biblio = Bibliothecaire()

    while True:
        print("\n===BIBLIOTHÈQUE===")
        print("1. Ajouter document")
        print("2. Inscrire membre")
        print("3. Prêter document")
        print("4. Retourner document")
        print("5. Quitter")

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
                        print("auteur invalide, saisir des lettres uniquement")
                        continue
                    doc = Livre(titre, auteur)
                else:
                    numero = input("Sasir le numéro : ").strip()
                    if not numero.isdigit():
                        print("le numéro doit être un entier")
                        continue
                    doc = Magazine(titre, int(numero))

                biblio.ajouter_document(doc)
                print("document ajouté avec succès")

            case "2":
                nom = input("Saisir le nom du membre : ").strip()
                if not nom or not nom.replace(" ", "").isalpha():
                    print("nom invalide, saisissez des lettres uniquement, et pas vide")
                    continue

                biblio.inscrire_membre(nom)
                print("membre inscrit avec succès")

            case "3":
                nom = input("saisissez le nom du membre : ").strip()
                titre = input("saissisez le titre du document : ").strip()

                if not nom or not titre:
                    print("champs vides interdits")
                    continue

                if not nom.replace(" ", "").isalpha():
                    print("nom invalide")
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
                nom = input("nom du membre : ").strip()
                titre = input("Titre du document : ").strip()

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
                    print("Document retourné")
                except ValueError as e:
                    print("Erreur :", e)

            case "5":
                print("Au revoir !")
                break
            case _:
                print("Choix invalide")
menu()