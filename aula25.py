"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Vinicius'
preco = 1000.95897643
variavel = '%s, o preço total foi R$%.2f' %(nome, preco)
print(variavel)
print('O hexadecimal de %d é %X' %(255, 255))