#46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.#
'''from time import sleep
for c in range(10, 0, -1):
        print(c)
        sleep(0.5)
print('BUM! BUM! POWW!!!')'''


#47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.#
'''for n in range(1, 51, 2):
    print(n, end=' ')
print('\nxxxFIMxxx')'''


#48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.#
'''soma = 0
cont = 0
for s in range (1, 501, 2):
    if s % 3 == 0:
        cont += 1
        soma += s
print(' A soma de todos os {} valores é {}'.format(cont, soma))'''


# 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.#
'''n = int(input('Tabuada de qual número? '))
mult = 0
for tab in (n, mult):
    while mult < 10:
        tabuada = n * mult
        mult += 1
        print('{} x {} = {}'.format(n, mult, tabuada))'''

### ou ###
'''n = int(input('Tabuada de qual número? '))
for tab in range(1, 11):
    print('{} x {} = {}'.format(n, tab, n*tab))'''


#50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.##
'''soma = 0
cont = 0
for n in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(n)))
    if num % 2 == 0 and num != 0:
        soma += num
        cont += 1
print('Você informou {} números pares, e a soma foi {}'.format(cont, soma))'''


#51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA(progressão aritmética). No final, mostre os 10 primeiros termos dessa progressão.#
'''print('\033[33m==' * 30)
print('10 TERMOS DE UMA RAZÃO')
print('==' * 30)
##começa o código##
termo = int(input('\033[mDigite qual o termo: ')) ##por onde começa##
razao = int(input('Digite a razão: ')) ##como será a contagem(de quanto em quanto quero pular##
decimo = termo + (10 - 1) * razao ## 
for t in range(termo, decimo + razao, razao):
    print(t, end=' ')
print('\033[33m-ACABOU-')'''


#52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.#
## número primo só é divisível por ele mesmo, tipo 5 só é divisível por 5 ##
'''n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[30m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível  {} vezes'.format(n, tot))
if tot == 2:
    print('\033[32mELE É PRIMO')
else:
    print('\033[31mNÃO É PRIMO')'''


#53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:#
'''frase = str(input('Digite uma frase: ')).strip() .upper()
palavras = frase.split()
tudojunto = ''.join(palavras)
inverso = ''
for letra in range(len(tudojunto) -1, -1, -1):
    inverso += tudojunto[letra]  #aqui escreve o inverso da frase
print('O inverso de {} é {}'.format(tudojunto, inverso))
if tudojunto == inverso:
    print('É Palíndromo')
else:
    print('Não é Palíndromo')'''


#54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.#
'''from datetime import date
ano = date.today().year
totmaior = 0
totmenor = 0
for i in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu: '.format(i)))
    idade = ano - nasc
    if idade < 21:
        totmenor+= 1
    else:
        totmaior+= 1
print('Tivemos {} pessoas \033[32mmenores de idade\033[m'.format(totmenor))
print('Tivemos {} pessoas \033[33mmaiores de idade\033[m'.format(totmaior))'''


# 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.#
'''maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Qual o peso da {}ª pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('maior peso {}'.format(maior))
print('menor peso {}'.format(menor))'''


#56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.#
somaidade = 0
media = 0
maioridadehomem = 0
nomevelho = ''
mulheridade = 0
qtdmulher20 = 0
for p in range(1, 5):
    print('===== {}ª PESSOA ====='.format(p))
    nome = str(input('Nome: '.strip() ))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: '.strip() ))
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        qtdmulher20 += 1

media = somaidade / 4
print('A média de idade entre as pessoas é {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}.' .format(maioridadehomem, nomevelho))
print('Quantidade de mulheres com menos de 20 anos é {}'.format(qtdmulher20))

