"""pessoa.py em 2021-03-01. Projeto pythonbirds.



"""


class Pessoa:
    def __init__(self, nome: str = None, idade: int = 35) -> None:
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Cícero')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Renzo'
    print(p.nome)
    print(p.idade)
