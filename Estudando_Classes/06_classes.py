#mantendo estados de uma classe:
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já esta filmando...')
            return

        print(f'{self.nome} esta filmando...')
        self.filmando = True
        
    def para_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não esta filmando...')
            return

        print(f'{self.nome} esta parando de filmar...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar, já esta filmando...')
            return
        else:
            print(f'{self.nome} esta fotografando...')


c1 = Camera('Cannom')
c2 = Camera('Sony')
c1.filmar()
c1.fotografar()
c1.para_filmar()
c1.fotografar()
print(c1.filmando)
print(c2.filmando)
