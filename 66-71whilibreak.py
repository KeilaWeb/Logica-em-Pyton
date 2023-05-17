#66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).#
'''cont = soma = 0
while True:
    n = int(input('Digite um número [para parar digite 999]: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'Você digitou {cont} números e a soma desses números foi {soma}')'''


#67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.#
'''while True:
    cont = 0
    num = int(input('Tabuada de qual número: '))
    if num < 0:
        break
    while cont < 10:
        cont += 1
        mult = num * cont
        print(f'{num} x {cont} = {mult}')'''

####Guanabara####
'''while True:
    num = int(input('Tabuada de qual número: '))
    if num < 0:
        break
    print('-' * 30)
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADA. Volte sempre!')'''


#68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de derrotas consecutivas que ele conquistou no final do jogo.#
'''from random import randint
from time import sleep
v = 0
while True:
    print('-'*30)
    jogador = str(input('Par ou impar? '))
    if jogador != 'par' and jogador != 'impar':
        print('Comando errado tente novamente')
    else:
        print('\033[34m1')
        sleep(0.3)
        print('2')
        sleep(0.3)
        print('3')
        sleep(0.3)
        print('Coloca já \033[m')
        num = int(input('\033[32mQual número você escolhe? \033[m'))
        computador = randint(0, 11)
        soma = num + computador
        print(f'Você escolheu {num}, e o computador escolheu {computador} = {soma}')
        if soma % 2 == 0:
            print('\033[33mDeu par\033[m')
        else:
            print('\033[33mDeu impar\033[m')
        if soma % 2 == 0 and jogador == 'par':
            print('Você ganhou! PARABÉNS')
            break
        else:
            print('O computador ganhou, tente novamente')
            v += 1
        print('-' * 30)

print(f'\033[32mVocê perdeu {v} vezes\033[m')'''


#69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.#
'''maior = masc = mmenor = 0
while True:
    print('-'*20)
    print('CADASTRE-SE')
    print('-' * 20)
    idade = int(input('Qual sua idade? '))
    sexo = str(input('Qual seu sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo: [F/M]: ')).upper().strip()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        masc += 1
    if sexo == 'F' and idade < 20:
        mmenor += 1
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continuar != 'S' and continuar != 'N':
        print('Opção inválidade! Tente Novamente')
    if continuar == 'N':
        break
print(f'OK!! Temos aqui: {maior} pessoas maiores de 18 anos, {masc} homens e {mmenor} mulheres menores de 20 anos')'''



#70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre: A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.#
'''total = totmil = menor = cont = 0
barato = ''
while True:
    nomeproduto = input('Nome do produto: ')
    preco = float(input('Qual o valor do produto? R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nomeproduto
    resp = ' '
    while resp not in 'SN':
        resp = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if resp == 'N':
        break

print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000,00')
print(f'O produto com o menor preço foi o(a) {barato} que custou R${menor:.2f}')
print('{:-^40}'.format('FIM DO PROGRAMA'))'''



#71: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.#

'''saque = int(input('Qual o valor a sacar? R$ '))
total = saque #pega o valor inteiro para ir tirando notas, começando pela maior até a menor
cedulas = 50 #começa com a de maior valor(pedido no programa)
totced = 0 #total de cada cédula
while True: #um loop infinito de calculo que sera quebrado quando acabar o valor
    if total >= cedulas: #tira 50 quantas vezes forem necessárias
        total -= cedulas #tirando 50 do valor total
        totced += 1
    else:
        if totced > 0: #ele só escreve se o total de cedulas for maior que 0
            print(f'Total de {totced} cédulas de R${cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        totced = 0 #cada vez que muda a nota o total de cédula volta ao 0
        if total == 0:
            break
print('\033[33m=' * 50)
print('Volte sempre ao Banco CURSO EM VÍDEO! Tenha um bom dia!')
print('=' * 50)'''

###ou###
valor = int(input("informe o valor a ser sacado : "))
nota50 = valor // 50
valor %=  50
nota20 = valor // 20
valor %= 20
nota10 = valor // 10
valor %= 10
nota1 = valor // 1
print(f"notas de 50 = {nota50}")
print(f"notas de 20 = {nota20}")
print(f"notas de 10 = {nota10}")
print(f"notas de 1 = {nota1}")

####ou####
'''print('\033[33m-=-'*21)
print('-=-'*8+'\033[34m   Banco CEV   '+'\033[33m-=-\033[m'*8)
print('\033[33m-=-\033[m'*21)
n = int(input('\033[36mQue valor você quer sacar? R$').strip())
c50 = n//50
c20 = (n % 50)//20
c10 = ((n % 50) % 20)//10
c5 = (((n % 50) % 20) % 10)//5
c = (((n % 50) % 20) % 10) % 5
if c50 != 0:
    print(f'\033[31mTotal de {c50} cédulas de R$50')
if c20 != 0:
    print(f'\033[31mTotal de {c20} cédulas de R$20')
if c10 != 0:
    print(f'\033[31mTotal de {c10} cédulas de R$10')
if c5 != 0:
    print(f'\033[31mTotal de {c5} cédulas de R$5')
if c != 0:
    print(f'\033[31mTotal de {c} cédulas de R$1')
print('\033[33m-=-\033[m'*21)
print('\033[35mVolte sempre ao BANCO CEV! Tenha um bom dia!')'''