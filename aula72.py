""" 
Exercícios com fonções 
Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável
Crie uma função falsa se um número é par ou ímpar
retorne se o número é  par o ímpar
"""

def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total 
     
    
    
def par_impar(numero):
    if numero % 2 == 0:
        return 'Par' 
    return 'Impar'
    

print(1*2*3*4*5*6)
conta = multiplicacao(1, 3, 5, 7,111)

print(conta)
e_par_impar = par_impar(conta)
print(e_par_impar)