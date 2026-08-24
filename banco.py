import sqlite3 

# Conectar ao banco de dados
conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

# Ativar chaves estrangeiras
cursor.execute("PRAGMA foreign_keys = ON")
print("Conexão estabelecida com sucesso!")

cursor.execute("""
    CREATE TABLE if NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL
    )
    """
)

cursor.execute("""
    CREATE TABLE if NOT EXISTS livros(
    isbn INTEGER PRIMARY KEY,
    titulo TEXT not NULL,
    autor TEXT not NULL,
    disponibilidade INTEGER NOT NULL DEFAULT 1
    )
   """
    )

cursor.execute("""
    CREATE TABLE if NOT EXISTS emprestimos(
        usuario_id INTEGER ,
        livros_isbn INTEGER,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id),
        FOREIGN KEY(livros_isbn) REFERENCES livros(isbn)
        )
""")

def salvar_livro(livro):
    try:
        cursor.execute("""
            INSERT INTO livros(isbn,titulo,autor,disponibilidade)
            VALUES (?, ?, ?, ?)
        """,(
            livro.isbn,
            livro.titulo,
            livro.autor,
            livro.disponivel
        )
        
        )
        conexao.commit()
        return True
    except sqlite3.IntegrityError:
        print("ISBN já cadastrado")
        return False

def salvar_usuario(usuario):
    try:
        cursor.execute("""
            INSERT INTO usuarios(id,nome)
            VALUES(?,?)
        """,(
            usuario.id,
            usuario.nome
        )
        )
        conexao.commit()
        return True
    
    except sqlite3.IntegrityError:
        print("Usuário já cadastrado")
        return False


def buscar_livros():
    cursor.execute("""
        SELECT isbn,titulo,autor,disponibilidade
        FROM livros
    """)
    return cursor.fetchall()

def buscar_usuarios():
    cursor.execute("""
    SELECT id,nome
    FROM usuarios
    """)
    return cursor.fetchall()

def buscar_emprestimos():
    cursor.execute("""
        SELECT usuario_id,livros_isbn
        FROM emprestimos
    """)
    return cursor.fetchall()


def realizar_emprestimo(id_usuario, isbn):
    try:
        cursor.execute("""
            INSERT INTO emprestimos(usuario_id, livros_isbn)
            VALUES (?, ?)
        """, (
            id_usuario,
            isbn
        ))

        cursor.execute("""
            UPDATE livros
            SET disponibilidade = 0
            WHERE isbn = ?
        """, (
            isbn,
        ))

        conexao.commit()
        return True

    except sqlite3.IntegrityError:
        conexao.rollback()
        return False


def realizar_devolucao(id_usuario, isbn):
    try:
        cursor.execute("""
            DELETE FROM emprestimos
            WHERE usuario_id = ? AND livros_isbn = ?
        """, (
            id_usuario,
            isbn
        ))

        cursor.execute("""
            UPDATE livros
            SET disponibilidade = 1
            WHERE isbn = ?
        """, (
            isbn,
        ))

        conexao.commit()
        return True

    except sqlite3.IntegrityError:
        conexao.rollback()
        return False
    
