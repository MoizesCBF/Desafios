
# Programa que lê um arquivo e mostra na
# tela o seu conteúdo.
# OBS: O arquivo deve se envontrar na pasta
# raiz do programa.

nome = input('Digite o nome do arquivo: ')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))

texto = 'Conteudo entre linhas {} e {}:'
print(texto.format(inicio, fim))

arquivo = open(nome + '.txt', 'r')
conteudo = arquivo.readlines()

for linha in range(inicio-1, fim, 1):
    print(conteudo[linha])

arquivo.close()
