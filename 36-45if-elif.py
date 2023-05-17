'''36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''

'''casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / anos / 12
mínimo = salario * 30/100
#print(prestação, excede)
if prestação > mínimo:
    print('Com um salário de R${:.2f}, para um empréstimo de R${:.2f}, a parcela excede os 30% do seu salário, pois a parcela ficaria em R${:.2f} ao mês. NÃO CONCEDIDO'.format(salario, casa, prestação))
else:
    print('Com um salário de R${:.2f}, para um empréstimo de R${:.2f}, a parcela ficará em R${:.2f} ao mês. EMPRÉSTIMO CONCEDIDO '.format(salario, casa, prestação))'''


#37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.#
#num = int(input('Digite um número: '))
#print('''Escolha uma das bases para conversão:
#[ 1 ] converter para BINÁRIO
#[ 2 ] converter para OCTAL
#[ 3 ] para converter HEXADECIMAL''')

'''opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente')'''


#38: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem: O primeiro valor é maior, O segundo valor é maior, Não existe valor maior, os dois são iguais#

'''n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('Entre {} e {}, o PRIMEIRO valor é MAIOR'.format(n1, n2))
elif n2 > n1:
    print('Entre {} e {}, o SEGUNDO valor é MAIOR'.format(n1, n2))
else:
    print('OS DOIS VALORES SÃO IGUAIS')'''


#39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.#

'''from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('Quem nasceu em {}, tem {} anos em {}'.format(nasc, idade, atual))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Você AINDA NÃO tem 18 anos, faltam {} anos para o alistamento'.format(saldo))
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Você JÁ DEVERIA ter se alistado há {} anos'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))'''

#40: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida: >Média abaixo de 5.0: REPROVADO< > Média entre 5.0 e 6.9: RECUPERAÇÃO >< Média 7.0 ou superior: APROVADO >#

'''nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota2 + nota1) /2
if media < 5.0:
    print('REPROVADO')
elif media >= 5.0 and media < 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')'''


#41: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:#
'''Até 9 anos: MIRIM  – Até 14 anos: INFANTIL  – Até 19 anos: JÚNIOR  – Até 25 anos: SÊNIOR  – Acima de 25 anos: MASTER'''

'''from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
print('Você tem {} anos'.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade > 9 and idade <= 14:
    print('INFANTIL')
elif idade > 14 and idade <= 19:
    print('JÚNIOR')
elif idade > 19 and idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')'''


#42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:#
'''– EQUILÁTERO: todos os lados iguais – ISÓSCELES: dois lados iguais, um diferente – ESCALENO: todos os lados diferentes#'''

'''print('\033[2;34m-=\033[m' *20)
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('\033[2;34m-=\033[m' *20)

if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo! ', end='')
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO')
    elif r1 == r2 and r2 != r3 and r3 != r1:
        print('ISÓSCELLES')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo')'''


#43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
''' – IMC abaixo de 18,5: Abaixo do Peso  – Entre 18,5 e 25: Peso Ideal  – 25 até 30: Sobrepeso  – 30 até 40: Obesidade  – Acima de 40: Obesidade Mórbida#'''

'''peso = float(input('Quanto você pesa? (Kg) '))
altura = float(input('Qual sua altura? (m) '))
imc = peso / altura**2
print('\033[1;32mSeu IMC é {:.1f} e você está \033[m'.format(imc), end='')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc < 25:
    print('com o peso IDEAL')
elif imc < 30:
    print('no SOBREPESO')
elif imc < 40:
    print('OBESO')
else:
    print('com OBESIDADE MÓRBIDA')'''


#44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
''' – à vista dinheiro/cheque: 10% de desconto  – à vista no cartão: 5% de desconto  – em até 2x no cartão: preço formal   – 3x ou mais no cartão: 20% de juros'''

#valor = float(input('Valor da compra: R$'))
#print('''\033[1;32mFORMAS DE PAGAMENTO
#[ 1 ] à vista dinheiro/cheque,
#[ 2 ] à vista cartão,
#[ 3 ] 2x no cartão,
#[ 4 ] 3x ou mais no cartão: \033[m''')
'''opção = int(input('Qual é a opção? '))
if opção == 1:
    total = valor - (valor * 10/100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor,total))
elif opção == 2:
    total = valor - (valor * 5/100)
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(valor, total))
elif opção == 3:
    total= valor / 2
    print('Sua compra vai custar 2x de R${:.2f}'.format(total))
elif opção == 4:
    parcela = int(input('Quantas parcelas? '))
    total = valor + (valor * 20/100)
    parcelado = total / parcela
    print('Sua compra de R${:.2f} parcelada em {:.2f}x, de R${:.2f} com juros, \nTotal da compra R${:.2f}'.format(valor, parcela, parcelado, total))
else:
    print('Opção inválida de pagamento, tente novamente')'''


#45: Crie um programa que faça o computador jogar Jokenpô com você.#
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''\033[2;31mSuas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA\033[m''')
jogador = int(input('\033[2;34mQual é sua opção? '))
print('\033[2;31mJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)
print('\033[1;33m-=\033[m'*12)
print('Computador jogou \033[2;31m{} \033[m'.format(itens[computador]))
print('Jogador jogou \033[2;34m{}\033[m'.format(itens[jogador]))
print('\033[1;33m-=\033[m'*12)
if computador == 0: #PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR GANHA')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1:#PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR GANHA')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2: #TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA!')


