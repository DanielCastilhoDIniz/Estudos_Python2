"""
Crie uma classe Pessoa que tenha os atributos nome, idade e profissão. Em seguida, 
crie um objeto dessa classe e exiba seus atributos.
"""


class Pessoa:
    def __init__(self, nome: str, idade: int, profissao: str, endereco=""):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.endereco = endereco

    def mostrar_pessoa(self):
        print(
            f"Nome: {self.nome}\nIdade: {self.idade} anos\nProfissão: {self.profissao}")


p1 = Pessoa("Daniel Castilho Diniz", 39, "professor")
p1.mostrar_pessoa()
