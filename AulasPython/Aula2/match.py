'''
dia = int(input("Digite o numero do dia da Semana: "))


if dia == 1:
    print("Domingo")
    
if dia == 2:
    print("Segunda")
    
if dia == 3:
    print("Terça")

if dia == 4:
    print("Quarta")
    
if dia == 5:
    print("Quinta")
    
if dia == 6:
    print("Sexta")

if dia == 7:
    print("Sabado")

else:
    print("Esse dia não existe")

'''

dia = int(input("Digite o número do dia da semana: "))

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4:
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sábado")
    case _:
        print("Esse dia não existe")                                        