import tkinter as tk
from tkinter import Menu, messagebox
from PIL import Image, ImageTk
from imagens import img_sair, logo_oficial,icone_oficial
from funcoes_tela import MontaTela, boletos_planilha, estoque_listagem, relatorio_conferencia, suporte, sobre, sair, fechar_tela
from funcoes import LimparConsole

LimparConsole()

tela = tk.Tk()
tela.geometry('1960x800+0+0')
tela.state('zoomed')
tela.title("Oficial Gestor - 1.0")
tela['bg'] = "black"

icone_image = Image.open(icone_oficial)
icone_photo = ImageTk.PhotoImage(icone_image)
tela.iconphoto(False, icone_photo)

image = Image.open(logo_oficial)
tkimage = ImageTk.PhotoImage(image)
label = tk.Label(tela, image=tkimage, bd=0, highlightthickness=0)
label.pack(padx=0, pady=0)
tk.Label(tela, image=tkimage).pack()

menu_frame = tk.Frame(tela)
menu_frame.pack(side="top", fill="x")

barra_menus = Menu(menu_frame, tearoff=0)
tela.config(menu=barra_menus)

# menu_rpa = tk.Menu(barra_menus)
menu_rpa = tk.Menu(barra_menus, tearoff=0)
menu_estoque = tk.Menu(barra_menus, tearoff=0)
menu_chatbot = tk.Menu(barra_menus, tearoff=0)
menu_administracao = tk.Menu(barra_menus, tearoff=0)
menu_ajuda = tk.Menu(barra_menus, tearoff=0)

barra_menus.add_cascade(label="RPA", menu=menu_rpa)
menu_rpa.add_command(label="Envio de Boletos - Planilha", command=boletos_planilha)
menu_rpa.add_command(label="Relatório Conferência",  accelerator="Alt+ O", command=relatorio_conferencia)
menu_rpa.add_separator()
menu_rpa.add_command(label="Sair", command=lambda: sair(tela))


barra_menus.add_cascade(label="Estoque", menu=menu_estoque)
menu_estoque.add_command(label="Listagem",  accelerator="Alt+L", underline=0,command=estoque_listagem)
menu_estoque.add_command(label="Lançamento")#, command=usuarios)
# tela.bind_all("<Alt-l>", lambda e: estoque_listagem())

barra_menus.add_cascade(label="ChatBot", menu=menu_chatbot)

barra_menus.add_cascade(label="Administração", menu=menu_administracao)
menu_administracao.add_command(label="Cadastro de Aplicação")#, command=aplicacoes)
menu_administracao.add_command(label="Cadastro de Usuário")#, command=usuarios)

barra_menus.add_cascade(label="Ajuda", menu=menu_ajuda)
menu_ajuda.add_command(label="Suporte", command=suporte)
menu_ajuda.add_command(label="Sobre", command=sobre)

# icone_image = Image.open(img_sair)
# icone_photo = ImageTk.PhotoImage(icone_image)
# botao_personalizado = tk.Button(menu_frame, image=icone_photo, text="Sair", command=sair)
# botao_personalizado.pack(side="right", padx=5, pady=2)

tela.bind('<Escape>', lambda event: fechar_tela(tela))

tela.bind_all("<Alt-r>", lambda e: relatorio_conferencia())
tela.bind_all("<Alt-l>", lambda e: estoque_listagem())

    
tela.mainloop()
