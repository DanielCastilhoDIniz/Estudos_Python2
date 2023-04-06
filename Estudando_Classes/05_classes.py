"""
    . Crie uma classe representando os alunos de um determinado curso. A classe deve
conter os atributos matrıcula do aluno, nome, nota da primeira prova, nota da segunda
prova e nota da terceira prova. Crie metodos para acessar o nome e a méedia do aluno. 
(a) Permita ao usuario entrar com os dados de 5 alunos. 
(b) Encontre o aluno com maior media geral. 
(c) Encontre o aluno com menor media geral 
(d) Para cada aluno diga se ele foi aprovado ou reprovado, considerando o valor 6 para

salvar dados em JSON
aprovação
"""

class Aluno:
    def __init__(self, matricula, nome, nota1, nota2, nota3):
        self.matricula = matricula
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.media = self.calcular_media()

    def calcular_media(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

    def get_nome(self):
        return self.nome

    def esta_aprovado(self):
        return self.media >= 6

    def __str__(self):
        return f"Aluno: {self.nome}\nMatrícula: {self.matricula}\nMédia: {self.media:.2f}\n"


if __name__ == "__main__":
    alunos = []

    for i in range(2):
        matricula = input("Digite a matrícula do aluno: ")
        nome = input("Digite o nome do aluno: ")
        nota1 = float(input("Digite a nota da primeira prova: "))
        nota2 = float(input("Digite a nota da segunda prova: "))
        nota3 = float(input("Digite a nota da terceira prova: "))

        aluno = Aluno(matricula, nome, nota1, nota2, nota3)
        alunos.append(aluno)

    aluno_com_maior_media = max(alunos, key=lambda a: a.media)
    aluno_com_menor_media = min(alunos, key=lambda a: a.media)

    print("\nAluno com maior média:")
    print(aluno_com_maior_media)

    print("Aluno com menor média:")
    print(aluno_com_menor_media)

    for aluno in alunos:
        status = "aprovado" if aluno.esta_aprovado() else "reprovado"
        print(f"{aluno.nome} está {status}.")
