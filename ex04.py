"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

def zipper(l1, l2):
    intervalo = min(len(l1), len(l2))
    return [(l1[i] + l2[i]) for i in range(intervalo)]

lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4, 6, 9, 10, 20]

lista_soma = zipper(lista_a, lista_b)
print(lista_soma)