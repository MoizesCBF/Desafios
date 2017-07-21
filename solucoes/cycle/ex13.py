#Proposto por @william_klein's#6834

from random import randint

n = int(randint(1, 9))
p = 0
t = 0

while p != n :
    p = int(input('Digite um palpite: '))
    t += 1
    if p > n :
        print('Seu palpite foi muito '
              'alto!')
    elif p < n :
        print('Seu palpite foi muito '
              'baixo!')
    else :
        print('Acertoouuhh !! '
              'Tentativas: {}.'.format(t))
