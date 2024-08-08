# -- coding: utf-8 --
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from funcoes_tela import MontaTela, PosicionaBotao, sair, fechar_tela, ExportaDadosGrid
from vars import *
import conexao as cn
from imagens import logo_oficial, icone_voltar, icone_limpar, icone_excel

def limpar():
    txt_Boleto.delete(0,"end")
    txt_Nome.delete(0,"end")
    txt_Vencimento.delete(0,"end")
    txt_DataHora.delete(0,"end")
    txt_Status.delete(0,"end")
    txt_pes_nome.delete(0,"end")
    
    
    txt_Boleto.focus_set()
    
    image_label.pack_forget()
    
    visualizar()
    
    
def buscarBoleto():
    var_codigo = txt_Boleto.get()
 
    con=cn.Conexao()                
    sql_txt = 'select "ID", "Nome", "Boleto", "Vencimento", "DataHoraEnvio", "Status" from "BoletosEnviados" WHERE "Boleto"  = %s order by "DataHoraEnvio"'         
    rs=con.consultar_tree(sql_txt, (var_codigo,))
    
    if rs:
        limpar()
        txt_Boleto.insert(0, rs[0][2])
        txt_Nome.insert(0, rs[0][1])
        txt_Vencimento.insert(0,rs[0][3])
        txt_DataHora.insert(0,rs[0][4])
        txt_Status.insert(0,rs[0][5])
    else:
        tk.messagebox.showwarning("Aviso", "Boleto não Encontrado",parent = tela_conferencia)
        limpar()
        txt_Boleto.focus_set()

    con.fechar()     
        
def duplo_click(event):
    limpar()
    item = tree.item(tree.selection())
    boleto = item['values'][2]  
    
    txt_Boleto.insert(0,boleto )
    buscarBoleto() 
    
    
def visualizar():
    con=cn.Conexao()

    sql_txt = 'select "ID", "Nome", "Boleto", "Vencimento", "DataHoraEnvio", "Status" from "BoletosEnviados" order by "DataHoraEnvio"'
    
    rs=con.consultar_tree(sql_txt)

    tree.bind("<Double-1>", duplo_click)
    
    for linha in tree.get_children():
        tree.delete(linha)
    
    for linha in rs:
        tree.insert("", tk.END, values=linha)

    con.fechar()    
    
def pesquisar_nome(p):
    con=cn.Conexao()
    condicao = f"like lower('{p}%')"

    sql_txt = f'select "ID", "Nome", "Boleto", "Vencimento", "DataHoraEnvio", "Status" from "BoletosEnviados" WHERE lower("Nome") {condicao} order by "DataHoraEnvio"'
    
    rs=con.consultar_tree(sql_txt)

    tree.bind("<Double-1>", duplo_click)
    
    for linha in tree.get_children():
        tree.delete(linha)
    
    for linha in rs:
        tree.insert("", tk.END, values=linha)

    con.fechar()   

    return True   

def pesquisar_Status():
    con=cn.Conexao()
    
    status = txt_Status.get()
    condicao = f"like lower('{status}%')"

    sql_txt = f'select "ID", "Nome", "Boleto", "Vencimento", "DataHoraEnvio", "Status" from "BoletosEnviados" WHERE lower("Status") {condicao} order by "DataHoraEnvio"'
    
    rs=con.consultar_tree(sql_txt)

    tree.bind("<Double-1>", duplo_click)
    
    for linha in tree.get_children():
        tree.delete(linha)
    
    for linha in rs:
        tree.insert("", tk.END, values=linha)

    con.fechar()   

    return True 
       
cor = "black"
largura_caixa = 100
posicao_vertical = 50

def menu():
    tela_conferencia.destroy()
        
tela_conferencia = MontaTela(cor, "Relatório de Conferência Envio Boletos", False)
pes_nome = tela_conferencia.register(func=pesquisar_nome)

# Insere um Label - anchor w= esquerda, e=direita, c=centralizada
lbl_Boleto = tk.Label(tela_conferencia, text ="Boleto:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lbl_Boleto.place(x = posicao_vertical, y = 60, width = largura_caixa,  height = 25)
txt_Boleto = tk.Entry(tela_conferencia, width = 35, font=('Roboto', 12))
txt_Boleto.place(x = 150, y = 60, width = 200, height = 25)
# txt_Boleto.place(x = 150, y = 60, width = 100, height = 25)

buscabtn = tk.Button(tela_conferencia, text ="Pesquisar", 
                     bg ='white',foreground='black', font=('Roboto', 12, 'bold'), command = buscarBoleto)
buscabtn.place(x = 355, y = 60, width = 90, height = 25)

lbl_Nome = tk.Label(tela_conferencia, text ="Nome:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lbl_Nome.place(x = posicao_vertical, y = 100, width = largura_caixa, height = 25)
txt_Nome = tk.Entry(tela_conferencia, width = 35, font=('Roboto', 12))
txt_Nome.place(x = 150, y = 100, width = 375, height = 25)

lbl_Vencimento = tk.Label(tela_conferencia, text ="Vencimento:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lbl_Vencimento.place(x = posicao_vertical, y = 140, width = largura_caixa, height = 25)
txt_Vencimento = tk.Entry(tela_conferencia, width = 35, font=('Roboto', 12))
txt_Vencimento.place(x = 150, y = 140, width = 375, height = 25)

lbl_DataHora = tk.Label(tela_conferencia, text ="Envio:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lbl_DataHora.place(x = posicao_vertical, y = 180, width = largura_caixa, height = 25)
txt_DataHora = tk.Entry(tela_conferencia, width = 35, font=('Roboto', 12))
txt_DataHora.place(x = 150, y = 180, width = 375, height = 25)

lbl_Status = tk.Label(tela_conferencia, text ="Status:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lbl_Status.place(x = posicao_vertical, y = 220, width = largura_caixa, height = 25)
txt_Status = tk.Entry(tela_conferencia, width = 35, font=('Roboto', 12))
txt_Status.place(x = 150, y = 220, width = 375, height = 25)

busca_Status = tk.Button(tela_conferencia, text ="Pesquisar", 
                         bg ='white',foreground='black', font=('Roboto', 12, 'bold'), command = pesquisar_Status)
busca_Status.place(x = 530, y = 220, width = 90, height = 25)

lbl_pes_nome = tk.Label(tela_conferencia, text ="Pesquisar por Nome :", font=('Roboto', 12, 'bold'), anchor = "w")
lbl_pes_nome.place(x = 150, y = 260, width=200, height = 25)
txt_pes_nome = tk.Entry(tela_conferencia, width = 35, font=('Roboto', 12),validate='key', validatecommand=(pes_nome,'%P'))
txt_pes_nome.place(x = 315, y = 260, width = 360, height = 25)

style = tk.ttk.Style()
style.configure("mystyle.Treeview", font=("Roboto", 10))
style.configure("mystyle.Treeview.Heading", font=("Roboto", 12, "bold"))

tree = tk.ttk.Treeview(tela_conferencia, column=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', style="mystyle.Treeview")

tree.column("#1")
tree.heading("#1", text="ID")
tree.column("#1", width=0, stretch=tk.NO, anchor ='c')

tree.column("#2")
tree.heading("#2", text="Nome")
tree.column("#2", width = 500, anchor ='w')

tree.column("#3")
tree.heading("#3", text="Boleto")
tree.column("#3", width = 150, anchor ='w')

tree.column("#4")
tree.heading("#4", text="Vencimento")
tree.column("#4", width = 100, anchor ='c')

tree.column("#5")
tree.heading("#5", text="Envio")
tree.column("#5", width = 180, anchor ='c')

tree.column("#6")
tree.heading("#6", text="Status")
tree.column("#6", width = 100, anchor ='w')

tree.place(x=150,y=300,height=590)

scrollbar = tk.ttk.Scrollbar(tela_conferencia, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.place(x = 1170, y = 300,height=590)

#Botão Menu
imagem = Image.open(icone_voltar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnmenu = tk.Button(tela_conferencia, text ="Menu",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=menu, underline=0)
btnmenu.image = tkimage
btnmenu.pack(pady=20)
btnmenu.place(x = 1090, y = 900, width = 100)

tela_conferencia.bind_all("<Alt-m>", lambda e: menu())
tela_conferencia.bind_all("<Alt-l>", lambda e: limpar())
#Botão Menu

#Botão Limpar
imagem = Image.open(icone_limpar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnlimpar = tk.Button(tela_conferencia, text ="Limpar",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=limpar, underline=0)
btnlimpar.image = tkimage
btnlimpar.pack(pady=20)
PosicionaBotao(tela_conferencia, btnmenu, btnlimpar)
#Botão Limpar

#Botão Excel
imagem = Image.open(icone_excel)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnExcel = tk.Button(tela_conferencia, text ="Exportar",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=lambda:ExportaDadosGrid(tela_conferencia, tree), underline=0)
btnExcel.image = tkimage
btnExcel.pack(pady=20)
PosicionaBotao(tela_conferencia, btnlimpar, btnExcel)
#Botão Excel

visualizar()

txt_Boleto.focus_set()

image_label = tk.Label(tela_conferencia)

# Variável global para armazenar o caminho da imagem atual
current_image_path = None

# tela_conferencia.bind('<Escape>', lambda event: sair(tela_conferencia))
tela_conferencia.bind('<Escape>', lambda event: fechar_tela(tela_conferencia))

#Mantêm a tela_conferencia em Execução
tela_conferencia.mainloop()

