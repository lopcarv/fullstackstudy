class Imovel:
    def __init__(self, nome, uf, valor, endereco='', area=''):
        self.nome = nome
        self.uf = uf
        self.valor = valor
        self.endereco = endereco
        self.area = area
        
    def detalhar(self):
        print(self.__dict__)
        
    def calcularImposto(self):
        return self.valor * 0.02

# O código abaixo deve ficar fora da classe (sem espaços no início da linha)
meu_imovel = Imovel('Solar do Cerrado', 'DF', 5000000)
meu_imovel.endereco = 'ABC'
meu_imovel.area = '2000'
meu_imovel.detalhar()

imposto = meu_imovel.calcularImposto()
print(f"O imposto a pagar é: R$ {imposto:,.2f}")