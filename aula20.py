primeiro_valor = input('Digite um valor ')
segundo_valor = input('Digite outro valor ')

if primeiro_valor > segundo_valor:
    print(f'O primeiro valor "{primeiro_valor}"'
          f' é maior que o segundo valor'
         f' "{segundo_valor}"')
elif segundo_valor > primeiro_valor:
    print(f'O segundo valor "{segundo_valor}"'
         f' é maior que o primeiro valor'
         f' "{primeiro_valor}"')
else:
    print(f'Os valores são iguais'
          f' "{primeiro_valor}"')