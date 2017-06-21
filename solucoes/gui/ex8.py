from tkinter import *
from tkinter.messagebox import *

#  _________________Classes_________________
class Calculadora:
    def __init__(self,mestre):
        #             mestre --> janela raiz
        self.mestre=mestre #  permite acesso por métodos
        self.mestre.geometry('250x300')
        self.mestre.title('Calculadora')
        
        #  Cria menu principal
        self.principal = Menu(self.mestre)
        self.mestre.configure(
                      menu=self.principal)

        #  Add menu em principal
        self.func = Menu(self.principal)
        self.principal.add_cascade(
                            label='Funções',
                            menu=self.func)

        #  Add submenu em funções
        self.func.add_command(label='Soma',
                          command=self.soma)
        self.func.add_command(
                       label='Subtração',
                       command=self.subtrai)
        self.func.add_command(
                            label='Divisão',
                        command=self.divide)
        self.func.add_command(
                      label='Multiplicação',
                    command=self.multiplica)

        #  Monitor para exibir resultado
        self.monitor = Label(text='',
                             height=5)
        self.monitor.grid(row=0,
                          column=0,
                          columnspan=2)

        #  Labels para entradas
        self.num1_lb = Label(
                        text='Primeiro Nº:')
        self.num1_lb.grid(row=1, column=0)
        self.num2_lb = Label(
                         text='Segundo Nº:')
        self.num2_lb.grid(row=2, column=0)

        #  Entrys para entradas
        self.num1_et = Entry()
        self.num1_et.grid(row=1, column=1)
        self.num2_et = Entry()
        self.num2_et.grid(row=2, column=1)

        #  Botões para Calcular
        self.sum_bt = Button(text='Somar',
                          command=self.soma)
        self.sum_bt.grid(row=3, column=0)
        self.sub_bt = Button(text='Subtrair',
                       command=self.subtrai)
        self.sub_bt.grid(row=3, column=1)
        self.div_bt = Button(text='Dividir',
                        command=self.divide)
        self.div_bt.grid(row=4, column=0)
        self.mult_bt = Button(
                         text='Multiplicar',
                    command=self.multiplica)
        self.mult_bt.grid(row=4, column=1)

    def verifica(self, resposta, texto):
        if resposta < 0: # cor = vermelho
            self.monitor.configure(
                                 text=texto,
                          font=('Arial',25),
                                   fg='red')
        else: #  define cor = azul
            self.monitor.configure(
                                 text=texto,
                          font=('Arial',25),
                                  fg='blue')  

    def soma(self):
        try: #  tratamento de erro com 'try'
            num1=float(self.num1_et.get())
            num2=float(self.num2_et.get())
            resp = num1 + num2
            texto='Resultado {}'.format(resp)
            self.verifica(resp, texto)
        except:
            showerror('Erro',
             'Entrada de valores inválidos')

    def subtrai(self):
        try: #  tratamento de erro com 'try'
            num1=float(self.num1_et.get())
            num2=float(self.num2_et.get())
            resp  = num1 - num2
            texto='Resultado {}'.format(resp)
            self.verifica(resp, texto)
        except:
            showerror('Erro',
             'Entrada de valores inválidos')

    def multiplica(self):
        try: #  tratamento de erro com 'try'
            num1 = float(self.num1_et.get())
            num2 = float(self.num2_et.get())
            resp = num1 * num2
            texto='Resultado {}'.format(resp)
            self.verifica(resp, texto)
        except:
            showerror('Erro',
             'Entrada de valores inválidos')
        
    def divide(self):
        try: #  tratamento de erro com 'try'
            num1 = float(self.num1_et.get())
            num2 = float(self.num2_et.get())
            resp = num1 / num2
            texto='Resultado {}'.format(resp)
            self.verifica(resp, texto)
        except ZeroDivisionError:
            showerror('Divisão por zero',
   'Denominador deve ser diferente de zero')
        except:
            showerror('Erro',
             'Entrada de valores inválidos')
#  ______________________________Fim Classes


#  ________________Código___________________

janela = Tk()

meuapp = Calculadora(janela)

janela.mainloop()
#  ____________________________Fim de código
