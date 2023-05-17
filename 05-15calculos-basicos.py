#1.sucessor e antecessor#
#num=int(input('Digite um número '))
#print('Seu sucessor é {}, e seu antecessor é {}'.format((num+1),(num-1)))

#calcule as notas do aluno#
#nota1=float(input('Nota do primeiro semestre '))
#nota2=float(input('A nota do segundo semestre é '))
#media= (nota1+nota2) /2
#print('A média entre {:.1f} e {:.f} é igual a {:.1f}'.format(n1, n2, media))

#Dobro, triplo e raiz quadrada #
#n=int(input('Digite um numero: '))
#print('você digitou {}, e o dobro disso é {}, o triplo é {}, e a raiz quadrada é {:.3f}'.format(n, n*2, n*3, n**(1/2) ))
#OU print('você digitou {}, e o dobro disso é {}, o triplo é {}, e a raiz quadrada é {:.3f}'.format(n, n*2, n*3, pow(n, (1/2) ))

#cm e mm #
#n=float(input('Distância em metros: '))
#print('Seu número convertido em centímettros é {}cm e em milímetros é {}mm'.format((n*100), (n*1000)))

#real para dolar#
#real=float(input('Quanto dinheiro você tem na carteira? R$'))
#dolar=real / 3.27
#print('Com R$ {:.2f}, você pode comprar USS{:.2f} '.format(real, dolar))

#tabuada #
'''num=int(input("Digite um número que lhe mostro a tabuada dele: "))
tabu=1
result=num
while tabu<=10:
    print(num, "x", tabu, "=",result)
    tabu=tabu+1
    result= num*tabu
print("PARABÉNS")'''

#Latas de tinta #
'''alt=float(input('Qual a altura do ambiente? '))
larg=float(input('Qual a largura? '))
mquadra=alt*larg
print('Altura {} x Largura {} é {}m². Você precisará de {} galões de tinta'.format(alt, larg, mquadra, (int(mquadra//2))))'''

#5% de desconto#
#valor=float(input('Quanto custa isto? R$ '))
#desc=5/100
#print('Isto custa R${:.2f}, mas a vista custa R${:.2f}'.format(valor, (valor - (desc * valor) )))

#15% de aumento no salario#
'''salario=float(input('Você recebe R$ '))
aumento=15/100
print('Passará a receber R${:.2f}'.format(salario + (aumento * salario) ))'''


#Convveersão de Celsius para F#
'''c=float(input('Informe a temperatura em ºC: '))
f=9*c/5+32
print('A temperraturaa de {}ºC corresponde a {}ºF!'.format(c, f))'''

#Valor a pagar pelo aluguel do carro#
'''dias= int(input('Quantos dias ele foi alugado? '))
km=float(input('Quantos Km o carro percorreu? '))
pago= (dias*60) + (km*0.15)
print('Percorrido {}km, por {} dias, o valor a se pagar é R${:.2f}'.format(km, dias, pago))'''