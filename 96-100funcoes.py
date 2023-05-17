#96: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.#
'''def area(larg, compr):
    a = larg * compr
    print(f'{larg} x {compr} = {a}m².')


print('-' * 24)
print('  Controle de Terrenos  ')
print('-' * 24)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)'''


#97: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.  #
'''def escreva(msg):
    linha = len(msg) + 6
    print('~' * linha)
    print(f'   {msg}   ')
    print('~' * linha)

texto = str(input('Escreva um título qualque: '))
escreva(texto)'''


#98: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:  a) de 1 até 10, de 1 em 1 b) de 10 até 0, de 2 em 2  c) uma contagem personalizada#
'''from time import sleep
def contador(i, f, p):
    if f > i:
        f += 1
    elif f < i:
        f -= 1
    print('=' * 30)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(.05)
    if i > f:
        for rev in range(i, f, -p):
            sleep(0.5)
            print(rev, end=' ')
        print()
    else:
        for c in range(i, f, p):
            sleep(0.5)
            print(c, end=' ')
        print()


contador(1, 10, 1)
contador(10, 0, 2)
print('AGORA É SUA VEZ')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
print('=' * 30)
contador(inicio, fim, passo)
print(' >>FIM DO PROGRAMA<< ')
print('=' * 30)'''


#99: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.#
'''from time import sleep
def maior(* núm):
    cont = maior = 0
    print('=-' * 30)
    print()
    print('Analisando os valores passados... ')
    for valor in núm:
        print(f'{valor} ', end='')
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo. ')
    print(f'O maior valor informado foi {maior}. ')
    print()


#Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()'''

#100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.#
from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f' {n} ', end='', flush=True)
        sleep(0.3)
    print(' || PRONTO! ||')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, resulta em: {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)

