from PySide2 import QtWidgets
from tinydb import TinyDB
from pathlib import Path

class Produit:
    # On initialise une instance de TinyDB en attribut de classe
    DB = TinyDB(Path(__file__).resolve().parent / 'data.json', indent=4)

    def __init__(self, nom: str, quantite = "1"):
        """Méthode d'initialisation de nos instances de Produit.

        Args:
            nom (str): le nom du produit.
            quantite (str, optional): la quantité souhaité pour ce produit. Defaults to "1".
        """

        self.nom = nom.capitalize()
        self.quantite = quantite
    
    def __str__(self):
        """Méthode pour mettre en forme nos instances lorsqu'elle sont print ou convertis en str().

        Returns:
            (str) : le nom de l'instance.
        """

        return f"{self.nom}"

    def __repr__(self):
        """Méthode de représentation de nos intances. Montre comment recréer l'instance à partir de la classe.

        Returns:
            (str) : comment re-créer l'instance à partir de la classe.
        """

        return f"Produit({self.nom}, {self.quantite})"
    
if __name__ == '__main__':
    banane = Produit("banane")