from PyQt5.QtWidgets import QApplication
import sys
from TelaCadastro import Tela_Cadastro

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Tela_Cadastro()
    janela.show()
    sys.exit(app.exec_())


