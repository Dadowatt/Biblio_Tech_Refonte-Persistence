class GestionEmprunt:
    def valider_pret(self, membre, document):
        if not membre.peut_emprunter(document):
            raise ValueError(f"Membre '{membre.nom}' ne peut pas emprunter ce document")
        if not document.peut_emprunter():
            raise ValueError(f"Document '{document.titre}' déjà emprunté")

        membre.emprunter_document(document)
        document.emprunter()


    def retour_document(self, membre, document):
        membre.retourner_document(document)
        document.retourner()