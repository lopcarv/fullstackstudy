# Programa para calcular metros quadrados (m²)
print("-" * 30)
print("  CALCULADORA DE TERRENO")
print("-" * 30)

# O float() serve para aceitar números com vírgula (usando ponto no código)
largura = float(input("Digite a largura do terreno (em metros): "))
comprimento = float(input("Digite o comprimento do terreno (em metros): "))

# O cálculo matemático: Área = Largura x Comprimento
area = largura * comprimento

print("-" * 30)
print(f"O terreno de {largura}m x {comprimento}m possui:")
print(f"Área Total: {area:.2f} m²")
print("-" * 30)