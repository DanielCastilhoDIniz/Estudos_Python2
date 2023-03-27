class Aluno:
    def __init__(self, nome: str, idade: int, endereco: str):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def imprime_endereco(self):
        print(self.nome)
        print(self.endereco)

    def mudar_endereco(self, novo_endereco: str):
        self.endereco = novo_endereco


daniel = Aluno("Daniel Castilho", 39, "Rua da lua n 73 João Pessoa")

daniel.imprime_endereco()

daniel.mudar_endereco("Rua do Sol, Quente 123")

daniel.imprime_endereco()
