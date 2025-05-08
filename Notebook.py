from Produto import Produto

produtos = []

class Notebook( Produto ) :
    def __init__(self, modelo, cor, categoria, preco, tempo_de_Bateria):
        super().__init__(modelo, cor, categoria )
        self.set_preco(preco)
        self.__tempo_de_Bateria = tempo_de_Bateria

    @property
    def tempo_Bateria(self):
        return self.__tempo_de_Bateria
    
    @tempo_Bateria.setter
    def tempo_Bateria(self, novo_tempo):
        self.__tempo_de_Bateria = novo_tempo
        
    def cadastrar(self):
        produto = {
            "Modelo":self.modelo,
            "cor": self.cor,
            "Categoria":self.categoria,
            "preço":self.preco,
            "Tempo de bateria": self.__tempo_de_Bateria
        }
        produtos.append(produto)
        print("Notebook salvo com sucesso")


        def getInformacoes(self):
            super().__init__ + f" Tempo de bateria { self.__tempo_de_Bateria}"
    

