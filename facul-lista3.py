'''
sem1 = float(input('Nota do primeiro semestre? '))
sem2 = float(input('Nota do segundo semestre? '))
media = (sem1+sem2)/2

if media >= 9:
    print('A nota do primeiro semestre é {}, e do segundo é {}, sua média então é {}, que equivale a A, e ele esta APROVADO '.format(sem1, sem2, media))
elif media >=7.5 and media <= 8.9:
    print('A nota do primeiro semestre é {}, e do segundo é {}, sua média então é {}, que equivale a B, e ele esta APROVADO '.format(sem1, sem2, media))
elif media >=6.0 and media <= 7.4:
    print('A nota do primeiro semestre é {}, e do segundo é {}, sua média então é {}, que equivale a C, e ele esta APROVADO '.format(sem1, sem2, media))
elif media >=4.0 and media <= 5.9:
    print('A nota do primeiro semestre é {}, e do segundo é {}, sua média então é {}, que equivale a D, e ele esta REPROVADO '.format(sem1, sem2, media))
elif media > 0 and media <= 3.9:
    print('A nota do primeiro semestre é {}, e do segundo é {}, sua média então é {}, que equivale a E, e ele esta REPROVADO '.format(sem1, sem2, media))
'''
while True:
    num = int(input('Digite um número menor de 1000: '))
    if num < 0:
        break

    cem = num // 100
    dez = num % 100 // 10
    uni = num % 10 // 1

    if cem == 1:
        centena = 'centena'
    else:
        centena = 'centenas'

    if dez == 1:
        dezena = 'dezena'
    else:
        dezena = 'dezenas'

    if uni == 1:
        unidade = 'unidade'
    else:
        unidade = 'unidades'

    if cem != 0 and dez != 0 and uni != 0:
        print(f'{num} = {cem} {centena}, {dez} {dezena} e {uni} {unidade}')
    elif cem != 0 and dez != 0 and uni == 0:
        print(f'{num} = {cem} {centena}, {dez} {dezena}')
    elif cem != 0 and dez == 0 and uni != 0:
        print(f'{num} = {cem} {centena} e {uni} {unidade}')
    elif cem != 0 and dez == 0 and uni == 0:
        print(f'{num} = {cem} {centena}')
    elif cem == 0 and dez != 0 and uni != 0:
        print(f'{num} = {dez} {dezena} e {uni} {unidade}')
    elif cem == 0 and dez != 0 and uni == 0:
        print(f'{num} = {dez} {dezena}')
    elif cem == 0 and dez == 0 and uni != 0:
        print(f'{num} = {uni} {unidade}')
    else:
        print(f'{num} = 0 unidades')'''



from math import floor

valor = int(input('Qual valor você quer retirar? R$'))

notas100 = valor // 100
valor = valor % 100

notas50 = valor // 50
valor = valor % 50

notas10 = valor // 10
valor = valor % 10

notas5 = valor // 5
valor = valor % 5

notas1 = valor // 1

print(f"notas de R$100 = {notas100}")
print(f"notas de R$50 = {notas50}")
print(f"notas de R$10 = {notas10}")
print(f"notas de R$5 = {notas5}")
print(f"notas de R$1 = {notas1}")

'''from math import floor
valor= int(input('Qual valor você quer retirar? R$'))
cem= valor//100
cinq= (valor % 100) // 50
dez= ((valor % 100) % 50) // 10
cin= ((valor % 100) % 50 % 10) // 5
uni= ((valor % 100) % 50 % 10 % 5) //1

print(f"notas de R$100 = {floor(cem)}")
print(f"notas de R$50 = {floor(cinq)}")
print(f"notas de R$10 = {floor(dez)}")
print(f"notas de R$5 = {floor(cin)}")
print(f"notas de R$1 = {floor(uni)}")'''


'''while True:
    tab= int(input('Qual o valor de tabuada você quer que eu calcule? '))
    if tab < 0 or tab >10:
        break
    x = 1
    while x <= 10:
        total = tab * x
        print(f'{tab} X {x} = {total}')
        x+= 1'''
