from tkinter import *

#  _____________Funções____________________
def aoClicarOk():
    print('Você clicou no botão OK!')

#  _____________________________Fim funções
janela = Tk()

'''Cria botão com texto = "OK" e comando 
                associado: aoClicarOk()'''
bt_ok = Button(janela, text='OK',
                       command=aoClicarOk)

'Usa-se pack() como gerenciador de layout'
bt_ok.pack(side=TOP)

janela.title(' | by Harry')
janela.geometry('250x50+300+300')
janela.mainloop()
