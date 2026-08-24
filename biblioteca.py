from banco import salvar_livro,salvar_usuario,realizar_emprestimo
from banco import realizar_devolucao,buscar_livros,buscar_usuarios,buscar_emprestimos
from livro import Livro
from usuario import Usuario


class Biblioteca():
    def __init__(self):
        self.livros = {}
        self.usuarios = {}
        self.carregar_livros()
        self.carregar_usuarios()
        self.carregar_emprestimos()

    def cadastrar_livro(self,livro):
        self.livros[livro.isbn] = livro
        salvar_livro(livro)

    def cadastrar_usuario(self,usuario):
        self.usuarios[usuario.id] = usuario
        salvar_usuario(usuario)
        

    def emprestar_livro(self, id_usuario, isbn):

        try:
            usuario = self.usuarios[id_usuario]
        except KeyError:
            return print("Usuário não encontrado")

        try:
            livro = self.livros[isbn]
        except KeyError:
            return print("Livro não encontrado")

        if not livro.disponivel:
            return print("Livro já está emprestado")

        if realizar_emprestimo(id_usuario, isbn):
            livro.disponivel = False
            usuario.livros_emprestados.append(livro)
        else:
            print("Não foi possível realizar o empréstimo.")


    def devolver_livro(self,id_usuario,isbn):
        try:
            usuario  = self.usuarios[id_usuario]
        except KeyError:
            return  print("Usuário não encontrado")
            
        try:
            livro = self.livros[isbn]
        except KeyError:
           return print("Livro não encontrado")
            
        
        if livro in usuario.livros_emprestados:
            if realizar_devolucao(id_usuario,isbn):
                livro.disponivel = True
                usuario.livros_emprestados.remove(livro)
            else:
                print("Não foi possível realizar a devolução")
        else:
            print("Livro não foi emprestado para esse usuário")

    def buscar_livro(self,titulo):
        for livro in self.livros.values():
            if livro.titulo == titulo:
                return livro
    
        return None

    def carregar_livros(self):
        dados = buscar_livros()
        for isbn,titulo,autor,disponibilidade in dados:
            livro = Livro(
                titulo,
                autor,
                isbn,
                bool(disponibilidade)
            )
            self.livros[isbn] = livro

    def carregar_usuarios(self):
        dados = buscar_usuarios()
        for id,nome in dados:
            usuario = Usuario(id,nome)
            self.usuarios[id] = usuario

    def carregar_emprestimos(self):
        dados = buscar_emprestimos()
        for id_usuario,isbn in dados:
            usuario = self.usuarios[id_usuario]
            livro = self.livros[isbn]

            usuario.livros_emprestados.append(livro)
    def buscar_usuario(self, nome):
        nome = nome.strip().lower()

        for usuario in self.usuarios.values():
            if usuario.nome.lower() == nome:
                return usuario.id

        return None
