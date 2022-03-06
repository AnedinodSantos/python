# Projeto de API simples

Nesse pequeno projeto criarei uma API simples que conversa com a API VIACEP.

Escopo do projeto: será um serviço de verificação que retorna ao cliente se
a empresa atende ou não ao bairro do mesmo.
Para tanto, a empresa tem de cadastrar os bairros que atende. O cliente ao
definir seu bairro recebe uma resposta do sistema se a empresa atende ou não
o seu bairro.
Esse atendimento pode ser qualquer coisa: entregas, serviços variados,
consultorias. O nosso foco é só disponibilizar a API de forma geral.

Teremos algumas funcionalidades simples como:

- adicionar bairro na lista de bairros que a empresa atende
- remover bairro da lista
- listar bairros que a empresa atende
- encontrar um bairro que a empresa atende pelo CEP
- encontrar um bairro que a empresa atende pelo nome