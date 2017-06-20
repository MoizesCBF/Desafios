from tkinter import *

#  ____________________Funções_____________________
def aoClicarBt():
    texto = 'Você clicou em OK.'
    nova_lb = Label(janela, text=texto)
    nova_lb.pack(side=TOP)
    pass
#  ______________________________________fim funções

janela = Tk()

'Cria um botão em janela'
ok_bt = Button(janela, text='OK', command=aoClicarBt)
ok_bt.pack(side=TOP)

janela.geometry('400x300')
janela.title('Proposta 5 | by Harry')
janela.mainloop()
