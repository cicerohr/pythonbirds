"""pessoa.py em 2021-03-01. Projeto pythonbirds.



"""


class Pessoa:
    olhos = 2  # atributo default ou atributo de classe

    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_classe_pai = super().cumprimentar()
        return f'{cumprimentar_classe_pai}. Aperto de mão.'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    renzo = Mutante(nome='Renzo')
    cicero = Homem(renzo, nome='Cícero')
    print(Pessoa.cumprimentar(cicero))
    print(id(cicero))
    print(cicero.cumprimentar())
    print(cicero.nome)
    print(cicero.idade)
    for filho in cicero.filhos:
        print(filho.nome)
    cicero.sobrenome = 'Rodrigues'  # atributo criado dinamicamente para esta instancia
    print(cicero.__dict__)
    print(renzo.__dict__)
    del cicero.filhos
    cicero.olhos = 1
    print(cicero.__dict__)
    print(renzo.__dict__)
    print(Pessoa.olhos)
    print(cicero.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(cicero.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), cicero.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), cicero.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(renzo, Pessoa))
    print(isinstance(renzo, Homem))
    print(renzo.olhos)
    print(cicero.cumprimentar())
    print(renzo.cumprimentar())
