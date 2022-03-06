import requests # módulo utilizado para fazer requisições

#usa a biblioteca requests para abrir uma conexao com o viacep
def cep_to_bairro(cep):
     url = f"https://viacep.com.br/ws/{cep}/json/"
     response = requests.get(url)
     if response.status_code != 200:
         pass #TODO, lançar um erro
     dicionario_retornado = response.json()
     return dicionario_retornado['bairro']