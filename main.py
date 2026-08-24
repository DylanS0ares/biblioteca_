from biblioteca import Biblioteca
from livro import Livro
from usuario import Usuario


biblioteca = Biblioteca()


def menu():
    print("\n" + "=" * 35)
    print("          BIBLIOTECA")
    print("=" * 35)
    print("1 - Cadastrar livro")
    print("2 - Cadastrar usuário")
    print("3 - Emprestar livro")
    print("4 - Devolver livro")
    print("5 - Buscar livro")
    print("6 - Listar livros")
    print("0 - Sair")
    print("=" * 35)


while True:

    menu()

    opcao = input("Escolha uma opção: ")

    # Cadastrar livro
    if opcao == "1":

        titulo = input("Título: ").strip().lower()
        autor = input("Autor: ").strip().lower()
        isbn = int(input("ISBN: ").strip())

        livro = Livro(titulo, autor, isbn)

        biblioteca.cadastrar_livro(livro)

    # Cadastrar usuário
    elif opcao == "2":

        nome = input("Nome: ").strip().lower()

        usuario = Usuario(None, nome)

        biblioteca.cadastrar_usuario(usuario)

    # Emprestar livro
    elif opcao == "3":

        nome = input("Nome do usuário: ")

        id_usuario = biblioteca.buscar_usuario(nome)

        if id_usuario is not None:

            isbn = int(input("ISBN do livro: ").strip())

            biblioteca.emprestar_livro(id_usuario, isbn)

        else:
            print("Usuário não encontrado")

    # Devolver livro
    elif opcao == "4":

        nome = input("Nome do usuário: ")

        id_usuario = biblioteca.buscar_usuario(nome)

        if id_usuario is not None:

            isbn = int(input("ISBN do livro: ").strip())

            biblioteca.devolver_livro(id_usuario, isbn)

        else:
            print("Usuário não encontrado")

    # Buscar livro
    elif opcao == "5":

        titulo = input("Título do livro: ").strip().lower()

        livro = biblioteca.buscar_livro(titulo)

        if livro:
            print("\nLivro encontrado:")
            print(f"Título: {livro.titulo}")
            print(f"Autor: {livro.autor}")
            print(f"ISBN: {livro.isbn}")
            print(f"Disponível: {livro.disponivel}")

        else:
            print("Livro não encontrado.")

    # Listar livros
    elif opcao == "6":

        print("\n--- LIVROS ---")

        if not biblioteca.livros:
            print("Nenhum livro cadastrado.")

        else:
            for livro in biblioteca.livros.values():

                print(
                    f"ISBN: {livro.isbn} | "
                    f"Título: {livro.titulo} | "
                    f"Autor: {livro.autor} | "
                    f"Disponível: {livro.disponivel}"
                )

    # Sair
    elif opcao == "0":

        print("Encerrando biblioteca...")
        break

    else:
        print("Opção inválida.")