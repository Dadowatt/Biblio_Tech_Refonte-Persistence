from membre import Membre
import persistance

class Bibliothecaire:
    def __init__(self):
        self.catalogue = []
        self.membres = []

    # chargement
    def charger_documents(self):
        """Charge tous les documents depuis la base"""
        self.catalogue = persistance.charger_documents()

    def charger_membres(self):
        """Charge tous les membres depuis la base"""
        self.membres = persistance.charger_membres()

    def charger_emprunts(self):
        """
        Charge tous les emprunts depuis la base.
        On passe self.membres et self.catalogue pour que la fonction puisse relier
        chaque emprunt à l'objet Membre et l'objet Document correspondant.
        """
        persistance.charger_emprunts(self.membres, self.catalogue)

    # ajout et sauvegarde
    def sauvegarder_document(self, document):
        persistance.sauvegarder_document(document)
        if document not in self.catalogue:
            self.catalogue.append(document)

    def ajouter_document(self, document):
        """Ajoute un document à la bibliothèque et le sauvegarde dans la base"""
        self.sauvegarder_document(document)

    def sauvegarder_membre(self, membre):
        persistance.sauvegarder_membre(membre)
        if membre not in self.membres:
            self.membres.append(membre)

    def inscrire_membre(self, nom):
        """Inscrit un membre dans la bibliothèque et la base"""
        membre = Membre(nom)
        self.sauvegarder_membre(membre)

    def sauvegarder_emprunt(self, membre, document):
        persistance.sauvegarder_emprunt(membre, document)

    def supprimer_emprunt(self, membre, document):
        persistance.supprimer_emprunt(membre, document)

    #recherche
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

    #gestion des emprunts
    def valider_pret(self, nom_membre, titre_document):
        membre = self.trouver_membre(nom_membre)
        if membre is None:
            raise ValueError("Membre introuvable")

        document = self.trouver_document(titre_document)
        if document is None:
            raise ValueError("Document introuvable")

        if not document.disponible:
            raise ValueError("Document déjà emprunté")

        document.emprunter()
        membre.emprunter(document)
        self.sauvegarder_emprunt(membre, document)

    def retour_document(self, nom_membre, titre_document):
        membre = self.trouver_membre(nom_membre)
        if membre is None:
            raise ValueError("Membre introuvable")

        document = self.trouver_document(titre_document)
        if document is None:
            raise ValueError("Document introuvable")

        if document not in membre.liste_emprunts:
            raise ValueError("Document n'a pas été emprunté par ce membre")

        document.retourner()
        membre.retourner(document)
        self.supprimer_emprunt(membre, document)

    #affichage
    def afficher_documents(self):
        if not self.catalogue:
            print("Aucun document dans le catalogue.")
            return
        print("\n===Liste des documents===")
        print()
        for doc in self.catalogue:
            print(doc)

    def afficher_membres(self):
        if not self.membres:
            print("Aucun membre inscrit.")
            return
        print("\n===Liste des membres===")
        print()
        for membre in self.membres:
            print('='*60)
            print(f"Membre : {membre.nom} -> Emprunts : {len(membre.liste_emprunts)} document(s)")
            for doc in membre.liste_emprunts:
                print()
                print(f"   - {doc}")