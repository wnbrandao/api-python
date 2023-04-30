from flask import Flask, jsonify, request

app = Flask(__name__)

lista_livros = [
    {
        'id': 1,
        'título': 'O Senhor dos Anéis - A Sociedade do Anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'título': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'título': 'Hábitos Atômicos',
        'autor': 'James Clear'
    },
]
###

#Lista
@app.route('/getall',methods=['GET'])
def obter_livros():
    return jsonify(lista_livros)

#GET's
@app.route('/id=<int:id>',methods=['GET'])
def puxar_por_id(id):
    for livro in lista_livros:
        if livro.get('id') == id:
            return jsonify(livro)

@app.route('/nome=<nome>',methods=['GET'])
def puxar_por_nome(nome):
    for livro in lista_livros:
        if livro.get('título') == nome:
            return jsonify(livro)

@app.route('/autor=<autor>',methods=['GET'])
def puxar_por_autor(autor):
    for livro in lista_livros:
        if livro.get('autor') == autor:
            return jsonify(livro)

#Altera
@app.route('/alteraporid=<int:id>',methods=['PUT'])
def editar(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(lista_livros):
        if livro.get('id') == id:
            lista_livros[indice].update(livro_alterado)
            return jsonify(lista_livros[indice])
        

#Criar novo
@app.route ('/add',methods=['POST'])
def incluir():
    novo_livro = request.get_json()
    lista_livros.append(novo_livro)
    return jsonify(lista_livros)

#deleta
@app.route ('/delete=<int:id>', methods=['DELETE'])
def excluir(id):
    for indice, livro in enumerate(lista_livros):
        if livro.get('id') == id:
            del lista_livros[indice]
            return jsonify(lista_livros)

app.run(port=5000,host='localhost',debug=True)