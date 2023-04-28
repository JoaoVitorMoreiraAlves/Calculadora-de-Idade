from tkinter import *

#Importanto tkcalendar para criar calendários
from tkcalendar import Calendar, DateEntry

#Importate dateutil para calcular calendários
from dateutil.relativedelta import relativedelta

#Importante datetime para manipular datas
from datetime import date


#Função Calcular
def calcular():
    #Tratando os dados da data inicial
    inicial = calendario1.get() #Pegando a data

    #Transformando a data do inicial para 3 variáveis diferentes em formato inteiro
    dia_inicial, mes_inicial, ano_inicial = [int(i) for i in inicial.split('/')]

    #Criando variável do tipo DATE para guardar os valores das 3 variáveis
    data_inicial = date(ano_inicial, mes_inicial, dia_inicial)

    #Tratando os dados da data nascimento
    nascimento = calendario2.get() #Pegando a data de nasc

    #Transformando a data do nasc para 3 variáveis diferente
    dia_nasc, mes_nasc, ano_nasc = [int(i) for i in nascimento.split('/')]

    #Criando variável do tipo DATE para guardar os valores
    data_nasc = date(ano_nasc, mes_nasc, dia_nasc)

    idade = relativedelta(data_inicial,data_nasc)

    label_baixo_ano['text'] = idade.years
    label_baixo_mes['text'] = idade.months
    label_baixo_dia['text'] = idade.days

    
#Criando Janela
janela = Tk()
janela.geometry('310x400')
janela.resizable(width=False, height=False)#Não pode modificar o tamanho da tela
janela.title('Calculadora de Idade')


#Dividir a Janela em 2 Frames

frame_cima = Frame(janela, width=310, height=130, pady=0, padx=0, 
                   relief=FLAT, bg='#000000')
frame_cima.grid(row=0, column=0)


frame_baixo = Frame(janela,width=310, height= 270, pady=0, padx=0, 
                    relief=FLAT, bg= '#3b3b3b')
frame_baixo.grid(row=1, column=0)


#Criando Label para o Frame de Cima

label_cima1 = Label(frame_cima, text="Calculadora", width=25, height=1, relief=FLAT, 
                    anchor=CENTER,fg='#FFFFFF', font='Arial 15 bold',bg='#000000')
label_cima1.place(x=0, y=15)

label_cima2 = Label(frame_cima, text="De Idade", width=25, height=1, relief=FLAT, 
                    anchor=CENTER,fg='#FFA500', font='Arial 15 bold',bg='#000000')
label_cima2.place(x=0, y=60)



#Criando Label para o Frame de Baixo

label_baixo1 = Label(frame_baixo, text="Data Inicial", padx=0, pady=0,fg='#FFFFFF', 
                     bg='#3b3b3b', relief=FLAT, font="Arial 11 bold")
label_baixo1.place(x=15,y=25)

#Criando Calendário para a Data Inicial

calendario1 = DateEntry(frame_baixo, width=13, background='#191970', foreground='#FFFFFF', 
                        borderwidth=2, font='Arial 9 bold', locale='pt_BR',
                        date_pattern='dd/mm/y')
calendario1.place(x=190,y=25)


label_baixo2 = Label(frame_baixo, text="Data de Nascimento", padx=0,pady=0, fg='#FFFFFF', 
                     bg='#3b3b3b', relief=FLAT, font="Arial 11 bold")
label_baixo2.place(x=15,y=60)

#Criando Calendário para a Datade Nascimento
calendario2 = DateEntry(frame_baixo, width=13, background='#191970', foreground='#FFFFFF', 
                        borderwidth=2, font='Arial 9 bold', locale='pt_BR',
                        date_pattern='dd/mm/y')
calendario2.place(x=190,y=60)



#Criando label para representar a Quantidade de Anos

#Número de Anos
label_baixo_ano = Label(frame_baixo, text='00', padx=0, pady=0,fg='#FFFFFF', 
                     bg='#3b3b3b', relief=FLAT, font="Arial 18 bold", anchor=CENTER)
label_baixo_ano.place(x=50,y=110)

#Palavra "Anos"
label_baixo_ano_nome = Label(frame_baixo, text="Anos", padx=0, pady=0,fg='#FFFFFF', 
                     bg='#3b3b3b', relief=FLAT, font="Arial 13 bold", anchor=CENTER)
label_baixo_ano_nome.place(x=42,y=145)



#Criando Label para representar a Quantidade de Meses

#Número de Meses
mes = ''
label_baixo_mes = Label(frame_baixo, text='00', padx=0, pady=0,fg='#FFFFFF', 
                     bg='#3b3b3b', relief=FLAT, font="Arial 18 bold", anchor=CENTER)
label_baixo_mes.place(x=140,y=110)

#Palavra "Mês"
label_baixo_mes_nome = Label(frame_baixo, text="Mês", padx=0, pady=0,fg='#FFFFFF', 
                     bg='#3b3b3b', relief=FLAT, font="Arial 13 bold", anchor=CENTER)
label_baixo_mes_nome.place(x=132,y=145)


#Criando Label para representar a Quantidade de Dias

#Número de Dias

label_baixo_dia = Label(frame_baixo, text='00', padx=0, pady=0,fg='#FFFFFF', 
                     bg='#3b3b3b', relief=FLAT, font="Arial 18 bold", anchor=CENTER)
label_baixo_dia.place(x=222,y=110)

#Palavra "Dia"
label_baixo_dia_nome = Label(frame_baixo, text="Dia", padx=0, pady=0,fg='#FFFFFF', 
                     bg='#3b3b3b', relief=FLAT, font="Arial 13 bold", anchor=CENTER)
label_baixo_dia_nome.place(x=220,y=145)




#Criando Botão para calcular a quantidade de anos,meses e dias

botao = Button(frame_baixo, text="Calcular Idade", width=15, height=1, command=calcular,
               fg='#FFFFFF', bg='#3b3b3b', relief=RAISED, overrelief=RIDGE, font="Arial 13 bold")
botao.place(x=75,y=200)




janela.mainloop()