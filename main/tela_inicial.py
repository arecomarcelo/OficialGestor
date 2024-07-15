import tkinter as tk
from tkinter import Menu, messagebox
from PIL import Image, ImageTk
from imagens import img_sair, logo_oficial,icone_oficial

def funcao_exemplo():
    print("Botão clicado!")
    
def sair():
    var_sair = messagebox.askyesno("Sair", "Tem certeza que deseja sair?")
    if var_sair == True:
        tela.destroy()

tela = tk.Tk()
tela.geometry('1960x800+0+0')
tela.state('zoomed')
tela.title("Oficial Gestor - 1.0")
tela['bg'] = "black"

icone_image = Image.open(icone_oficial)
icone_photo = ImageTk.PhotoImage(icone_image)
tela.iconphoto(False, icone_photo)

menu_frame = tk.Frame(tela)
menu_frame.pack(side="top", fill="x")

image = Image.open(logo_oficial)
tkimage = ImageTk.PhotoImage(image)
label = tk.Label(tela, image=tkimage, bd=0, highlightthickness=0)
label.pack(padx=0, pady=0)
tk.Label(tela, image=tkimage).pack()

barra_menus = Menu(menu_frame)
tela.config(menu=barra_menus)

menu_rpa = tk.Menu(barra_menus)
menu_chatbot = tk.Menu(barra_menus)
menu_administracao = tk.Menu(barra_menus)
menu_ajuda = tk.Menu(barra_menus)

barra_menus.add_cascade(label="RPA", menu=menu_rpa)

barra_menus.add_cascade(label="ChatBot", menu=menu_chatbot)

barra_menus.add_cascade(label="Administração", menu=menu_administracao)
menu_administracao.add_command(label="Cadastro de Aplicação")#, command=aplicacoes)
menu_administracao.add_command(label="Cadastro de Usuário")#, command=usuarios)

barra_menus.add_cascade(label="Ajuda", menu=menu_ajuda)
menu_ajuda.add_command(label="Sobre")#, command=sobre)

icone_image = Image.open(img_sair)
icone_photo = ImageTk.PhotoImage(icone_image)
botao_personalizado = tk.Button(menu_frame, image=icone_photo, text="Sair", command=sair)
botao_personalizado.pack(side="right", padx=5, pady=2)

tela.mainloop()