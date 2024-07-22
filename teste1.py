class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome(self):
        print(self.nome, self.sobrenome)

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, valor):
        self._cpf = valor


class Cpf:
    def __init__(self, cpf):
        self.cpf = cpf


class Cliente(Pessoa):
    def __init__(self, categoria, enderecos):
        self.categoria
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero


nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')

p1 = Pessoa(nome, sobrenome)

cpf = input('Digite o seu CPF: ')

p1.cpf = cpf

resposta = input('A pessoa em questão é um cliente? ')

if resposta[0].upper() == 'S':
    c1 = Cliente
    c1.nome = nome
    c1.sobrenome = sobrenome
    c1.cpf = cpf
    categoria = input('A qual categoria pertence este cliente? ')
    c1.categoria = categoria

    while True:
        # c1.inserir_endereco(input('Digite a rua: '), input('Digite o número: '))
        c1.rua = input('Digite a rua: ')
        c1.numero = input('Digite o número do endereço: ')
        # c1.inserir_endereco(rua=input('Digite a rua: '), numero=input('Digite o número: '))
        sair = input('Deseja adicionar mais endereços? ')
        if sair[0].upper() == 'N':
            break
    print(c1.nome, c1.sobrenome, c1.cpf, c1.categoria)
    c1.listar_enderecos(c1)
