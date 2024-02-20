""" 
Introdução às funções (def) em Python
Funções são trechos de código usados para
replicar determinad aação ao longo do código
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada)
"""

def imprimir(a, b, c):
    print(a, b, c)
    

imprimir(1, 2, 3)
imprimir('a', 'b', 'c')

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}')
    
entrada = input('Digite seu nome: ')
saudacao()
saudacao(entrada)