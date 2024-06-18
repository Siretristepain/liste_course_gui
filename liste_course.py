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
    
    @property
    def name_and_quantity(self):
        """Propriété qui associe le nom du produit à sa quantité : Banane (x6).

        Returns:
            (str) : Le nom et la quantité du produit.
        """

        return f"{self.nom} (x{self.quantite})"
    
    def _write_items(self):
        """Méthode privée utilisée pour ajouter un produit et sa quantité dans la bdd (-> fichier JSON).
        """

        Produit.DB.insert({'nom' : self.nom, 'quantite' : self.quantite})

    def _remove_items(self):
        """Méthode privée utilisée pour retirer un produit et sa quantité dans la bdd.
        La suppression se fait en recherchant le nom du produit.
        """

        Produit.DB.remove(where('nom') == self.nom)

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
    
    def add_item(self):
        """Méthode pour ajouter un élément dans la bdd (JSON).
        Elle utilise notre méthode privée _write_items() et _check_item() en amont.
        Si l'item est déjà dans la bdd, elle ne l'ajoute pas.

        Returns:
            (str) : Information sur l'ajout (ou le non ajout) de l'item à la bdd.
        """
        
        # D'abord on vérifie que l'item ne soit pas déjà dans la bdd
        if self._check_item() == False:
            self._write_items()
            return f"{self.nom} ajouté à la liste"
        else:
            return f"{self.nom} déjà dans la liste."
            # Là on pourrait ajouter une option pour savoir si l'utilisateur souhaite 
            # quand même ajouter l'item, auquel cas on ferait +1 sur la quantité de l'item.

    def delete_item(self):
        """Méthode pour supprimer un élément dans la bdd (JSON).
        Elle utilise _check_items() au préalable pour s'assurer que le produit à retirer est dans la bdd.

        Returns:
            (str) : Information sur le retrait (ou le non retrait) de l'item dans la bdd.
        """
        # On ne peut supprimer l'item que si il existe déjà dans la bdd
        if self._check_item() == True:
            self._remove_items()
            return f"{self.nom} supprimé de la liste"
        else:
            return f"{self.nom} n'est déjà pas dans la liste."

def get_items():
    # Liste d'instances de tous les produits de notre liste
    items = []

    # On récupère tous les produits de la bdd
    all_items = [(x['nom'], x['quantite']) for x in Produit.DB]

    # On boucle sur tous les produits et on stocke dans 'items' les instances
    for tpl in all_items:
        items.append(Produit(tpl[0], tpl[1]))

    return items

def clean_all():
    """Méthode utilisée pour nettoyer toute la base de donnée (JSON)
    """
    
    Produit.DB.truncate()

    
if __name__ == '__main__':
    banane = Produit("banane")
    print(banane)

    # Ajout de banane dans la bdd
    banane._write_items()

    # Récupération des items de la bdd
    print(banane._get_items())

    # On vérifie que la banane soit dans la bdd
    print(f"La banane est elle dans la liste : {banane._check_item()}")

    # On crée un produit 'noix de coco' que l'on enregistre pas dans la bdd pour voir si _check_item() a bien le comportement attendu
    coco = Produit(nom="noix de coco")
    print(f"La noix de coco est elle dans la liste : {coco._check_item()}")

    # On utilise la propriété name_and_quantity pour vérifier qu'elle a bien le comportement attendu
    print(coco.name_and_quantity)

    # On utilise la méthode 'add_item()' sur notre noix de coco pour l'ajouter à la bdd (JSON)
    print(coco.add_item())
    print(f"La noix de coco est elle dans la liste : {coco._check_item()}")

    # On supprime la noix de coco de la bdd et on revérifie si elle est dedans
    coco._remove_items()
    print(f"Présence noix de coco : {coco._check_item()}")

    # On supprime la banane de la bdd
    # print(banane.delete_item())

    # Print get_items
    print(get_items())