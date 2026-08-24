class Usuario():
    def __init__(self,id,nome,livros =[]):
        self.nome = nome
        self.id = id
        self.livros_emprestados = livros
