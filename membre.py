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