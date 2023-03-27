class Aluno:
    def __init__(self, nome, matricula, curso, nota1, nota2, nota3):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.media = None

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.curso}"

    def calcular_media(self):
        self.media = (self.nota1 + self.nota2 + self.nota3) / 3
        return self.media


def adicionar_alunos(lista_alunos, *alunos):
    lista_alunos.extend(alunos)


a1 = Aluno("Daniel", 1223456, "DAS", 7, 8, 7)
a1.calcular_media()

a2 = Aluno("Luiz", 1223450, "DAS", 9, 8, 7)
a2.calcular_media()

alunos = []
adicionar_alunos(alunos, a1, a2)

for aluno in alunos:
    print(aluno, aluno.media)
    
    
    
a1 = Aluno("Daniel", 1223456, "DAS", 7, 8, 7)
a1.calcular_media()
a2 = Aluno("Luiz", 1223450, "DAS", 9, 8, 7)
a2.calcular_media()
