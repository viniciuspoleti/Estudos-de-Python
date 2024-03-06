# Problemas dos parâmetros mutáveis em funções Python
def adciona_clientes(nome, lista=[]):
   lista.append(nome)
   return lista
   
cliente1= adciona_clientes('Vinicius')
adciona_clientes('Joana', cliente1)
print(cliente1)
    
    