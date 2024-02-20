#dir, hasattr e getattr em Python

string = 'Vinicius'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
    # print(string)
else:
    print('Não existe o método', metodo)
