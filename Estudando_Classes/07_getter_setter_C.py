class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self._idade = idade 

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 0:
            raise ValueError("Idade deve ser um número positivo")
        self._idade = nova_idade


p1 = Pessoa("Daniel", 30)
print(p1.idade)
p1.idade = 40
print(p1.idade)
p1.idade = -20


# sem o uso dos decoradores o codigo abaixo quebra, um alternativa seria desproteger a atributo o que no caso não faz sentido
# já desjamos que ele seja util apenas dentro da classe


# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self._idade = idade


#     def idade(self):
#         return self._idade


#     def idade(self,nova_idade):
#         if nova_idade < 0:
#             raise ValueError("Idade deve ser um número positivo")
#         self._idade =nova_idade

# p1 = Pessoa("Daniel", 30)
# print(p1.idade)
# p1.idade = 40
# print(p1.idade)
p1.idade = -20
