# Liste de course avec GUI

## Objectifs

> Le but de ce projet est de créer une application pour éditer des listes de courses via une interface graphique et une base de donnée TinyDB en Python.

L'utilisateur aurait face à lui une interface où il pourrait voir les produits dans sa liste ainsi que la quantité souhaitée. Il pourrait en rajouter et/ou en supprimer et/ou encore en modifier la quantité.

L'interface graphique est faite via le module PySide2.
La base de donnée est crée via le module tinydb. Il s'agit de petite base de donnée très légère utilisant un fichier JSON. Ce type de base de donnée convient très bien à ce genre de projet.

## Les points importants (à faire)

- Il y aurait une LineEdit pour écrire le produit à ajouter.
- Il y aurait une SpinBox pour sélectionner la quantité souhaitée, fixée par défaut sur 1.
- Il y aurait un Button pour valider l'ajout du produit dans la liste (-> également la possibilité d'appuyer sur Entrée pour valider)
- Il y aurait ensuite ListWidget dans laquelle serait listés tous les produits de la liste (ceux enregistrés dans la bdd). Il faudrait qu'ils soient listés avec leurs quantité entre parenthèses. Ex: Banane (x6). (-> ça va un peu compliqué ma méthode pour monitorer la présence d'un produit mais ça devrait aller) => Bah non ça va rien compliqué du tout.
- Il y aurait ensuite un Button pour supprimer des éléments. Il faudrait que l'action de cliquer supprimer l'ensemble des produits séléctionnés. (-> s'arranger pour faire une séléction multiple).
- Il y aurait ensuite un Button permettant de réinitialiser la liste de course (-> remettre la bdd à zéro).

## A faire dans l'immédiat

- Une méthode (propriété) qui associerait le nom du produit à sa quantité : Banane (x6). Car au final c'est ça qu'on voudra afficher dans notre application par la suite.
- Une méthode qui permet d'ajouter un produit dans la liste. Elle serait basée sur notre méthode existante '_write_item()' mais ferait au préalable le check du produit (on ne veut pas ajouter un produit qu'il y a déjà dans la liste). Ce check serait fait par notre méthode '_check_item()'.
- Une méthode privée pour supprimer un élément de la bdd. -> Sur le même fonctionnement que '_write_item()'.
- Une méthode qui à l'inverse de celle au point 2 permettrait de supprimer un produit. Sur le même modèle, on appliquerait la méthode '_check_item()'. Si elle retourne True, c'est que le produit existe, alors on le supprime via notre future méthode privée faite pour ça (point 3).