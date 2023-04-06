# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tel

class Car:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


gol = Car('Gol')
volkswagen = Fabricante('volkswagen')
gol.fabricante = volkswagen
motor_1_0 = Motor('Motor 1.0')
gol.motor = motor_1_0

print(gol.nome, gol.fabricante.nome, gol.motor.nome)

siena = Car('Siena')
fiat = Fabricante('Fiat')
siena.fabricante = fiat
motor_1_6 = Motor('Motor 1.6')
siena.motor = motor_1_6

print(siena.nome, siena.fabricante.nome, siena.motor.nome)



""" 
Explicando o códigos
ste código cria três classes: Car, Motor e Fabricante. A classe Car tem atributos para o nome do carro, 
o motor e o fabricante. O motor e o fabricante são definidos como atributos privados (_motor e _fabricante) 
e são acessados por meio de propriedades com os decoradores @property e @setter. O método init é usado para inicializar os atributos do objeto.

A classe Motor tem um único atributo, o nome do motor. A classe Fabricante também tem um único atributo, o nome do fabricante.

No final do código, três objetos são criados: um objeto Car com o nome "Gol", um objeto Fabricante com o nome "volkswagen" e 
um objeto Motor com o nome "Motor 1.0". O objeto Fabricante é atribuído ao atributo "fabricante" do objeto Car e 
o objeto Motor é atribuído ao atributo "motor" do objeto Car.

Finalmente, a impressão é usada para exibir o nome do carro, o nome do fabricante e o nome do motor. 
A saída do código será: "Gol volkswagen Motor 1.0". Isso significa que o objeto Car chamado "Gol" foi fabricado pela Volkswagen e possui um motor chamado "Motor 1.0".

"""