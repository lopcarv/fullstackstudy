class Produto:
    def __init__(self, codigo, nome, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.quantidade = quantidade
        
    def mostrar_detalhes(self):
        print("Código: ", self.codigo)
        print("Nome: ", self.nome)
        print("Quantidade: ", self.quantidade)
        
    def adicionar_estoque(self, quantidade):
        self.quantidade += quantidade
# Criando um objeto "produto1" 
produto1 = Produto(1, "Camisa", 10)

# Chamando método "ostrar_detalhes" do objeto "produto1"
produto1.mostrar_detalhes()

# Adicionando estoque ao objeto "produto1"
produto1.adicionar_estoque(5)

# chamando o metodo "mostrar_detalhes" novamente para verificar a quantidade atualizada
produto1.mostrar_detalhes()

