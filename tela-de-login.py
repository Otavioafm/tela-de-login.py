from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox

#cores---------------------------------------------------
cor1 = "#ffa200" #laranja forte
cor2 = '#f9f9f9' #branco
cor3 = '#221133' #roxo escuro


#Janelas--------------------------------------------------
janela = Tk()
janela.title('')
janela.geometry('310x300')
#janela.configure(background=cor)
janela.resizable(width=FALSE, height=FALSE)



#Divisor----------------------------------------------------
Frame_topo = Frame(janela, width=310, height=55, bg=cor2, relief='flat')
Frame_topo.grid(row=0,column=0, pady=1, padx=0, stick=NSEW)

Frame_baixo = Frame(janela, width=310, height=250, bg=cor2, relief='flat')
Frame_baixo.grid(row=1,column=0, pady=1, padx=0, stick=NSEW)

#configuração do frame superior/topo--------------------------
nome= Label(Frame_topo, text='LOGIN', anchor=NE , font=('electrolize 25'),bg=cor2, fg=cor3)
nome.place(x=5,y=5)

linha_login=Label(Frame_topo, text='',width=280, anchor=NW , font=('electrolize 1'),bg=cor1, fg=cor3)
linha_login.place(x=10,y=45)

#configuração do frame inferior/baixo--------------------------
usuario=Label(Frame_baixo, text='Usuário*', anchor=NW , font=('electrolize 10'),bg=cor2, fg=cor3)
usuario.place(x=10,y=20)

e_usuario= Entry(Frame_baixo, width=25, justify='left',font=('',15), highlightthickness=1, relief='solid')
e_usuario.place(x=14,y=50)



senha=Label(Frame_baixo, text='Senha*', anchor=NW , font=('electrolize 10'),bg=cor2, fg=cor3)
senha.place(x=10,y=95)

e_senha= Entry(Frame_baixo, width=25, justify='left',font=('',15), highlightthickness=1, relief='solid')
e_senha.place(x=14,y=130)


#credenciais do Usuário/ou coloque um banco de dados aqui--------------------------
credenciais=['otavio','123']

def verificar():
    login=e_usuario.get()
    senha=e_senha.get()

    if login=='otavio' and senha=='123':
       messagebox.showinfo('Login','Seja Bem vindo Criador do Fenix Bank')
    elif credenciais[0]==nome and credenciais[1]==senha:
       messagebox.showinfo('Login','Seja Bem vindo ao Fenix Bank')
    else:
       messagebox.showwarning('ERRO','Usuário ou Login incorretos')

#botão de entrar-------------------------------------------------------------------
btn_confirmar=Button(Frame_baixo, command=verificar, text='Entrar',width=34, height=2, font=('electrolize 10'),bg=cor1, fg=cor3, relief=RAISED, overrelief=RIDGE)
btn_confirmar.place(x=15,y=180)


janela.mainloop()