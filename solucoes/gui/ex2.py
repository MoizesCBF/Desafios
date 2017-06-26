from tkinter import *
from tkinter.messagebox import *

#  _________________Funções________________
def calcular():
    '''recebe ano, calcula idade e exibe no 
                                 monitor'''
    try:
        ano_nascimento = int(idade_et.get())
        assert len(idade_et.get()) == 4
        assert ano_nascimento <= 2017
    except:
       '''mostra mensagem de erro caso não 
                             seja válido'''
        showerror('ValueError',
      'Digite um ano de nascimento válido')

    idade = 2017 - ano_nascimento
    nome = nome_et.get()
    texto = 'Olá {}, você tem {} anos.'
    monitor.configure(text=texto.format(
                              nome, idade))
#  _____________________________fim funções

'Cria janela principal'
root = Tk()

'Cria Label monitor com texto vazio'
monitor = Label(root, text='', height=10)
monitor.pack(side=TOP)

'Cria label nome'
nome_lb = Label(root, text='Nome:')
nome_lb.pack(side=TOP)

'Cria entrada para receber nome'
nome_et = Entry(root)
nome_et.pack(side=TOP)

'Cria label idade'
idade_lb = Label(root, text='Idade:')
idade_lb.pack(side=TOP)

'Cria entrada para receber idade'
idade_et = Entry(root)
idade_et.pack(side=TOP)

'''Cria botão calcular, comando associado
                       a funcao calcular'''
bt_calcular = Button(root, text='Calcular',
                          command=calcular)
bt_calcular.pack(side=TOP)


root.geometry('300x300')
root.title('Prop 02 | by KamenRider')
root.mainloop()