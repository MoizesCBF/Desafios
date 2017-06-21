from tkinter import *
from tkinter.messagebox import *


class aplicativo:
    
    def __init__(self, janela):
        #              janela --> raiz
        self.janela = janela #  permite acesso à raiz
        self.janela.geometry('200x200')
        self.janela.title('IMC | by Harry')

        #  Criando frame1:
        self.frame1 = Frame(self.janela)
        self.frame1.pack(side=LEFT)

        #  Criando frame2:
        self.frame2 = Frame(self.janela)
        self.frame2.pack(side=RIGHT)


        # Criando widgets em Frame1:
        self.peso=Label(self.frame1,
                        text='Peso: ')
        self.peso.grid(row=0, column=0)
        self.alt=Label(self.frame1,
                       text='Altura: ')
        self.alt.grid(row=1, column=0)
        self.bt_sair=Button(self.frame1,
                            text='Sair',
                      command=self.sair)
        self.bt_sair.grid(row=2,column=0)


        #  Criando widgets em Frame2:
        self.ed_p=Entry(self.frame2)
        self.ed_p.grid(row=0,column=0)
        self.ed_h=Entry(self.frame2)
        self.ed_h.grid(row=1,column=0)
        self.bt_calcular=Button(self.frame2,
                            text='Calcular',
                      command=self.calcular)
        self.bt_calcular.grid(row=2,column=0)
        
    def sair(self):
        resp = askyesno('Encerrar aplicação',
                    'Certeza que quer sair?')
        if resp:
            root.destroy()
        else:
            pass
        
    def mensagem(self,texto):
        showinfo('Mensagem', texto)
        
    def calcular (self):
        try:
            peso   = float(self.ed_p.get())
            altura = float(self.ed_h.get())
            
            if peso <= 0 or altura <=0:
                showerror('Valor Invalido',
             'Digite valor maior que zero')
            else:
                pass
        except:
            showerror('Valor Inválido',
          'Verifique os valores de entrada')
            
        try:
            resp = peso / (altura**2)
        except ZeroDivisionError:
            showerror('Valor Inválido',
                 'Valor não pode ser zero.')
        if resp < 18.5:
            self.mensagem('Abaixo do peso '
                                   'ideal.')
        elif resp > 25:
            self.mensagem('Acima do peso '
                                   'ideal.')
        else:
            self.mensagem('Você esta no '
                    'peso ideal. Parabéns!')    

#  __________________Código____________________
root=Tk()

meuapp = aplicativo(root)

root.mainloop()
#  _______________________________Fim do código

