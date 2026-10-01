from flask import Flask, jsonify, request
import database

app = Flask(__name__)

# GET - Listar todos os livross
@app.route("/livros", methods=["GET"])
def listar_livros():
    return jsonify(database.listar_todos_livros())


# GET - Buscar livros por ID
@app.route("/livros/<int:id>", methods=["GET"])
def buscar_livro(id):
    livro = database.buscar_livro_por_id(id)
    if livro:
        return jsonify(livro)
    return jsonify({"erro": "Livro não encontrado"}), 404


# POST - Adicionar novo livros
@app.route("/livros", methods=["POST"])
def adicionar_livro():
    dados = request.get_json()

    if (
        not dados
        or "Title" not in dados
        
    ):
        return jsonify({"erro": "Dados incompletos"}), 400 

    novo_Livro = dados.inserir_livro(dados)

    return (
        jsonify(
            {"mensagem": "livros cadastrado com sucesso", "livro": novo_Livro}
        ),
        201,
    )


# PUT - Atualizar livros
@app.route("/livros/<int:id>", methods=["PUT"])
def atualizar_livro(id):
    dados = request.get_json() or {}
    livro_atualizado = database.atualizar_livro_db(id, dados)

    if not livro_atualizado:
        return jsonify({"erro": "livro não encontrado"}), 404

    return jsonify(
        {"mensagem": "livros atualizado com sucesso", "livro": livro_atualizado}
    )


# DELETE - Remover livros
@app.route("/livros/<int:id>", methods=["DELETE"])
def remover_livro(id):
    removido = database.deletar_livro_db(id)

    if not removido:
        return jsonify({"erro": "livro não encontrado"}), 404

    return jsonify({"mensagem": "livro removido com sucesso"})


# Executar aplicação
if __name__ == "__main__":
    app.run(debug=True)
