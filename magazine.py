from document import Document
class Magazine(Document):
    def __init__(self, titre, numero):
        super().__init__(titre)
        self.numero = numero

    def __str__(self):
        statut = "Disponible" if self.disponible else "Emprunté"
        return f"Magazine : {self.titre} - Numéro : {self.numero} ({statut})"