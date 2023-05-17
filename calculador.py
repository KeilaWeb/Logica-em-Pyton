import math
print('\033[1;34m-=\033[m'*12)
opcao= print('''\033[2;33mOperações: 
[ 1 ] Adição
[ 2 ] Subtração 
[ 3 ] Multiplicação
[ 4 ] Divisão
[ 5 ] Raiz Quadrada 
[ 6 ] Potenciação
[ 7 ] Conversão de bases 
[ 0 ] Sair \033[m''')
print('\033[1;34m-=\033[m'*12)
user = int(input('Qual operação você escolhe? '))

if user == 1:
    print("Adição:")
    adicao = 0
    n=float(input('Digite o número: '))
    while n!=0:
        adicao=adicao + n
        print(adicao)
        n=float(input('+'))
elif user == 2:
    print("Subtração:")
    subtrai = int(input('Digite o número: '))
    n = subtrai
    n=float(input('- '))
    while n!=0:
        subtrai = subtrai - n
        print(subtrai)
        n=float(input('- '))
elif user == 3:
    print("Multiplicação:")
    multi = 1
    n=float(input('Digite o número: '))
    while n!=0:
        multi = multi * n
        print(multi)
        n=float(input('x '))
elif user == 4:
    print("Divisão:")
    divisa = int(input('Digite o número: '))
    n = divisa
    n=float(input('/ '))
    while n!=0:
        divisa = divisa / n
        print(divisa)
        n=float(input('/ '))
elif user == 5:
    print("Raiz Quadrada:")
    n=float(input('Digite o número: '))
    if n < 0:
        print('Erro: tente novamente!!')
    else:
        print('Raiz de {:.2f} é'.format(math.sqrt(n)))
elif user == 6:
    print("Potenciação:")
    base = float(input('Digite a base: '))
    expoente = float(input('Digite o expoente: '))
    n = base ** expoente
    print('{} sobre {} = {}'.format(base, expoente, n))
elif user == 7:
    print('Conversão de bases')
    num = int(input('Digite um número decimal: '))
    print(num, 'BINÁRIO: ',bin(num)[2:])
    print(num, 'HEXADECIMAL: ', hex(num)[2:])
    print(num, 'OCTAL: ', oct(num)[2:])
elif user == 0:
    print('Obrigada por usar a calculadora!!')
else:
    print('Opção inválida')