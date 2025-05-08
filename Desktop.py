from Produto import Produto
from Categoria import Categoria

produtos = []

class Desktop(Produto):
    def __init__(self, modelo, cor,  categoria, preco, potencia_Da_Fonte):
        super().__init__(modelo, cor,categoria)
        self.set_preco(preco)
        self._potencia_Da_Fonte = potencia_Da_Fonte



    @property
    def potenciaDaFonte(self):
        return self._potencia_Da_Fonte
    
    @potenciaDaFonte.setter
    def potenciaDaFonte(self, novaPotencia):
        self._potencia_Da_Fonte = novaPotencia

    def cadastrar(self):
        produto = {
            "modelo":self.modelo,
            "cor":self.cor,
            "preco":self.preco,
            "categoria":self.categoria.nome,
            "potencia da fonte":self._potencia_Da_Fonte
        }
        produtos.append(produto)
        print("Produto cadastrado com sucesso.")

    def getInformacoes(self):
        return super().getInformacoes() +f", Potencia da fonte: {self._potencia_Da_Fonte}."