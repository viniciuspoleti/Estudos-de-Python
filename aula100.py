# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos produtos por deep copy (cópia profunda)

import copy




produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]



# Ordene os produtos por nome decrescente (do maior para o menor)
# Gere produtos_ordenados_por_nome por deep copy

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

# Ordene os produtos por preço crescente (do menor para o maior)
# Gere produtos_ordenados_por_preco por deep copy

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(novos_produtos),
    key=lambda p: p['preco']
)


print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')
print()
print(*produtos, sep='\n')

