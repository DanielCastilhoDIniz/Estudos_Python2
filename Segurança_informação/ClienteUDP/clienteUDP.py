import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Cliente Socket criado com sucesso!")

host = 'localhost'
port = 5432
mensagem = " Olá servidor!!!"

try:
    print("Cliente" + mensagem)
    s.sendto(mensagem.encode(), (host, port))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print("Cliente: " + dados)
finally:
    print("Cliente: Fechando a conexão")
    s.close()
