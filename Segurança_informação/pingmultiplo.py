import os

with open('Segurança_informação\host.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        os.system('ping ' + ip)