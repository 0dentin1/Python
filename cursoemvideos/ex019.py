import math
num = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(num))
print(f'O ângulo de {num} tem o SENO de {seno:.2f}')
cos = math.cos(math.radians(num))
print(f'O ângulo {num} tem o COSSENO de {cos:.2f}')
tang = math.tan(math.radians(num))
print(f'O ângulo de {num} tem a TANGENTE de {tang:.2f}')