from PySide2 import QtWidgets, QtCore
from liste_course import get_items

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


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = App()
    win.show()
    app.exec_()