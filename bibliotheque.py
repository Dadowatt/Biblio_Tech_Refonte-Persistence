from membre import Membre
import persistance

class Bibliotheque:
    def __init__(self):
        self.catalogue = []
        self.membres = []


    def ajouter_document(self, document):
        self.catalogue.append(document)
        persistance.sauvegarder_document(document)


    def trouver_document(self, titre):
        return next((d for d in self.catalogue if d.titre == titre), None)


    def inscrire_membre(self, membre):
        self.membres.append(membre)
        persistance.sauvegarder_membre(membre)


    def trouver_membre(self, nom):
        return next((m for m in self.membres if m.nom == nom), None)


    def charger_documents(self):
        self.catalogue = persistance.charger_documents()


    def charger_membres(self):
        self.membres = persistance.charger_membres()


    def charger_emprunts(self):
        persistance.charger_emprunts(self.membres, self.catalogue)


    def afficher_documents(self):
        """Affiche tous les documents du catalogue avec leur statut"""
        if not self.catalogue:
            print("Aucun document dans le catalogue.")
            return
        print("\n=== Liste des documents ===")
        for doc in self.catalogue:
            #appelle __str__ de Livre ou Magazine automatiquement
            print("-"*70)
            print(doc)


    def afficher_membres(self):
        """Affiche tous les membres avec la liste de leurs emprunts"""
        if not self.membres:
            print("Aucun membre inscrit.")
            return
        print("\n=== Liste des membres ===")
        print("="*70)
        for membre in self.membres:
            print(f"Membre -> {membre.nom} | Emprunts : {len(membre.liste_emprunts)} document(s)")
            for doc in membre.liste_emprunts:
                """ __str__ appelé automatiquement """
                print("-"*70)
                print(f"   - {doc}")
                print()