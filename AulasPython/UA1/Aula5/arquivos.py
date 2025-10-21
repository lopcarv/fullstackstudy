arquivo = open('pessoas.txt', 'w')

arquivo.write('João\n')
arquivo.write('Orien\n')
arquivo.write('Maria\n')

arquivo.close()

with open('pessoas.txt', 'r+') as arquivoleitura:
    for linha in arquivoleitura:
        print(linha)




  