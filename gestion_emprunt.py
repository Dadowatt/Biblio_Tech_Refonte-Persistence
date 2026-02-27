class GestionEmprunt:
    def __init__(self, repository):
        self.repository = repository  # on stocke la dépendance

    def valider_pret(self, membre, document):
        if not membre.peut_emprunter(document):
            raise ValueError(f"Membre '{membre.nom}' ne peut pas emprunter ce document")
        if not document.peut_emprunter():
            raise ValueError(f"Document '{document.titre}' déjà emprunté")

        # Mise à jour en mémoire
        membre.emprunter_document(document)
        document.emprunter()
        #Mise à jour base de données
        self.repository.sauvegarder_emprunt(membre, document)


    def retour_document(self, membre, document):
        # Mise à jour en mémoire
        membre.retourner_document(document)
        document.retourner()
        #Mise à jour base de données
        self.repository.supprimer_emprunt(membre, document)