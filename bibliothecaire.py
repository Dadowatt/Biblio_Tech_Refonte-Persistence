from membre import Membre
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
        """
        Permet à un membre d'emprunter un document.
        Vérifie que le membre existe, le document existe et que le document est disponible
        """

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
        """
        Gère le retour d'un document emprunté par un membre.
        Vérifie que le membre et le document existent et que le document a bien été emprunté.
        """
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
        
    def afficher_documents(self):
        """Affiche tous les documents du catalogue avec leur statut"""
        if not self.catalogue:
            print("Aucun document dans le catalogue.")
            return

        print("\n--- Liste des documents ---")
        for doc in self.catalogue:
            """appelle __str__ de Livre ou Magazine automatiquement"""
            print(doc)

    
    def afficher_membres(self):
        if not self.membres:
            print("Aucun membre inscrit.")
            return

        print("\n--- Liste des membres ---")
        for membre in self.membres:
            print(f"Membre : {membre.nom} - Emprunts : {len(membre.liste_emprunts)} document(s)")
        for doc in membre.liste_emprunts:
            """__str__ appelé automatiquement"""
            print(f"   - {doc}")