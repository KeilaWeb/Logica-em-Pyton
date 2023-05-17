#22: Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.
'''nome= str(input('Digite seu nome completo ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))'''

#23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.#

'''num= int(input('Digite um número de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m= num // 1000 % 10
print('Analisando o número {}'.format(num))

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))'''

#24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.#
'''cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')'''

#25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.#
'''nome = str(input('Qual seu nome? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))'''

#26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.#
'''frase = str(input('Digite uma frase ')).upper().strip()
print('Nessa frase a letra A aparece? {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))'''

#27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente#
'''n = str(input('Qual seu nome? ')).strip()
nome = n.split()
print('=='*10)
print('Muito prazer em te conhecer')
print('=='*10)
print('Seu preimeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))'''


#53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:#
frase = str(input('Digite uma frase: ')).strip() .upper()
palavras = frase.split()
tudojunto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(tudojunto, inverso))
if tudojunto == inverso:
    print('É Palíndromo')
else:
    print('Não é Palíndromo')