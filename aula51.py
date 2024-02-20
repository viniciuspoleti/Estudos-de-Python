""" 
Introdução ao desempacotamento + tuples(tuplas)
"""

nomes = ['Maria', 'Helena', 'Luiz']
_, nome, *_ = nomes
print(nome, _)