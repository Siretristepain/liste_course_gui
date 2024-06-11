from PySide2 import QtWidgets
from tinydb import TinyDB, where
from pathlib import Path
from typing import List

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
    
    def _write_items(self):
        """Méthode privée utilisée pour ajouter un produit et sa quantité dans la bdd (-> fichier JSON).
        """

        Produit.DB.insert({'nom' : self.nom, 'quantite' : self.quantite})

    def _get_items(self) -> List[tuple]:
        """Méthode privée utilisée pour récupérer tous les éléments de notre bdd sous forme de liste de tuple (nom, quantite).

        Returns:
            List[tuple]: [(nom, quantite)]
        """
        # On récupère tous les éléments de notre bdd dans une liste
        all_items = [(x['nom'], x['quantite']) for x in Produit.DB]

        # Si la liste est vide, on retourne [("",0)] pour être cohérent avec notre docstring
        if bool(all_items) == False:
            return [("",0)]
        
        return all_items
    
    def _check_item(self):
        """Méthode privée utilisée pour monitorer la présence d'un produit dans la bdd JSON.

        Returns:
            (bool) : 'True' si le produit est trouvé dans la bdd, 'False' sinon.
        """
        
        # On fait appel à notre méthode '_get_items()' pour récupérer tous les produits de la bdd
        all_items = self._get_items()

        for tpl in all_items:
            if tpl[0] == self.nom:
                return True
        return False

    
if __name__ == '__main__':
    banane = Produit("banane")
    print(banane)

    # Ajout de banane dans la bdd
    # banane._write_items()

    # Récupération des items de la bdd
    print(banane._get_items())

    # On vérifie que la banane soit dans la bdd
    print(banane._check_item())
    # On crée un produit 'noix de coco' que l'on enregistre pas dans la bdd pour voir si _check_item() a bien le comportement attendu
    coco = Produit(nom="noix de coco",quantite=1)
    print(coco._check_item())