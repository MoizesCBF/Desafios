
str1 = input('String 1: ')
str2 = input('String 2: ')

if str2 not in str1:
    txt = '{} não contém {}.'
    print(txt.format(str1, str2))

else:
    texto = '{} contém {}.'
    t = '{} econtrado na posição {}.'
    print(texto.format(str1, str2))
    print(t.format(str2, str1.index(str2)))
