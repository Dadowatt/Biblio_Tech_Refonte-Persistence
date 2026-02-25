from document import Document
class Livre(Document):
    def __init__(self, titre, auteur, id=None):
        super().__init__(titre, id=id)
        self.auteur = auteur
    
    def __str__(self):
        statut = "Disponible" if self.disponible else "Emprunté"
        return f"Livre : {self.titre} - Auteur : {self.auteur} ({statut})"