class Aluno ():
    def __init__(self, nome: str, idade: int, endereco: str):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def imprime_endereco(self):
        print(self.nome)
        print(self.endereco)

    def mudar_endereco(self, novo_endereco: str):
        self.endereco = novo_endereco
        
        
        
daniel = Aluno("Daniel", 39, " Rua abcd ef nro 123")

