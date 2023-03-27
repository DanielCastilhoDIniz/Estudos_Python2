'''cpf = input('type your CPF:')

temp = [] # armazenar str como int temporariamente
truecpf = []
for i, in cpf:
    temp.append(int(i))
    truecpf.append(int(i))


if len(cpf) > 11:
    print('CPF INVALIDO!')

lista1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
soma1 = 0
for t, b in enumerate(lista1):
    soma1 += temp[t] * b

digito1 = 11 - (soma1 % 11)

if digito1 > 9:
    digito1 = 0
#print(digito1)

# 2° digito

lista2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
soma2 = 0
for h, j in enumerate(lista2):
    soma2 += temp[h] * j
    #print(f'{temp[h]} * {j} = {temp[h] * j}')
#print(soma2)
digito2 = 11 - (soma2 % 11)

if digito2 >= 9:
    digito2 = 0
#print(digito2)

novo_cpf = temp
novo_cpf[9] = digito1
novo_cpf[10] = digito2

print(novo_cpf)
print(truecpf)
print(temp)
if (set(truecpf) == set(novo_cpf)):
    print('CPF valido')
else:
    print('CPF invalido') '''
consultarcpf = int(input('Deseja consultar válido CPF? (1 - sim, 2 - não) \n'))
while consultarcpf == 1:
    cpf = input('type your CPF: ')
    while len(cpf) != 11:           #verifica quantidade de digitos do cpf
        print('ERRO! Digite um CPF com 11 números\n')
        cpf = input('type your CPF:')
        break

    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9
        total += int(novo_cpf[index]) * reverso
        #print(cpf[index], index, reverso)
        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)
            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)
    sequencia = cpf == str(novo_cpf[0]) * 11
    print(novo_cpf)
    if cpf == novo_cpf and not sequencia:
        print('CPF Válido')
    else:
        print('CPF inválido')
    consultarcpf = input('Deseja consultar CPF? (1 - sim, 2 - não) \n')
else:
    print('FIM DA CONSULTA')