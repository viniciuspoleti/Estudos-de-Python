"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)

soma(
    x= int(input('Digite o valor de x: ')), 
    y= int(input('Digite o valor de y: ')), 
    z= int(input('Digite o valor de z: '))
    )

soma(1, 2, 3)
soma(1, y=2, z=5)

print(1, 2, 3, sep='-')