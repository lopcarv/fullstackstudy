import csv 
from pip._vendor.msgpack.fallback import newlist_hint
from pip._vendor.rich.console import NewLine
carros = [
    ['VW', 'Fusca', '1967'],
    ['GM', 'Opala', '1978'],
    ['Ford', 'Corcel', '1969'],
    ['Chevrolet', 'Celta', '2006'],
    
]

with open('carros.csv', 'w', newline='') as arquivo:
    fileCSV = csv.writer(arquivo, delimiter=';')
    
    fileCSV.writerow(['Marca', 'Modelo', 'Ano'])
    fileCSV.writerows(carros)