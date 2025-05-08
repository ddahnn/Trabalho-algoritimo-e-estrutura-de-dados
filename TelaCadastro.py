from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox
from Desktop import Desktop
from Notebook import Notebook
from Categoria import Categoria
from TelaExibicao import Tela_Exibicao

class Tela_Cadastro(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Produtos")
        self.setGeometry(100, 100, 400, 300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Botão para exibir produtos
        self.botaoExibir = QPushButton("Ver Produtos Cadastrados")
        self.botaoExibir.clicked.connect(self.abrirTelaExibicao)
        layout.addWidget(self.botaoExibir)

        # Tipo do produto
        self.tipo = QComboBox()
        self.tipo.addItems(["Desktop", "Notebook"])
        layout.addWidget(QLabel("Tipo de Produto:"))
        layout.addWidget(self.tipo)

        # Modelo
        self.modelo = QLineEdit()
        self.modelo.setPlaceholderText("Modelo")
        layout.addWidget(self.modelo)

        # Cor
        self.cor = QLineEdit()
        self.cor.setPlaceholderText("Cor")
        layout.addWidget(self.cor)

        # Preço
        self.preco = QLineEdit()
        self.preco.setPlaceholderText("Preço")
        layout.addWidget(self.preco)

        # Extra
        self.extra = QLineEdit()
        self.extra.setPlaceholderText("Potência da Fonte (W) ou Tempo de Bateria (h)")
        layout.addWidget(self.extra)

        # Botão de cadastro
        self.botaoCadastrar = QPushButton("Cadastrar")
        self.botaoCadastrar.clicked.connect(self.cadastrarProduto)
        layout.addWidget(self.botaoCadastrar)

        self.setLayout(layout)

    def abrirTelaExibicao(self):
        self.tela_exibicao = Tela_Exibicao()
        self.tela_exibicao.show()

    def cadastrarProduto(self):
        try:
            tipo = self.tipo.currentText()
            modelo = self.modelo.text()
            cor = self.cor.text()
            preco = float(self.preco.text())
            extra = self.extra.text()
            categoria = Categoria( "Informática")

            if tipo == "Desktop":
                produto = Desktop(modelo, cor, categoria, preco, extra)
            else:
                produto = Notebook(modelo, cor, categoria, preco, extra)

            produto.cadastrar()
            QMessageBox.information(self, "Sucesso", f"{tipo} cadastrado com sucesso!")
        except ValueError:
            QMessageBox.warning(self, "Erro", "Por favor, insira um valor numérico válido para o preço.")
        except Exception as e:
            QMessageBox.critical(self, "Erro inesperado", str(e))
