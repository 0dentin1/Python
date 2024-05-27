n = str(input('Digite seu nome completo: ')).strip()#strip() é usado para eliminar espaços desnecessarios
nome = n.split()#dividi frase em pedaçoex: Nicolas Ritter Lima, usando split() ira ficar 'Nicolas' 'Ritter' 'Lima'
print(f'Muito prazer em te conhecer {n}!')
print(f'Seu primeiro nome é {nome[0]}')
print(f'Seu ulimo nome é {nome[len(nome)-1]}')