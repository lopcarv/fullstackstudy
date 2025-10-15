'''
try:
    n1 = int(input('Número 1: '))
    n2 = int(input('Número 2: '))
    resultado = n1 / n2

    print(f"O resultado da divisão é {resultado}")

except Exception as erro:
    print(f"Ocorreu um erro: {erro}") 
'''
try:
    n1 = int(input('Número 1: '))
    n2 = int(input('Número 2: '))
    resultado = n1 / n2

    print(f"O resultado da divisão é {resultado}")

except ValueError:
    print(f"Favor digitar somente numeros") 
except ZeroDivisionError:
    print(f"nao é possivel dividir por zero")
    
except Exception as error:
    print(f"ocorreu um erro: ", error)
    
else:
    print("o programa foi executado corretamente")
finally: 
    print("fim")