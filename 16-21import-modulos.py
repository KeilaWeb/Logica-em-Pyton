#import math
####num = int(input('Digite um número '))####
'''raiz = math.sqrt(num)
normal- print(' A raiz de  {} é igual a {}'.format(num, (raiz)))
arredonda pra cima- print(' A raiz de  {} é igual a {}'.format(num, math.ceil(raiz)))
arredonda pra baixo- print(' A raiz de  {} é igual a {}'.format(num, math.floor(raiz)))'''
import random

####1) porção inteira de número real####
'''num = float(input("Digite um número quebrado "))
print("Sua porção inteira é {}".format(math.trunc(num)))'''


####2) calcule o comprimento da hipotenusa####
'''ca= float(input('Valor do cateto adjacente: '))
co = float(input('Valor do cateto oposto: '))
hi= (co**2 + ca**2)**(1/2)
print ('O valor da hipotenusa é de {:.2f}'.format(hi))'''

#########ou#########

####import math
'''ca= float(input('Valor do cateto adjacente: '))
co = float(input('Valor do cateto oposto: '))
hi = math.hypot(co, ca)
print ('O valor da hipotenusa é de {:.2f}'.format(hi))'''


####3) calcule o seno, cosseno e tangente####
'''import math
ang= float(input('Digito o ângulo: '))
seno= math.sin(math.radians(ang))
print('O ângulo de {} tem o seno de {:.2f}'.format(ang, seno))
cosseno = math.cos(math.radians(ang))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(ang, cosseno))
tangente = math.tan(math.radians(ang))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ang, tangente))'''


####4) sortear um aluno de uma lista de 4 alunos####
'''from random import choice
aluno1 = input('Digite o nome de um aluno ')
aluno2 = input('Digite o nome de outro aluno ')
aluno3 = input('Digite o nome de mais um aluno ')
aluno4 = input('Digite o nome de mais outro aluno ')
lista = [aluno4, aluno3,aluno2, aluno1]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))'''


####5) leia o nome dos 4 alunos e coloque em ordem####
'''from random import shuffle
aluno1 = input('Digite o nome de um aluno ')
aluno2 = input('Digite o nome de outro aluno ')
aluno3 = input('Digite o nome de mais um aluno ')
aluno4 = input('Digite o nome de mais outro aluno ')
lista = [aluno4, aluno3,aluno2, aluno1]
shuffle(lista)
print('A ordem de apresentação será,',end='')
print(lista)'''


####6) abra um áudio em mp3####
'''import pygame #importando módulo de jogos#
pygame.init() #iniica a biblioteca do paygame#
pygame.mixer.music.load('fino.mp3') #pasta da música a ser tocada#
pygame.mixer.music.play()
pygame.event.wait() #espera o evendo terminar para encerrar o programa#'''