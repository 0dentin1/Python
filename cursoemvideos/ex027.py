frase = str(input('Digite uma frase: ')).upper().strip()
print(f'A letra A apareceu {frase.count('A')} vezes na frase')
print(f'A primeira letra A apareceu na posição {frase.find('A')}')
print(f'A ultima vez que a letra A aparece é na posição {frase.rfind('A')}')