from tkinter import *
from tkinter.messagebox import *

#  ______________Funções___________________
def clickSair():
    resposta=askyesno('Encerrar aplicação',
                'Certeza que desja sair?')
    if resposta:
        janela.destroy()
    else:
        pass

def calcular():
    try:
        num = int(num_et.get())
        den = int(den_et.get())
        resultado = num/den
        texto='A divisão de {} por {} é {}.'
        monitor.configure(text=texto.format(
                       num, den, resultado))
    except ZeroDivisionError:
        showerror('Divisão por Zero',
'Denominador deve ser diferente de zero.')
    except:
        showerror('ValueError',
        'Você digitou um valor inválido.')
#  _____________________________fim funções

janela = Tk()

'Criando um frame'
frame1 = Frame(janela)
frame1.pack()

'Criando label monitor'
monitor = Label(frame1, height=5)
monitor.grid(row=0, column=0, columnspan=2)

'Criando label numerador'
num_lb = Label(frame1, text='Numerador')
num_lb.grid(row=1, column=0)

'Criando entrada para numerador'
num_et = Entry(frame1, width=9)
num_et.grid(row=1, column=1)

'Criando label denominador'
den_lb = Label(frame1, text='Denominador')
den_lb.grid(row=2, column=0)

'Criando entrada para denominador'
den_et = Entry(frame1, width=9)
den_et.grid(row=2, column=1)

'Criando botão calcular'
ok_bt = Button(frame1,text='OK',
               height=5, command=calcular)
ok_bt.grid(row=3, column=0, sticky=W+E)

'Criando botão sair'
sair_bt = Button(frame1, text='Sair',
                         height=5,
                         command=clickSair)
sair_bt.grid(row=3, column=1, sticky=W+E)

janela.geometry('300x300')
janela.title('Prop 3 | by KamenRider')
janela.mainloop()