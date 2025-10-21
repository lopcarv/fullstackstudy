import json

pessoas = [
    {"nome": "João", 'telefone':'(85) 9865-4569', "idade": 30, "cidade": "São Paulo"},
    {"nome": "Maria", 'telefone':'(85) 9875-1234', "idade": 25, "cidade": "Rio de Janeiro"},
    {"nome": "Pedro", 'telefone':'(85) 9854-7896', "idade": 35, "cidade": "Belo Horizonte"}
    ]
with open('pessoas.json', 'w') as arquivo:
    json.dump(pessoas, arquivo, indent=4)

import os
print(os.path.abspath('pessoas.json'))


    
