'''cop = float(input('Digite o comprimento do cateto oposto: '))
cadj = float(input('Digite o comprimento do cateto adjacente: '))
h = (cop ** 2 + cadj ** 2) ** (1/2)
print(f'A hipotenusa vai medir {h:.2f}')'''

import math
cop = float(input('Digite o comprimento do cateto oposto: '))
cadj = float(input('Digite o comprimento do cateto adjacente: '))
h = math.hypot(cop, cadj)
print(f'A hipotenusa vai medir {h:.2f}')