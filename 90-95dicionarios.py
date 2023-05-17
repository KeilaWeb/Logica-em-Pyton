#90: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.#
'''aluno = {}
aluno['nome'] = str(input('nome: '))
aluno['média'] = float(input('média do aluno: '))

if aluno['média'] < 5:
    aluno['situação'] = 'reprovado'
elif aluno['média'] >= 5 and aluno["média"] <= 9:
    aluno['situação'] = 'recuperação'
else:
    aluno['situação'] = 'aprovado'

print('='*60)
if aluno['situação'] == 'recuperação':
    print(f'o aluno {aluno["nome"]} está de {aluno["situação"]} com a média de {aluno["média"]} pontos')
else:
    print(f'o aluno {aluno["nome"]} está {aluno["situação"]} com a média de {aluno["média"]} pontos')'''

#91: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.#
'''from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.8)
ranking = sorted(jogo.items(), key = itemgetter(1), reverse=True)
print('=-' * 30)
print('RANKING DOS JOGADORES')
for i, v in enumerate(ranking):
    print(f'{i+1} lugar: {v[0]} com {v[1]}.')'''


#92: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar#
'''from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados ['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('=-'*30)
for c, i in dados.items():
    print(f'{c}: {i}')'''


#93: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.#
'''jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: ')).title()
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
if partidas != 0:
    for g in range(0, tot):
        partidas.append(int(input(f'  Quantos gols na partida {g}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador["gols"]):
    print(f'    => Na partida {i}, fez {v} gols')
print(f'Foi um total de {jogador["total"]} gols')'''

#94: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média#
'''dados = dict()
lista = list()
somaidade = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: ')).title()
    while True:
        dados['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    dados['idade'] = int(input('Idade: '))
    somaidade += dados['idade']
    lista.append(dados.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('=-'* 30)
print('=-'* 30)
print(f'Foram cadastradas {len(lista)} pessoas.')
print('- -' * 20)
idades = somaidade / len(lista)
print(f'A média de idades é igual a {idades:5.2f}')
print('- -' * 20)
print(f'As mulheres cadastradas foram: ', )
for p in lista:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print('- -' * 20)
print(f'A lista das pessoas que estão acima da média: ', end=' ')
for p in lista:
    if p['idade'] > idades:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v} ', end=' ')
print()
print('=-'* 30)
print('<< ENCERRADO >>')'''


#95: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.#
#93:O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.#
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).title()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    if partidas != 0:
        for c in range(0, tot):
            partidas.append(int(input(f'  Quantos gols na partida {c + 1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print('code ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-='*30)
for k, v in enumerate(time):
    print(f'{k:>3}: ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRo! Não existe jogador com esse código {busca}')
    else:
        print(f' -- LEVANTAMENDO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols. ')
print('-='*30)

