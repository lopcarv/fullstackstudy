
class Produto:
    
    def __init__(self):
        self.nome = ''
        self.marca = ''
        self.modelo = ''
        self.valor = ''
        
Produto0 = Produto()
Produto0.marca = 'Sansung'
Produto0.valor = 5000

Produto1 = Produto()

Produto2 = Produto()

print(Produto0.__dict__)
print(Produto1.__dict__)
print(Produto2.__dict__)