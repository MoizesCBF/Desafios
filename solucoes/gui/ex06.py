from tkinter import *
from tkinter.messagebox import *

#  ______________Funções______________
def sair():
    resposta = askyesno('Encerrar app',
            'Certeza que quer sair?')
    if resposta:
        root.destroy()
        exit()
    else:
        pass

def criaMenu(pai, rotulo):
    novoMenu = Menu(pai)
    pai.add_cascade(label=rotulo, menu=novoMenu)
    return novoMenu
#  ________________________Fim funções

root = Tk()

'Cria menu principal'
principal = Menu(root)
root.configure(menu=principal)

'Cria menu Arquivo, Formatar e Crédito em principal'
arquivo  = criaMenu(principal, 'Arquivo')
formatar = criaMenu(principal, 'Formatar')
credito  = criaMenu(principal, 'Crédito')

'Cria submenus em Arquivo'
arquivo.add_command(label='Abrir')
arquivo.add_command(label='Salvar')
arquivo.add_command(label='sair', command=sair)

'Cria submenus em Formatar'
edit_fonte = criaMenu(formatar, 'Fonte')  #  cria submenu em submenu
edit_pagina = criaMenu(formatar, 'Página')#  cria submenu em submenu

'Cria submenus em Crédito'
credito.add_command(label='Harry')


root.geometry('300x300')
root.title('Proposta 6 | by Harry')
root.mainloop()