#Aula 17: #
'''galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])  #[:] cria uma cópia
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} de maiores e {totmen} de menores')
print(galera)'''


#84: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas. B) Uma listagem com as pessoas mais pesadas. C) Uma listagem com as pessoas mais leves.
'''princ = list()
temp = list()
pesadas = list()
leves = list()
gordo = magro = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        gordo = magro = temp[1]
    else:
        if temp[1] > gordo:
            gordo = temp[1]
            temp.append(pesadas)
        if temp[1] < magro:
            magro = temp[1]
            temp.append(leves)
    princ.append(temp[:])
    temp.clear()
    resp = input('Quer continuar? [S/N]: ')
    if resp in 'Nn':
        break
print('=-' * 30)
print(f'Foram cadastradas {len(princ)} pessoas')
print(f'O maior peso foi de {gordo}Kg. Peso de ', end='')
for p in princ:
    if p[1] == gordo:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {magro}Kg. peso de ', end='')
for p in princ:
    if p[1] == magro:
        print(f'[{p[0]}] ', end='')
print()'''



#85: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.#
'''lista = [[],[]]
for n in range(1, 8):
    num = int(input(f'Digite o {n}º valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print('=-'*30)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram {lista[0]}')
print(f'Os valores impares digitados foram {lista[1]}')'''


#86: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.#
'''matriz = [[0, 0, 0],[0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l] [c] = int(input(f'Digite um valorpara[{l}, {c}]: '))

print('=-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l] [c]:^5}]', end='')
    print()'''


#87: Aprimore o desafio anterior, mostrando no final: A) A soma de todos os valores pares digitados. B) A soma dos valores da terceira coluna. C) O maior valor da segunda linha.#
'''matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #linha um ao lado do outro, coluna um abaixo do outro
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l] [c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=-'*20)
for l in range(0, 3): #linha
    for c in range(0, 3): #coluna
        print(f'[{matriz[l] [c]:^5}]', end='')
        if matriz[l][c] % 2 == 0: #A soma de todos os valores pares digitados.
            spar += matriz[l] [c]
    print()
print('=-'*20)
print(f'A soma dos valores pares é {spar}.')#A soma de todos os valores pares digitados.
for l in range(0, 3): #B) A soma dos valores da terceira coluna.
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3): #C) O maior valor da segunda linha.
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
            mai = matriz [1][c]
print(f'O maior valor da 2ª linha é {mai}')'''


#88: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.#
'''from random import randint
from time import sleep
print('-'*30)
print('         JOGA NA SENA         ')
print('-'*30)
lista = list()
jogos = list()
cont = 0
quant = int(input('Quantos jogos você quer que eu soteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break

    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SOTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'O jogo {i+1}: {l}')
    sleep(0.7)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)'''



#89: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.#
'''ficha = list()
while True:
    nome = (str(input('Nome: ')))
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break

print('=-' * 30)
print(f'{"Nº.":<4}{"NOME":<8}{"MÉDIA":>8}')
print('-' *20)
for i, a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<8} {a[2]:>8.1f}')

while True:
    print('=-' * 30)
    opc = str(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        print('FINALIZADO')
        break
    if opc <= len(ficha)-1:
        print(f'A notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('=-' * 30)'''

#######ou########
lista = []
listatemp = []
while True:
    listatemp.append(str(input('Nome: ')))
    listatemp.append(float(input('Nota 1: ')))
    listatemp.append(float(input('Nota 2: ')))
    lista.append(listatemp[:])
    listatemp.clear()
    sn = str(input('Quer continuar? [S/N]: ')).upper().strip()

    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if sn == 'N':
        break
print('-='*35)
print(f'{"Nº.":<4}{"NOME":<8}{"MÉDIA":>8}')
print('-'*19)
for i in range(0, len(lista)):
    print(f'{i:<3}', f'{lista[i][0]:<8} ', f'{(lista[i][1] + lista[i][2]) / 2:.1f}')
while True:
    print('-' * 35)
    m = int(input('Quer ver nota de que aluno? [999 para parar]: '))
    if m == 999:
        print('Finalizando...')
        break
    if m <= len(lista)-1:
        print(f'As notas de {lista[m][0]} são {lista[m][1]} e {lista[m][2]}')
print('Programa finalizado, volte sempre')