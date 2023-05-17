#28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.#
'''from random import randint
from time import sleep
computador = randint (0, 5) #faz o computador pensar
print('\033[1;32m =='*20) #enfeite colorido
print('Vou pensar me um número entre 0 e 5. Tente adivinhar...')
print('\033[1;32m ==\033[m'*20)
jogador = int(input('Em que número estou pensando? ')) #jogador tenta adivinhar
print('PROCESSANDO')
sleep(1)
if jogador == computador:
    print('PARABÉNS, você conseguiu me vencer')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))'''


#29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.#
'''velocidade = float(input('Qual a velocidade do carro? '))
if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança')
else:
    multa = (velocidade - 80) * 7
    print('MULTADO! Sua multa é de R${:.2f}'.format(multa))'''

#30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.#
'''n = int(input('Digite um número: '))
if n % 2 == 0:
    print('O número {}, é par '.format(n))
else:
    print('O número é impar')'''


#31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.#
'''distancia = int(input('Qual a distância da viagem?: '))
if distancia <= 200:
    custo = distancia * 0.50
    print('Sua viagem irá custar R${:.2f}'.format(custo))
else:
    custo = distancia * 0.45
    print('Sua viagem irá custar R${:.2f}'.format(custo))'''


#32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.#
'''from datetime import date
ano = int(input('Qual ano você quer analisar? Coloque 0 para ver o ano atual '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))'''


#33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.#
'''n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
#menor valor
menor = n1 #simulando que n1 é o menor, se não
if n2 < n1 or n2 < n3 :
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#maior valor
maior = n1
if n2 > n1 and n2 > n3 :
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O menor valor é: {}'.format(menor))
print('O maior valor é: {} '.format(maior))'''


#34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.#
'''salario = float(input('O salário atual do funcionário é R$'))
if salario >= 1250:
    aumento = salario + (salario * 10/100)
else:
    aumento = salario + (salario * 15/100)
print('O novo salário do funcionario é R${}'.format(aumento))'''


# 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.#
'''print('\033[2;34m-=\033[m' *20)
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('\033[2;34m-=\033[m' *20)
if r1 < r2 + r3 and r2 < r1 +r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo')'''