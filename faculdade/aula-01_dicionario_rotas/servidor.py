from flask import Flask # módulo utilizao para criar um web service / api
from consulta_cep import cep_to_bairro


app = Flask(__name__) #instancio um objeto chamado app
#uma burocracia que a gente faz sempre

#o meu servidor tem uma URL bairro
# eu firefox -> meu servidor -> viacep
#            <-               <-
@app.route("/bairro/<cep>")
def bairro(cep):
    bairro = cep_to_bairro(cep)
    return {"bairro": bairro, "status": "ok"}
    #TODO tratar o erro, devolvendo um dicionario mais informativo para o usuario, e um status code 500

bairros_atende = ["Barra Funda", "Lapa", "Parque Residencial da Lapa", "Vila Invernada"]

#o meu servidor tem uma URL bairro
# eu firefox -> meu servidor -> viacep
#            <-               <-
@app.route("/atende/<cep>")
def atende(cep):
    bairro = cep_to_bairro(cep)
    return {"atende": bairro in bairros_atende, "status": "ok"}

#adiciona um bairro, pra eu nao precisar ficar mexendo no codigo pra adicionar
#bairros. Mas isso eu vou mostrar mais pra frente (se quiser brincar com isso
# aprenda primeiro como funciona a biblioteca requests)
@app.route("/bairros/<nome>", methods=["PUT"])
def add_bairro(nome):
    if nome not in bairros_atende:
        bairros_atende.append(nome)
        return {"bairro_adicionado": nome, "status": "ok"}
    #TODO: adicionar tratamento de erro se o bairro já está na lista. Status code 400.

#TODO adicionar remoção de bairro

if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)
