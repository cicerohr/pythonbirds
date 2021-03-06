"""
Para rodar os testes no terminal digite python3 -m unittest discover oo.
Sendo que oo é o diretório onde esta os testes
"""
from unittest import TestCase

from oo.carro import Motor


class CarroTesteCase(TestCase):
    def teste_velocidade_inicial(self):
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)

    def teste_frear(self):
        motor = Motor()
        motor.frear()
        self.assertEqual(0, motor.velocidade)


if __name__ == '__main__':
    pass
