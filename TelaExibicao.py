from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit
from Desktop import produtos as produtos_desktop
from Notebook import produtos as produtos_notebook

class Tela_Exibicao(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Produtos Cadastrados")
        self.setGeometry(200, 200, 400, 400)

        self.layout = QVBoxLayout()

        self.titulo = QLabel("Lista de Produtos:")
        self.layout.addWidget(self.titulo)

        self.area_texto = QTextEdit()
        self.area_texto.setReadOnly(True)
        self.layout.addWidget(self.area_texto)

        self.botao_atualizar = QPushButton("Atualizar Lista")
        self.botao_atualizar.clicked.connect(self.mostrarProdutos)
        self.layout.addWidget(self.botao_atualizar)

        self.setLayout(self.layout)
        self.mostrarProdutos()  # mostrar ao abrir

    def mostrarProdutos(self):
        texto = ""

        if not produtos_desktop and not produtos_notebook:
            texto = "Nenhum produto cadastrado ainda."
        else:
            for produto in produtos_desktop:
                texto += f"[DESKTOP] {produto}\n"

            for produto in produtos_notebook:
                texto += f"[NOTEBOOK] {produto}\n"

        self.area_texto.setText(texto)
