class Aluno():
    def __init__(self, nome: str, matricula: int, curso: str):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso

    def mostrar_curso(self):
        print(self.curso)
        
    def alterar_curso(self,novo_curso:str):
        self.curso = novo_curso
        
    
c1 = Aluno("Daniel Castilho", 20232020, "Desenvolvimento de softwares")

print(c1.nome, c1.matricula, c1.curso)

c1.alterar_curso("Corte e costura")

print(c1.curso)