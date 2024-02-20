# Operadores in e not in
# Strings são iteraveis
# 0 1 2 3 4 5 6 7 
# V i n i c i u s
#--8-7-6-5-4-3-2-1

#nome = 'Vinicius'

#print(nome[-3])

#print('n' in nome)
#print('a' in nome)
#print('cius' in nome)
#print(10 * '_')
#print('cius' not in nome)
#print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

