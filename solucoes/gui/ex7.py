from tkinter import *
from tkinter.messagebox import *

#  __________________Classes________________

class DNA:
    def __init__(self,mestre):
        #             mestre --> janela raiz
        self.mestre=mestre  #  permite que métodos acessem 'mestre' 
        self.mestre.geometry('300x300')
        self.mestre.title('Contagem de bases'
                               '| by Harry')

        'Cria-se um label'
        self.seq=Label(self.mestre,
                       text='Sequência: ')
        self.seq.grid(row=0,column=0)

        'Cria-se uma entrada'
        self.ed=Entry(self.mestre)
        self.ed.grid(row=0,column=1)

        'Cria-se dois botões'
        self.sair_bt = Button(self.mestre,
                              text='Sair',
                  command=self.aoClicarSair)
        self.sair_bt.grid(row=1,column=0)
        self.verif_bt = Button(self.mestre,
                           text='Verificar',
             command=self.aoClicarVerificar)
        self.verif_bt.grid(row=1,column=1)

        

    def aoClicarSair (self):
        resp=askyesno('Sair','Deseja '
                          'realmente sair?')
        if resp:
            'encerra janela raiz'
            self.mestre.destroy()
        else:
            pass

    def aoClicarVerificar (self):
        dna = self.ed.get()# captura entrada
        dna = dna.lower() # entrada em lower

        a, c, g, t = 0, 0, 0, 0 
        #  Loop (for) para contagem de bases
        for base in dna: 
        #Verifica se base é uma base válida'
            if base != 'a' and base != 'c' and base != 'g' and base != 't':
                showerror('ValueError',
                  'Sequência DNA inválida.')
        #Caso base inválida, quebre o loop
                break 
        
            if base == 'a':
                a+=1 #  Acumulador de a
            elif base == 'c':
                c+=1 #  Acumulador de c
            elif base == 'g':
                g+=1 #  Acumulador de g
            else:
                t+=1 #  Acumulador de t
        texto = 'A = {}\nC = {}\nG = {}
                '\nT = {}'
        showinfo('Resp',
                      texto.format(a,c,g,t))
#  ___________________________Fim de Classes


#  _______________Código_______________________

root=Tk()

meuapp = DNA(root) #  meuapp é um DNA()

root.mainloop()
#  _______________________________Fim de código
