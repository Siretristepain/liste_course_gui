from PySide2 import QtWidgets, QtCore
from liste_course import Produit, get_items, clean_all

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Liste de course")
        self.setup_ui()
        self.setup_connections()
        self.show_items()
        self.resize(600,500)

    def setup_ui(self):
        """Méthode pour définir l'organisation de l'interface visuelle de l'application.
        """

        # On défini ici le layout principal ainsi que les différents widgets qui vont le composer
        self.layout = QtWidgets.QVBoxLayout(self)
        self.lineEdit = QtWidgets.QLineEdit()
        self.spinBox = QtWidgets.QSpinBox()
        self.button_add = QtWidgets.QPushButton("Ajouter")
        self.listWidget = QtWidgets.QListWidget()
        # La ligne suivante permet d'avoir un comportement + ergonomique pour séléctionner plusieurs items à la fois
        # Ce sera utile pour supprimer plusieurs éléments d'un coup par exemple
        self.listWidget.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.button_remove = QtWidgets.QPushButton("Retirer")
        self.button_clean = QtWidgets.QPushButton("Nettoyer")
        # On défini la valeur de base de la spinBox sur 1
        self.spinBox.setValue(1)

        # Création du sous-layout pour la lineEdit et la spinBox pour qu'ils soient côte à côte
        self.top_child_layout = QtWidgets.QHBoxLayout()
        self.top_child_layout.addWidget(self.lineEdit)
        self.top_child_layout.addWidget(self.spinBox)

        # Création du sous-layout pour les boutons 'Retirer' et 'Nettoyer' pour qu'ils soient côte à côte
        self.bottom_child_layout = QtWidgets.QHBoxLayout()
        self.bottom_child_layout.addWidget(self.button_remove)
        self.bottom_child_layout.addWidget(self.button_clean)

        # On ajoute les widgets au layout principal
        self.layout.addLayout(self.top_child_layout)
        self.layout.addWidget(self.button_add)
        self.layout.addWidget(self.listWidget)
        self.layout.addLayout(self.bottom_child_layout)

    def setup_connections(self):
        self.button_add.clicked.connect(self.add_item)
        self.lineEdit.returnPressed.connect(self.add_item)
        self.button_remove.clicked.connect(self.remove_item)
        self.button_clean.clicked.connect(self.clean)

    def show_items(self):
        """Méthode pour afficher les éléments présents dans la bdd (JSON) sur la ListWidget.
        """

        # On récupère tous les éléments de la bdd via la méthode 'get_items()'
        all_items = get_items()

        for item in all_items:
            # Pour chaque item on crée une QListWidgetItem pour lier l'item à une instance via setData
            # On ajoute 'item.name_and_quantity' dans lw_item et pas seulement 'item.nom' afin de pouvoir voir la quantité de l'item désirée
            lw_item = QtWidgets.QListWidgetItem(item.name_and_quantity)

            lw_item.setData(QtCore.Qt.UserRole, item)
            self.listWidget.addItem(lw_item)

    def add_item(self):
        """Méthode qui ajoute l'item donné par l'utilisateur dans la liste de course.
        On récupère la valeur issue de la spinBox (-> quantité souhaitée).
        Pour cela, on récupère le texte de la LineEdit.
        A partir de ce texte on crée une instance de Produit.
        On utilise la méthode add_item() sur notre Produit pour l'ajouter à la bdd.
        Deux options :

        - soit le produit existait déjà dans la bdd, auquel cas on implémente sa quantité de la valeur issue de la spinBox.
        - soit le produit n'existait pas déjà dans la bdd, auquel cas la suite :

        On lie l'instance avec le texte (-> cad le nom du produit).
        On ajoute le nom du produit dans la liste et on ajoute l'instance dans la bdd (JSON).

        Returns:
            (bool) : False dans le cas où le texte saisi par l'utilisateur est vide.
        """

        # On récupère le texte de la LineEdit
        item = self.lineEdit.text()

        # On récupère la valeur (= quantité) de la spinBox
        quantity = self.spinBox.value()

        # On vérifie que le texte ne soit pas vide
        if item == "":
            return False
        
        # On créer une instance de notre item
        item_to_add = Produit(item, quantity)

        # On ajoute notre nouveau produit à notre bdd
        ajout = item_to_add.add_item(x=quantity)

        # Si ajout == False, cela signifie que le produit qu'on souhaite ajouté est déjà dans la bdd.
        # Dans ce cas, le back-end à simplement incrémenté la quantité de ce produit de x (x étant la valeur dans la spinBox -> variable 'quantity')

        # Si ajout == True, cela signifie que le produit qu'on souhaite ajouté n'était pas déjà présent dans la bdd, auquel cas on l'ajoute simplement.
        if ajout == True:
            # On vas lié notre item à une instance puis ajouter l'item à la ListWidget
            lw_item = QtWidgets.QListWidgetItem(item_to_add.name_and_quantity)
            lw_item.setData(QtCore.Qt.UserRole, item_to_add)
            self.listWidget.addItem(lw_item)

        # On "rafraichit" (nettoye) la listWidget et on refait appel à la méthode show_items()
        self.listWidget.clear()
        self.show_items()

        # On remet la valeur de la spinBox sur 1
        self.spinBox.setValue(1)
        
        # On enlève le texte de la LineEdit
        self.lineEdit.setText("")

    def remove_item(self):
        """Méthode qui permet de supprimer les éléments séléctionnés, à la fois de la ListWidget et de la bdd (JSON).
        """

        for selected_item in self.listWidget.selectedItems():
            # On récupère l'instance qu'on avait liée au nom du produit
            item = selected_item.data(QtCore.Qt.UserRole)
            # On applique la méthode delete_item dessus pour le retirer de la bdd
            item.delete_item()
            # On retire ensuite les items séléctionnés de la listWidget
            self.listWidget.takeItem(self.listWidget.row(selected_item))

    def clean(self):
        """Méthode utilisée pour nettoyer toute la base de donnée.
        Elle fait appel à la méthode 'clean_all()'.
        """

        # Méthode pour supprimer tous les éléments de la bdd
        clean_all()

        # On nettoye toute la listWidget de notre GUI
        self.listWidget.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = App()
    win.show()
    app.exec_()