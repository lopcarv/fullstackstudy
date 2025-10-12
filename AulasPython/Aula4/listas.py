numeros= [10, 20, 30,  17, 58, 6]
#print(numeros[5])

carros = ['Palio', 'gol', 'Omega', 'Virtus',  'Ka', 'Onix', 'Corola']
print('1 ->' , carros)

carros.append('Kombi')
print('2 ->' , carros)

carros.remove('gol')
print('3 ->' , carros)

del carros[3]
print('4 ->' , carros)

carros = sorted(carros)
print('5 ->' , carros)

for i in carros:
    print(i)