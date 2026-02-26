class Membre:
    def __init__(self, nom, id=None):
        self.id = id
        self.nom = nom
        self.liste_emprunts = []


    def peut_emprunter(self, document):
        """Retourne True si le membre peut emprunter ce document"""
        return document not in self.liste_emprunts


    def emprunter_document(self, document):
        """Ajoute un document à la liste d'emprunts si possible"""
        if not self.peut_emprunter(document):
            raise ValueError(f"Le membre '{self.nom}' a déjà emprunté ce document")
        self.liste_emprunts.append(document)


    def retourner_document(self, document):
        """Retire un document de la liste d'emprunts"""
        if document not in self.liste_emprunts:
            raise ValueError(f"Le document n'a pas été emprunté par ce membre")
        self.liste_emprunts.remove(document)