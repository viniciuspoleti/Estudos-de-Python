"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu nome: ')
tamanho = len(nome)

if tamanho > 1:
    if tamanho <= 4:
        print(f'Seu nome {nome} é curto')
    elif tamanho < 6:
        print(f'Seu nome {nome} é normal')
    else:
        print(f'Seu nome {nome} é muito grande')
else:
    print('Digite mais de uma letra')