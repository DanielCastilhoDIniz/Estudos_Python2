"""_summary_

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
import json
caminho_arquivo = "05_b_classes.json"


class Aluno():

    todos_alunos = []

    def __init__(self, nome, matricula, curso, nota1, nota2, nota3, media=None):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.media = media
        Aluno.todos_alunos.append(self)

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.curso}"

    @classmethod
    def consultar_pessoas(cls):
        for aluno in cls.todos_alunos:
            print(aluno)
            
    def calcular_media(self):
        self.media = (self.nota1 + self.nota2 + self.nota3)/3
        return self.media

    def adicionar_alunos_lista(self, aluno):
        self.alunos.extend(aluno)


# def mostrar_valores(*objs):
#     for obj in objs:
#         print(obj)


a1 = Aluno("Daniel", 1223456, "DAS", 7, 8, 7)
a1.calcular_media()
a1.adicionar_alunos_lista
a2 = Aluno("Luiz", 1223450, "DAS", 9, 8, 9)
a2.calcular_media()
a2.adicionar_alunos_lista
a3 = Aluno("Pedro", 1223450, "DAS", 9, 8, 9)
a3.calcular_media()
a3.adicionar_alunos_lista

print(a1.media)
Aluno.consultar_pessoas()

# for aluno in alunos:
#     maior = None
#     if alunos.media > maior:
#         maior = alunos.media
# em andamento....
