# 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.#
'''sexo = str(input('Digite seu sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))'''


#58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.#
'''from random import randint
print('-=' *46)
print('\033[4;33m-= Sou o seu comp´putador... Acabei de pensar em um número entre 0 e 10 -=')
print('-=-=-=-=-=-=-=- Será que você consegue adivinhar qual foi? -=-=-=-=-=-=-=-\033[m')
computador = randint(0, 10)
jogador = int(input('\nQual seu palpite?'))
palpites = 1
while jogador != computador:
    palpite = int(input('Você errou tente novamento: '))
    palpites += 1
    if palpite > 10:
        print('Número inválido tente novamente: ')
    if palpite < computador:
        print('Pensei em um número maior')
    elif palpite > computador:
        print('Pensei em um número menor')
    else:
        print('Acertou miserávis')
        break
print(palpites)'''

###GUANABARA###
'''from random import randint
computador = randint(0, 10)
print('-=' *46)
print('\033[4;33m-= Sou o seu comp´putador... Acabei de pensar em um número entre 0 e 10 -=')
print('-=-=-=-=-=-=-=- Será que você consegue adivinhar qual foi? -=-=-=-=-=-=-=-\033[m')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('\nQual é seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Pensei em um número maior')
        elif palpite > computador:
            print('Pensei em um número menor')
print('\033[34mAcertou com {} tentativas.'.format(palpite))'''


#59: Crie um programa que leia dois valores e mostre um menu na tela: [ 1 ] somar  [ 2 ] multiplicar  [ 3 ] maior  [ 4 ] novos números  [ 5 ] sair do programa  Seu programa deverá realizar a operação solicitada em cada caso.#
'''from time import sleep
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número: '))
opção = 0
while opção != 5:
    print('''#\033[31m    [ 1 ] somar
    #[ 2 ] multiplicar
    #[ 3 ] maior
    #[ 4 ] novos números
    #[ 5 ] sair do programa\033[m''')
'''    opção = str(input('\033[35m>>>>Qual sua opção?\033[m '))
    if opção == '1':
        print('Somando...')
        sleep(0.3)
        soma = n1 + n2
        print('{} + {} = {}'.format(n1, n2, soma))
    elif opção == '2':
        print('Multiplicando...')
        sleep(0.3)
        multi = n1 * n2
        print('{} x {} = {}'.format(n1, n2, multi))
    elif opção =='3':
        print('Verificando...')
        sleep(0.3)
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {}, o maior é {}'.format(n1, n2, maior))
    elif opção == '4':
        print('Informe outros número')
        sleep(0.3)
        n1 = int(input('Digite outro número: '))
        n2 = int(input('Digite mais um número: '))
    elif opção =='5':
        print('Finalizando')
        sleep(0.3)
        print('Até mais pequeno gafonhoto!!!!')
        break
    else:
        print('opção inválida')'''


#60: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
'''n = int(input('Digite um número: '))
c = n
f = 1
print('\033[34mCalculando {}! = \033[m'.format(n),end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))'''


#61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.#
'''print('\033[33m==' * 30)
print('GERADOR DE PA')
print('==' * 30)
##começa o código##
primeiro = int(input('\033[mDigite qual o termo: ')) ##por onde começa##
razao = int(input('Digite a razão: ')) ##como será a contagem(de quanto em
termo = primeiro
cont = 1
while cont <= 10:
    print('{} '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')'''


#62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.#
'''print('\033[33m==' * 30)
print('GERADOR DE PA')
print('==' * 30)
##começa o código##
primeiro = int(input('\033[mDigite qual o termo: ')) ##por onde começa##
razao = int(input('Digite a razão: ')) ##como será a contagem(de quanto em
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')'''


#63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8#
'''print('\033[34m==' * 30)
print('Sequência de Fibonacci')
print('==' * 30)
n = int(input('\033[mQuantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*50)
print('{} - {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' - FIM')
print('~'*50)'''


#64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).#
'''num = cont = soma = 0
num = int(input('Digite um número [999 para parar]:'))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 para parar]:'))
#print('A soma entre os {} é igual a {}'.format(cont-1, soma-999))
print('A soma entre os {} é igual a {}'.format(cont, soma))
print('FIM')'''


#65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
num = quant = soma= 0
maior = menor = media = 0
resp = 'S'
while resp in 'Ss':
    num = int(input('Digite um número:'))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]

media = soma / quant
menor = menor
maior = maior
print('Você digitou {} números e a média foi {:.2f}'.format(quant, media))

print('O maior valor foi {}, e o menor foi {}'.format(maior, menor))
print('FIM')