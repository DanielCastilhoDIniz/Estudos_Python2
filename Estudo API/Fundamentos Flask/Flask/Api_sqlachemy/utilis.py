from models import Pessoas



# insere dados na tabela pessoa
def inseri_pessoas():
    pessoa = Pessoas(nome='Pedro', idade=60)
    print(pessoa)
    pessoa.save()

# Realiza consula na tabela pessoa
def consulta():
    pessoas = Pessoas.query.all()
    print(pessoas)

# Altera dados na tabela pessoa
def aletera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Daniel').first()
    pessoa.idade = 39
    pessoa.save()
    print(pessoa.idade)

# Exclui dados na tabebla pessoas
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Pedro')
    pessoa.delete()


if __name__ == "__main__":
    # inseri_pessoas()
    consulta()
    aletera_pessoa()
    exclui_pessoa()
    consulta()
