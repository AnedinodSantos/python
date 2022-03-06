from requests import exceptions
from flask import Flask # módulo utilizao para criar um web service / api
from consulta_cep import cep_to_bairro


app = Flask(__name__) #instancio um objeto chamado app
#uma burocracia que a gente faz sempre

bairros_atende = ["Barra Funda", "Lapa", "Parque Residencial da Lapa", "Vila Invernada"]


# Consulta o CEP no Via CEP e retorna o nome do bairro caso a requisição tenha
# sucesso
@app.route("/bairro/<cep>")
def bairro(cep):
    try:
        resposta = cep_to_bairro(cep)
    except exceptions.HTTPError as err:
        return {"status": err.response.status_code, "resp":'', "info": err.args[0]}
    return {"status": 200,"resp": resposta, "info": "Este e o bairro do CEP"}


# adiciona um bairro na lista de bairros que a empresa atende
@app.route("/bairros/<nome>", methods=["PUT"])
def add_bairro(nome):
    if nome not in bairros_atende:
        bairros_atende.append(nome)
        return {"status": 200, "resp": "sucesso", "info": "bairro adicionado com sucesso à base de dados"}
    else:
        return {"status": 409, "resp": "conflito", "info": "bairro já está cadastrado na base de dados"}












#o meu servidor tem uma URL bairro
# eu firefox -> meu servidor -> viacep
#            <-               <-
@app.route("/atende/<cep>")
def atende(cep):
    bairro = cep_to_bairro(cep)
    return {"atende": bairro in bairros_atende, "status": "ok"}



#TODO adicionar remoção de bairro

if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)
