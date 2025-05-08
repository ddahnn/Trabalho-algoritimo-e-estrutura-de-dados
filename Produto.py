from abc import ABC, abstractmethod

produtos =[]

class Produto( ABC ):
    def __init__(self, modelo, cor, categoria):
        self.modelo = modelo
        self.cor = cor
        self.categoria = categoria
        self.preco = 0.0
    



    def get_preco(self):
        ''' exibe o preço '''
        return self.preco
    
    #area SETTER

    def set_preco (self, novo_Preco):
        ''' Altera o preço  apenas ser o valor for maior que zero. '''
        if float(novo_Preco) > 0:
            self.preco = novo_Preco
        else:
            raise ValueError("O preço deve ser maior que zero.")

    def getInformaocoes(self):
        """ Retorna as informações da categoria ."""
        return f"Modelo {self.modelo}, Cor: {self.cor}, Categoria {self.categoria}, Preço R${float(self.preco)}"


    @abstractmethod
    def cadastrar(self):
        pass    