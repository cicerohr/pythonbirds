"""pessoa.py em 2021-03-01. Projeto pythonbirds.



"""


class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    cicero = Pessoa(renzo, nome='Cícero')
    print(Pessoa.cumprimentar(cicero))
    print(id(cicero))
    print(cicero.cumprimentar())
    print(cicero.nome)
    print(cicero.idade)
    for filho in cicero.filhos:
        print(filho.nome)
