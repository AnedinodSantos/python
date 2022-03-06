import requests # módulo utilizado para fazer requisições

# usa a biblioteca requests para abrir uma conexao com o viacep e retorna
# o nome do bairro conforme o cep pesquisado
def cep_to_bairro(cep):
     url = f"https://viacep.com.br/ws/{cep}/json/"
     response = requests.get(url) # faço a requisição
     response.raise_for_status() # lanço exceção HTTP
     dic_bairro = response.json()
     return dic_bairro['bairro']