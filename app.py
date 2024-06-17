from PySide2 import QtWidgets, QtCore
from liste_course import Produit, get_items

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Liste de course")
        self.setup_ui()
        self.show_items()
        self.resize(600,500)

    def setup_ui(self):
        """Méthode pour définir l'organisation de l'interface visuelle de l'application.
        """

        # On défini ici le layout principal ainsi que les différents widgets qui vont le composer
        self.layout = QtWidgets.QVBoxLayout(self)
        self.lineEdit = QtWidgets.QLineEdit()
        self.button_add = QtWidgets.QPushButton("Ajouter")
        self.listWidget = QtWidgets.QListWidget()
        self.button_remove = QtWidgets.QPushButton("Retirer")
        self.button_clean = QtWidgets.QPushButton("Nettoyer")

        # Création du sous-layout pour les boutons 'Retirer' et 'Nettoyer' pour qu'ils soient côte à côte
        self.child_layout = QtWidgets.QHBoxLayout()
        self.child_layout.addWidget(self.button_remove)
        self.child_layout.addWidget(self.button_clean)

        # On ajoute les widgets au layout principal
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.button_add)
        self.layout.addWidget(self.listWidget)
        self.layout.addLayout(self.child_layout)

    def setup_connections(self):
        pass

    def show_items(self):
        """Méthode pour afficher les éléments présents dans la bdd (JSON) sur la ListWidget.
        """

        # On récupère tous les éléments de la bdd via la méthode 'get_items()'
        all_items = get_items()

        for item in all_items:
            # Pour chaque item on crée une QListWidgetItem pour lier l'item à une instance via setData
            lw_item = QtWidgets.QListWidgetItem(item.nom)

            lw_item.setData(QtCore.Qt.UserRole, item)
            self.listWidget.addItem(lw_item)

    def add_item(self):
        """Méthode qui ajoute l'item donné par l'utilisateur dans la liste de course.
        Pour cela, on récupère le texte de la LineEdit.
        A partir de ce texte on crée une instance de Produit.
        On lie l'instance avec le texte (-> cad le nom du produit).
        On ajoute le nom du produit dans la liste et on ajoute l'instance dans la bdd (JSON).

        Returns:
            (bool) : False dans le cas où le texte saisi par l'utilisateur est vide.
        """
        
        # On récupère le texte de la LineEdit
        item = self.lineEdit.text()

        # On vérifie que le texte ne soit pas vide
        if item == False:
            return False
        
        # On créer une instance de notre item
        item_to_add = Produit(item)

        # On ajoute notre nouveau produit à notre bdd
        item_to_add.add_item()

        # On vas lié notre item à une instance puis ajouter l'item à la ListWidget
        lw_item = QtWidgets.QListWidgetItem(item_to_add.nom)
        lw_item.setData(QtCore.Qt.UserRole, item_to_add)
        self.listWidget.addItem(lw_item)

        # On enlève le texte de la LineEdit
        self.lineEdit.setText("")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = App()
    win.show()
    app.exec_()