# -- coding: utf-8 --
# Importação das bibliotecas necessárias
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from imagens import logo_oficial,icone_oficial

# Criação da janela principal da aplicação
tela = tk.Tk() 
tela.geometry('1960x800+0+0')  # Definição do tamanho inicial da janela
tela.state('zoomed')  # Maximiza a janela na inicialização
tela.title("Oficial Gestor - 1.0")  # Define o título da janela
tela['bg'] = "black"  # Define a cor de fundo da janela

# Carregar a imagem do ícone
icone_image = Image.open(icone_oficial)
icone_photo = ImageTk.PhotoImage(icone_image)

# Definir a imagem do ícone
tela.iconphoto(False, icone_photo)

# Carrega e exibe a imagem de fundo
image = Image.open(logo_oficial)#.resize((1800, 1080))
tkimage = ImageTk.PhotoImage(image)
label = tk.Label(tela, image=tkimage, bd=0, highlightthickness=0)
label.pack(padx=0, pady=0)
tk.Label(tela, image=tkimage).pack()

# Função que exibe informações sobre o sistema
def sobre():
    messagebox.showinfo("Sobre", "Oficial Gestor 1.0")

# Função para confirmar e executar a saída do sistema
def sair():
    var_sair = messagebox.askyesno("Sair", "Tem certeza que deseja sair?")
    if var_sair == True:
        tela.destroy()

# Criação da barra de menu
barramenu = tk.Menu(tela)
menu_func = tk.Menu(barramenu)
menu_ajuda = tk.Menu(barramenu)

# Adição de menus e comandos à barra de menu
barramenu.add_cascade(label="Funcionalidades", menu=menu_func)
menu_func.add_command(label="Clientes")
menu_func.add_command(label="Produtos/Serviços")
menu_func.add_command(label="Vendas")
menu_func.add_command(label="Gestão de Acessos")
menu_func.add_separator()
menu_func.add_command(label="Sair", command=sair)  # Comando para sair do sistema

barramenu.add_cascade(label="Ajuda", menu=menu_ajuda)
menu_ajuda.add_command(label="Sobre", command=sobre)  # Comando para exibir informações sobre o sistema

# Configuração da barra de menu na janela principal
tela.config(menu=barramenu)

# Inicia o loop principal da aplicação
tela.mainloop()