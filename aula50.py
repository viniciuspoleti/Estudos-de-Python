""" 
for in com listas
"""

lista = ['Maria', 'Helena', 'Luiz', 'Pedro']
indices = range(len(lista))

for contador in indices:
    print(contador, lista[contador], type(lista[contador]))
    contador += 1