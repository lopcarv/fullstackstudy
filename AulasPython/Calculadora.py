def exibir_menu():
    print("\n🧮 Calculadora de Conversões")
    print("Escolha o tipo de conversão:")
    print("1. Comprimento (metros <-> quilômetros)")
    print("2. Armazenamento (bits, bytes, KB, MB, GB, TB)")
    print("3. Sair")

def converter_comprimento():
    print("\n📏 Conversão de Comprimento")
    print("1. Metros para Quilômetros")
    print("2. Quilômetros para Metros")
    opcao = input("Escolha uma opção (1/2): ")
    valor = float(input("Digite o valor: "))

    if opcao == '1':
        resultado = valor / 1000
        print(f"{valor} metros = {resultado:.6f} quilômetros")
    elif opcao == '2':
        resultado = valor * 1000
        print(f"{valor} quilômetros = {resultado} metros")
    else:
        print("Opção inválida.")

def converter_armazenamento():
    print("\n💾 Conversão de Armazenamento")
    print("De: bits, B, KB, MB, GB, TB")
    unidade_origem = input("Digite a unidade de origem (ex: MB): ").strip().upper()
    valor = float(input("Digite o valor: "))
    unidade_destino = input("Digite a unidade de destino (ex: GB): ").strip().upper()

    # Dicionário com os fatores em relação ao byte
    fatores = {
        'BIT': 0.125,
        'B': 1,
        'KB': 1024,
        'MB': 1024 ** 2,
        'GB': 1024 ** 3,
        'TB': 1024 ** 4
    }

    if unidade_origem in fatores and unidade_destino in fatores:
        total_em_bytes = valor * fatores[unidade_origem]
        resultado = total_em_bytes / fatores[unidade_destino]
        print(f"{valor} {unidade_origem} = {resultado:.6f} {unidade_destino}")
    else:
        print("Unidade inválida.")

# Programa principal
while True:
    exibir_menu()
    escolha = input("Digite sua escolha (1/2/3): ")

    if escolha == '1':
        converter_comprimento()
    elif escolha == '2':
        converter_armazenamento()
    elif escolha == '3':
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida.")