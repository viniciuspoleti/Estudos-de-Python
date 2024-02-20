""" 
Iterando strings com while
"""

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)
contador = 0
novo_nome = ''

while contador < tamanho_nome:
    letra = nome[contador]
    novo_nome += f'*{letra}'
    print(novo_nome) 
    contador += 1
    
    
novo_nome += '*'
print(novo_nome)