import os
def soma(x, y):
    return x + y
    
def subtracao(x, y):
    return x - y
    
def divisao(x, y):
    return x / y
    
def multiplicacao(x, y):
    return x * y
    
def resto(x, y): 
    return x % y

def potencia(x, y):
    return x ** y
    
while True:
     numero_1 = input('Digite o valor de x: ')
     numero_2 = input('Digite o valor de y: ')
     numeros_validos = None
     num_1_float = 0
     num_2_float = 0
   
     try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
   
   
     except :
        numeros_validos = None
   
     if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos')
        continue
    
    
     operador = input('Selecione o tipo de operação a ser feita (+ - * / % ^): ')
    
     if operador not in '+-*/%^':
        print('Tipo de operação selecionada inválida.')
        continue
        
     if len(operador) > 1:
         print('Digite apenas um operador por vez')
         continue
     
     if operador == "+":
         res = soma(x= num_1_float, y= num_2_float)
    
     elif operador == '-':
         res = subtracao(x= num_1_float, y= num_2_float)
     
     elif operador == "*":
         res = multiplicacao(x= num_1_float, y= num_2_float)
    
     elif operador == "/":
         res = divisao(x= num_1_float, y= num_2_float)
     
     elif operador == '%':
         res = resto(x= num_1_float, y= num_2_float)
     
     else:
         res = potencia(x=num_1_float, y=num_2_float)
     
     print(f'{num_1_float} {operador} {num_2_float} = {round(res, 3)}')
         
     continuar = input('Deseja continuar? (S)im (N)ão: ')
     if continuar[0].upper() == 'N':
         break
     
     else:
         os.system('cls')
         continue
         
     
os.system('cls')
print('Você encerrou a calculadora')   
