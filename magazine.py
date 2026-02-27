from document import Document

class Magazine(Document):
    def __init__(self, titre, numero, id=None):
        super().__init__(titre, id=id)
        self.numero = numero

    def __str__(self):
        statut = "Disponible" if self.disponible else "Emprunté"
        return f"Magazine : {self.titre} | Numéro : {self.numero} état: ({statut}) |"
