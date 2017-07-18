
#  Considere o ano atual = 2017

while True:
    print()  # pula 1 linha
    nome = input('Nome: ')
    ano = int(input('Ano de nascimento: '))

    if (2017 - ano) < 18:
        print()  # pula 1 linha
        texto = '{} ainda n pode dirigir.'
        print(texto.format(nome))
    else:
        print()  # pula 1 linha
        texto = '{}, você já pode dirigir.'
        print(texto.format(nome))
