from membre import Membre
from bibliotheque import Bibliotheque
from gestion_emprunt import GestionEmprunt


class Bibliothecaire:
    def __init__(self, bibliotheque: Bibliotheque, gestion_emprunt: GestionEmprunt):
        self.bibliotheque = bibliotheque
        self.gestion_emprunt = gestion_emprunt


    #délégation à la bibliothèque 
    def ajouter_document(self, document):
        self.bibliotheque.ajouter_document(document)


    def inscrire_membre(self, membre):
        self.bibliotheque.inscrire_membre(membre)


    #coordination des actions
    def valider_pret(self, nom_membre, titre_document):
        membre = self.bibliotheque.trouver_membre(nom_membre)
        if not membre:
            raise ValueError(f"Membre '{nom_membre}' introuvable")
        document = self.bibliotheque.trouver_document(titre_document)
        if not document:
            raise ValueError(f"Document '{titre_document}' introuvable")
        self.gestion_emprunt.valider_pret(membre, document)


    def retour_document(self, nom_membre, titre_document):
        membre = self.bibliotheque.trouver_membre(nom_membre)
        if not membre:
            raise ValueError(f"Membre '{nom_membre}' introuvable")
        document = self.bibliotheque.trouver_document(titre_document)
        if not document:
            raise ValueError(f"Document '{titre_document}' introuvable")
        self.gestion_emprunt.retour_document(membre, document)


    def afficher_documents(self):
        """affichage (optionnel pour accès direct depuis bibliothécaire)"""
        self.bibliotheque.afficher_documents()


    def afficher_membres(self):
        self.bibliotheque.afficher_membres()