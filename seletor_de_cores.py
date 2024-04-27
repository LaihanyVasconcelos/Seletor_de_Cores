from tkinter import *
from tkinter import ttk 
import tkinter.messagebox
#cores
cor1 = "#444466" #preto
cor2 = "#feffff" #branco
cor3 = '#9703ad' #roxo

#janelas
janela = Tk()
janela.title('Seletor de Cores')
janela.geometry("530x205")
janela.configure(bg=cor2)
janela.resizable(width=FALSE, height=FALSE)

#configurando a janela
tela = Label(janela, bg=cor1, width=40, height=10, bd=1)
tela.grid(row=0, column=0)

#criando frames para os botões laterais
frame_direita = Frame(janela, bg=cor2)
frame_direita.grid(row=0, column=1, padx=5)

frame_baixo = Frame(janela, bg=cor2)
frame_baixo.grid(row=1, column=0, columnspan=2, pady=15)#estará ocupando 2 colunas "columnspan"

#função scala (lógica)
def escala(valor):
    r = slide_red.get()
    g = slide_green.get()
    b = slide_blue.get()

    rgb = f'{r}, {g}, {b}' 

#convertendo o corpo rgb em hexadecimal
    hexadecimal = "#%02x%02x%02x" % (r, g, b)
#alterando a cor do fundo da tela
    tela['bg'] = hexadecimal

#para mostrar # da cor/ alterando a endry
    endry_cor.delete(0,END)
    endry_cor.insert(0,hexadecimal)

#criando função clicar
def onClick():

    #criar messagem dizendo que copiou informando
    tkinter.messagebox.showinfo("cor", "A cor foi copiada ♡")

    #serve para criar o botão copiar
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear
    clip.clipboard_append(endry_cor.get()) #vai pegar aquele valor
    clip.destroy() #apagar 


#configurando o fram_direita red                                         nw=vai para a direita                  
label_red = Label(frame_direita, text='Red', width=7, bg=cor2, fg='red', anchor='nw', font=('Time New Roman', 12, "bold"))
label_red.grid(row=0, column=0)

slide_red = Scale(frame_direita, command=escala, from_=0, to=255, length=150,bg=cor2, fg='red', orient=HORIZONTAL)
slide_red.grid(row=0, column=1)

#configurando o frame direita green
label_green = Label(frame_direita, text='Green', width=7, bg=cor2, fg='green', anchor='nw', font=('Time New Roman', 12, "bold"))
label_green.grid(row=1, column=0)

slide_green = Scale(frame_direita, command=escala, from_=0, to=255, length=150,bg=cor2, fg='green', orient=HORIZONTAL)
slide_green.grid(row=1, column=1)

#configurando o frame direita blue
label_blue = Label(frame_direita, text='Blue', width=7, bg=cor2, fg='blue', anchor='nw', font=('Time New Roman', 12, "bold"))
label_blue.grid(row=2, column=0)

slide_blue = Scale(frame_direita, command=escala,from_=0, to=255, length=150,bg=cor2, fg='blue', orient=HORIZONTAL)
slide_blue.grid(row=2, column=1)

# configurando frame_baixo
label_rgb = Label(frame_baixo, text='CÓDIGO HEX :', bg=cor2, font=('Ivy', 10, "bold"))
label_rgb.grid(row=0, column=0, padx=5)

endry_cor = Entry(frame_baixo, width=12, font=('Ivy', 10, "bold"), justify=CENTER)
endry_cor.grid(row=0, column=1, padx=5)

# botão copiar
botao_copiar = Button(frame_baixo, command=onClick, text='Copiar a cor', bg=cor2, font=('Ivy', 8, "bold"), relief=RAISED, overrelief=RIDGE)
botao_copiar.grid(row=0, column=2, padx=5)

# nome do app
label_app_nome = Label(frame_baixo, text='Seletor de Cores',  bg=cor2, fg=cor3, font=('Ivy', 15, "bold"))
label_app_nome.grid(row=0, column=3, padx=40)

#parte lógica










janela.mainloop()

