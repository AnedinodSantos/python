from requests import exceptions
from flask import Flask, request # módulo utilizao para criar um web service / api
from consulta_cep import cep_to_bairro


app = Flask(__name__) #instancio um objeto chamado app
#uma burocracia que a gente faz sempre

# carga de bairros para teste
bairros_atende = ["Barra Funda", "Lapa", "Parque Residencial da Lapa", "Vila Invernada"]


@app.route("/")
def home():
    return "<h1> Bem vindo <h1/>"


# adiciona um bairro na lista de bairros que a empresa atende
@app.route("/bairro/adiciona", methods=["PUT"])
def add_bairro():
    nome = request.json["nome"]
    if nome not in bairros_atende:
        bairros_atende.append(nome)
        return {"status": 200, "resp": "sucesso", "info": "bairro adicionado com sucesso à base de dados"}
    else:
        return {"status": 409, "resp": "conflito", "info": "bairro já está cadastrado na base de dados"}


# remove bairro da lista de bairros que a empresa atende
@app.route("/bairro/remove", methods=["DELETE"])
def remove_bairro():
    nome = request.json["nome"]
    if nome in bairros_atende:
        bairros_atende.remove(nome)
        return {"status": 200, "resp": "sucesso", "info": "bairro removido com sucesso da base de dados"}
    else:
        return {"status": 404, "resp": "não encontrado", "info": "bairro não encontrado na base de dados"}


# lista todos os bairros que a empresa atende
@app.route("/bairros")
def listar_bairros():
    return {"status": 200, "resp": bairros_atende, "info": "lista com todos os bairros que a empresa atende"}


# procura um bairro pelo CEP na lista de bairros
@app.route("/consulta/bairro/cep/<cep>")
def consulta_por_cep(cep):
    try:
        resposta = cep_to_bairro(cep)
    except exceptions.HTTPError as err:
        return {"status": err.response.status_code, "resp":'', "info": err.args[0]}

    if resposta in bairros_atende:
        info = f"o bairro {resposta} é atendido pela empresa"
        return {"status": 200, "resp": "sucesso", "info": info}
    else:
        info = f"o bairro {resposta} não é atendido pela empresa"
        return {"status": 404, "resp": "não encontrado", "info": info}



# procura um bairro pelo nome na lista de 
@app.route("/consulta/bairro/nome/<nome>")
def consulta_por_nome(nome):
    if nome in bairros_atende:
        info = f"o bairro {nome} é atendido pela empresa"
        return {"status": 200, "resp": "sucesso", "info": info}
    else:
        info = f"o bairro {nome} não é atendido pela empresa"
        return {"status": 404, "resp": "não encontrado", "info": info}


if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)
