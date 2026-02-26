from abc import ABC, abstractmethod

class Document(ABC):
    """Classe abstraite représentant un document général.
    Cette classe sert de base pour d'autres types de documents comme Livre et Magazine"""
    def __init__(self, titre, id=None):
        self.titre = titre
        self.__disponible = True
        self.id = id

    @abstractmethod
    def __str__(self):
        #chaque type de document doit définir son affichage    
        pass

    @property
    def disponible(self):
        return self.__disponible

    def peut_emprunter(self):
        return self.__disponible

    def emprunter(self):
        if not self.__disponible:
            raise ValueError(f"Le document '{self.titre}' est déjà emprunté")
        self.__disponible = False

    def retourner(self):
        if self.__disponible:
            raise ValueError(f"Le document '{self.titre}' n'a pas été emprunté")
        self.__disponible = True