"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
entrada = input('Digite a hora atual: ')

if entrada.isdigit():
    hora = int(entrada)
    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora > 11 and hora <= 17:
        print('Boa tarde')
    elif hora <= 23:
        print('Boa noite')
    else:
        print('Não conheço essa hora')
else:
    print('Valor fornecido não é horário válido')