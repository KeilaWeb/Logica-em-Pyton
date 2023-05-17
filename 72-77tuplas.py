#72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input('Digite um número de 0 a 20: '))
    if 0 <= num <= 20:
        break
    print('Este não, tente novamente. \n', end='')

print(f'Você digitou o número {cont[num]}')'''


#73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time da Chapecoense.
'''times = ('Fluminense', 'Bragantino', 'Flamengo', 'Botafogo', 'Corinthians', 'Palmeiras', 'Vasco', 'Grêmio', 'São Paulo', 'Athletico-PR', 'Fortaleza', 'Internacional', 'Cuiabá', 'Bahia', 'Cruzeiro', 'Atlético-MG', 'Santos', 'Goiás', 'Coritiba', 'América-MG')
print('-='*30)
print(f'Lista de times: \n {times}')
print('-='*30)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-='*30)
print(f'Os 4 últimos são: {times[-4:]}')
print('-='*30)
print(f'Em ordem alfabética: {sorted(times)}')
print('-='*30)
print(f'O Corinthians esta na {times.index("Corinthians")+1}ª posição')
print('-='*30)'''


#74: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.#
'''from random import randint
num = randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10)
print('Os valores sorteados foram: ')
for n in num:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')'''


#75: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.#
'''num = int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: '))
print(f'Você digitou os valores {num}')
print(f'O número 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 esta na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')
print('Os números pares são ', end='')
for n in num:
    if n % 2 ==0:
        print(n, end=' , ')'''


#76: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.#
'''print('='*40)
print(f'{"VERDUREIRA DO CURSO EM VÍDEO":^40}')
print('='*40)
produtos = ('Maçã', 5.99, 'Caqui', 6.99, 'Morango', 19.99, 'Uva', 8.99, 'Abacaxi', 7.99, 'Abacate', 7.99)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print (f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')'''


#77: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.#
palavras = ('mercado', 'computador', 'programador', 'futuro', 'trabalho', 'python', 'linguagem', 'familia','filhos')

for p in palavras:
    print(f'\n\033[39mNa palavra \033[33m{p.upper()}\033[m temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print('\033[3;33m',letra, end='')
print('\n\033[37mEsse foi o jogo das palavras')
