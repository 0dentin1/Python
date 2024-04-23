import random
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
a5 = str(input('Quinto aluno: '))
lista = [a1, a2, a3, a4, a5]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')