larg = float(input('Qual a largura do cômodo que você deseja pintar? '))
alt = float(input('Qual a altura do cômodo que você deseja pintar? '))
area = larg * alt
print(f'A parede do seu cômodo tem uma área de {area:.2f}m²')
tinta = area / 2
print(f'E você vai precisar de {tinta:.2f}l de tinta')