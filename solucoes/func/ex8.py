# Solução enviada por @Like_a_NachozBR#5267

from math import floor

def is_square(x):
    x = str(x**0.5)
    return x[len(x)-2:]=='.0'


while True:
    n = int(input())
    if n==0:
        break
    s = ''
    f = floor(n**0.5)
    for i in range(1,f+1):
        s+=str(i**2)+' '
    print(s[:len(s)-1])
