#Aula 17
'''valores = [] #ou valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores): #(c= chave | v= valores)
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao valor da lista')'''

### ou ###
'''valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores): #(c= chave | v= valores)
    print(f'Na posição {c} encontrei o valor {v}...')
print('Cheguei ao final da lista')'''

##copiando uma lista###
'''a = [2, 3, 4, 7]
b = a[:]  #criou uma cópia
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')'''

#78: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.#
'''nums = []
maxi = []
mini = []
for c in range(0, 5):
    nums.append(int(input(f'Digite um valor para a posição {c}: ')))
for pos, valores in enumerate(nums):
    if valores == max(nums):
        maxi.append(pos)
    if valores == min(nums):
        mini.append(pos)

print(f'Você digitou {nums}...')
print(f'O maior valor digitado foi {max(nums)}, na posição {maxi}')
print(f' O menor valor digitado foi {min(nums)}, na posição {mini}')'''


#79: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.#
'''listanumerica = list()
while True:
    n = (int(input('Digite um número: ')))
    if n not in listanumerica:
        listanumerica.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado, não vou adicionar!')
    continuar = input('Quer continuar? [S/N]: ').strip() .upper()
    if continuar == 'N':
        break
print('-='*30)
listanumerica.sort()
print(f'Você digitou os valores: {listanumerica}')'''


#80: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.#
'''lista = list()
for c in range(0, 5):
    usuario = int(input(f'Digite o {c}º número: '))
    if c == 0 or usuario > lista[-1]:
        lista.append(usuario)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if usuario <= lista[pos]:
                lista.insert(pos, usuario)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print('=-'*30)
print(f'Os valores digitados em ordem foram {lista}')'''


#81: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente. C) Se o valor 5 foi digitado e está ou não na lista.#
'''lista = list()
n = ''
while True:
    lista.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuas? [S/N]'))
    if resp in 'Nn':
        break
print('=-'*30)
print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'A lista em ordem descrescente é {lista}')
if 5 in lista:
    print('Valor 5 esta na lista')
else:
    print('O valor 5 não esta na lista')'''

#82: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.#
'''lista1 = list()
listapares = list()
listaimpares = list()
while True:
    n = int(input('Digite um valor: '))
    lista1.append(n)
    resp = str(input('Quer continuas? [S/N]: '))
    if resp in 'Nn':
        break
    if n % 2 == 0:
        listapares.append(n)
    else:
        listaimpares.append(n)
print('=-'*30)
print(f'A lista completa de números é {lista1}')
print(f'Os pares da lista são {listapares}')
print(f'Os ímpares da lista são{listaimpares}')'''


#83: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.#
expressao = str(input('Digite uma expressão númerica: '))
pilha = []
for simbolo in expressao:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo ==')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
