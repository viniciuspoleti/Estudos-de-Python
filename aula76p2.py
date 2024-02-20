# Manipulando chaves e valores em dicionários

pessoa = {}

chave = 'nome'

pessoa[chave] = 'Vinicius Dante'
pessoa['sobrenome'] = 'Poleti'

print(pessoa)
print(pessoa[chave])

pessoa[chave] = 'Maria'

# del pessoa['sobrenome']
print(pessoa)

if pessoa.get('sobrenome', None) is None:
    print('Não Existe')
else:
    print(pessoa['sobrenome'])
    

    
