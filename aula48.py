""" 
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""

lista = [123, True, 'Vinicius Dante', 1.2]
print(lista)
lista[2] += ' Poleti'
print(lista[2][0], lista[2])
del lista[3]
print(lista)
lista.append(200)
lista.pop()
lista.append(300)
lista.append(400)
lista.append(500)
print(lista, len(lista))
