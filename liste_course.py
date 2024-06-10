from PySide2 import QtWidgets
from tinydb import TinyDB
from pathlib import Path

class Produit:
    DB = TinyDB(Path(__file__).resolve().parent / 'data.json', indent=4)
    def __init__(self, nom: str, quantite = 1):
        self.nom = nom.capitalize()
        self.quantite = quantite
    
    def __str__(self):
        return f"{self.nom}"

    def __repr__(self):
        return f"Produit({self.nom}, {self.quantite})"
    
if __name__ == '__main__':
    banane = Produit("banane")