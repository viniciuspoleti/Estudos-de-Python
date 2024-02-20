# (Parte1) try e except para tratar exceções
# a = 18
# b = 0
# c = a / b
# string = 'Vinicius'
# print(isinstance(string, str))

try:
    a = 18
    b = 0
    # print(b[0])
    print('Linha 1'[1000])
    # c = a / b
    print('Linha 2')
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')