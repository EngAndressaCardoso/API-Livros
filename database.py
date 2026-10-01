# Base de dados em memória
Livros = [
    {
        "id": 1,
        "Title": "A culpa é das estrelas",
    },
    {
        "id": 2,
        "Title": "O acordo",
    },
    {
        "id": 3,
        "Title": "O erro",
    },
    {
        "id": 4,
        "Title": "O morro do ventos uivante",
    },
    {
        "id": 5,
       "Title": "Memória póstumas de brás cubas",
    },
    {
        "id": 6,
        "Title": "O triste fim de policarpo  quaresma",
    },
    {
        "id": 7,
        "Title": "A seleção",
    },
    {
        "id": 8,
       "Title": "Estilhaça-me",
    },
    {
        "id": 9,
        "Title": "Harry Potter e a pedra filosofal",
    },
    {
        "id": 10,
       "Title": "Mal começo",
    },
]

def listar_todos_livros():
    return Livros


def buscar_livro_por_id(livro_id):
    return next((a for a in Livros if a["id"] == livro_id), None)


def inserir_livro(novo_livro):
    novo_id = max((livro["id"] for livro in Livros), default=0) + 1
    novo_livro["id"] = novo_id
    Livros.append(novo_livro)
    return novo_livro


def atualizar_livro_db(livro_id, dados):
    livro = buscar_livro_por_id(livro_id)
    if livro:
        livro["Title"] = dados.get("Title", livro["Title"])
       
    return livro


def deletar_livro_db(livro_id):
    livro = buscar_livro_por_id(livro_id)
    if livro:
        livro.remove(livro)
        return True
    return False


