from PySide2 import QtWidgets

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Liste de course")
        self.setup_ui()
        self.resize(600,500)

    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.lineEdit = QtWidgets.QLineEdit()
        self.button_add = QtWidgets.QPushButton("Ajouter")
        self.listWidget = QtWidgets.QListWidget()
        self.button_remove = QtWidgets.QPushButton("Retirer")
        self.button_clean = QtWidgets.QPushButton("Nettoyer")

        # Création du sous-layout pour les boutons 'Retirer' et 'Nettoyer'
        self.child_layout = QtWidgets.QHBoxLayout()
        self.child_layout.addWidget(self.button_remove)
        self.child_layout.addWidget(self.button_clean)

        # On ajoute les widgets au layout
        self.layout.addWidget(self.lineEdit)
        self.layout.addWidget(self.button_add)
        self.layout.addWidget(self.listWidget)
        self.layout.addLayout(self.child_layout)
        # self.layout.addWidget(self.button_remove)
        # self.layout.addWidget(self.button_clean)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = App()
    win.show()
    app.exec_()