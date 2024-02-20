import os
# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4

def multiplicador(multiplo):
    def multiplicar(numero):
        return numero * multiplo
    return multiplicar

numeros_validos = None
while numeros_validos == None:    
    numero = input('Digite um número: ')
    num_float = 0
    mult = input (f'Digite por quanto {numero} será multiplicado: ')
    mult_float = 0
    try:
        num_float = float(numero)
        mult_float = float(mult)
        numeros_validos = True
   
    except :
        numeros_validos = None
        continue
   
        
        
duplicar = multiplicador(2)
triplicar = multiplicador(3)
quadruplicar = multiplicador(4)
novo_multiplicador = multiplicador(mult_float)

os.system('cls')
print(f'O número {numero} multiplicado por {mult} é {novo_multiplicador(num_float)}')
print(f'O dobro de {numero} é {duplicar(num_float)}' )
print(f'O triplo de {numero} é {triplicar(num_float)}' )
print(f'O quadruplo de {numero} é {quadruplicar(num_float)}' )