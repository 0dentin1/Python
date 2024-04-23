valor = float(input('Qual é o valor do seu produto? '))
desc = valor - (valor * 5 / 100)
print(f'Este produto vai sair de R${valor}, na promoção vai sair por R${desc:.2f}')
