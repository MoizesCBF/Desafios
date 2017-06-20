from tkinter import *

root = Tk()

'Instancia um canvas com fundo branco'
bandeira = Canvas(root, bg='white')
bandeira.pack()

'Criando esfera vermelha (sol nascente)'
sol = bandeira.create_oval(80, 20, 220, 130, fill='red')

'''Dependendo da resolução do monitor,
pode-se não ter uma esfera perfeita.'''

root.geometry('300x150')  #  Janela retangular
root.title('Proposta 4 | By Harry')
root.mainloop()