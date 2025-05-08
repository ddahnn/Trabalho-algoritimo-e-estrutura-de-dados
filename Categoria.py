class Categoria:
   # configuração automatica de ID
    autoId = 0
    
    def __init__(self,  nome):
        self.id = self.autoid =+1
        self.nome = nome

    
    def __str__(self):
        return f"Id {self.id}, Categoria: {self.nome}."
    
    def __str__(self):
        return self.nome
