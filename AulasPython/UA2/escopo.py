
# Escopo global
x = 10

def mostrar_escopos():
    # Escopo local
    y = 5
    print("Escopo global x:", x)
    print("Escopo local y:", y)

mostrar_escopos()

# Fora da função, só x está disponível
print("Fora da função, x:", x)
# print("Fora da função, y:", y)  # Isso gera erro, pois y é local
