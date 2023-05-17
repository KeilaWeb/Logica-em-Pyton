#O fatorial de um número é a multiplicação desse número por todos os seus antecessores até chegar a 1. Por exemplo, o fatorial de 5 é 5*4*3*2*1 que é igual a 120. De forma geral:n! = n*(n-1)*(n-2)*(n-3)...*1#

'''def fatorial(n):
    if n == 0:
       return 1
    else:
       return n * fatorial(n - 1)

n = int(input('Digite um número até 10: '))
x = n-1
print(fatorial(n))'''


#O termial de um número é a soma desse número por todos os seus antecessores até chegar a 1. Por exemplo, o termial de 5 é 5+4+3+2+1 que é igual a 15. De forma geral: n? = n +(n-1)+(n-2)+(n-3)...+1#

'''def terminal(n):
    if n == 1:
        return 1
    else:
        return n + terminal(n - 1)

n = int(input('Digite um número: '))
x = n-1
print(terminal(n))'''


#Construa uma função em python que dado um número ela retorne a tabuada desse número. Novamente aqui permita que o usuário escolha qual tabuada deseja saber e só interrompa quando ele digitar um número negativo.#
'''def tabuada(n):
    cont = 1
    while cont <= 10:
        result = n * cont
        print('{} x {} = {}'.format(n, cont, result))
        cont = cont +1

n=int(input('Digite o número: '))
tabuada(n)'''


#) Desenvolva uma função que peça como parâmetro os 3 lados de um triângulo. A função deverá devolver se os valores passados como parâmetro de entrada compõem um triângulo equilátero, isósceles ou escaleno. Regras:
#Triângulo Equilátero: três lados iguais;
#Triângulo Isósceles: quaisquer dois lados iguais;
#Triângulo Escaleno: três lados diferentes.#
'''def tri(b1, b2, b3):
    if b1 == b2 and b3 == b1:
        return 'Equilátero'
    elif b1 == b2 or b1 == b3 or b2 == b3:
        return 'Isóceles'
    else:
        return 'Escaleno'


b1 = int(input('Tamanho de um lado: '))
b2 = int(input('Tamanho de outro lado: '))
b3 = int(input('Tamanho de mais um lado: '))
print('{}, {}, {} Refere-se a um triângulo {}'.format(b1, b2, b3, tri(b1, b2, b3)))'''


#Implemente uma função que dado como parâmetro o valor de um saque no caixa eletrônico (terminal ATM) ela retorne quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50, 100 e 200 reais. ##
def nota(saque):
    if saque <= 0 or saque > 10000:
        print("Valor inválido para saque.")
        return

    nota200 = saque // 200
    nota100= (saque % 200) // 100
    nota50= (saque % 100) // 50
    nota10= ((saque % 100) % 50) // 10
    nota5= ((saque % 100) % 50 % 10) // 5
    nota1= ((saque % 100) % 50 % 10 % 5) // 1
    print('{} notas de R$200,00 \n{} notas de R$100,00 \n{} notas de R$50,00 \n{} notas de R$10,00 \n{} notas de R$5,00 \n{} notas de R$1,00'.format(nota200, nota100, nota50, nota10, nota5, nota1))


saque = int(input('Qual valor a ser retirado? R$'))
nota(saque)
#print('nota200= ', nota200, '\nnota100 =', nota100, '\nnota50= ',nota50, '\nnota10= ', nota10, '\nnota5= ', nota5, '\nnota1= ', nota1)
