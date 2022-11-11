from tkinter import *
from funcoes import *
janela = Tk()
janela.title("Prontuário eletônico")
janela.minsize(200, 200)
janela.geometry("200x250")


teste = "Cadastros"
#Funções

def abrirNovaJanela(teste):
          
    newWindow = Toplevel(janela) 
   
    newWindow.title(teste) 
    
    newWindow.geometry("200x200")


texto_menu_inicial = Label(janela, text='Menu Inicial')
texto_menu_inicial.grid(column=0, row=0)

texto_orientacao = Label(janela, text='Escolha uma opção')
texto_orientacao.grid(column=0, row=1)

botao = Button(janela, text="Cadastros",  command = abrirNovaJanela(teste))
botao.grid(column=0, row=3, padx=10, pady=10)

botao = Button(janela, text="Agendamento", command = abrirNovaJanela)
botao.grid(column=0, row=4, padx=10, pady=10)

botao = Button(janela, text="Nova Consulta", command = abrirNovaJanela)
botao.grid(column=0, row=5, padx=10, pady=10)

botao = Button(janela, text="Relatórios", command = abrirNovaJanela)
botao.grid(column=0, row=6, padx=10, pady=10)

janela.mainloop()