
# Programa que lê um arquivo e mostra na
# tela o seu conteúdo.
# OBS: O arquivo deve se envontrar na pasta
# raiz do programa.

nome = input('Digite o nome do arquivo: ')
arquivo = open(nome + '.txt', 'r')

for linha in arquivo.readlines():
    print(linha)

arquivo.close()
