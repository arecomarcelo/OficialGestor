# -- coding: utf-8 --
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
# from funcoes import PosicionaBotao, CriarBotao
from funcoes_tela import MontaTela, PosicionaBotao, sair, fechar_tela
from vars import *
import conexao as cn
from imagens import logo_oficial, icone_voltar, icone_limpar, icone_gravar

def limpar():
    txtcodigo.delete(0,"end")
    txtnome.delete(0,"end")
    txtestoque.delete(0,"end")
    txtlocalizacao.delete(0,"end")
    txtcodigo.focus_set()
    
    image_label.pack_forget()
    
    # visualizar()
    
def buscar():
    var_codigo = txtcodigo.get()
 
    con=cn.Conexao()
                
    sql_txt = 'SELECT "CodigoExpedicao", "Nome", "Estoque", "Localizacao", "CodigoInterno" FROM "Produtos" WHERE "CodigoExpedicao" = %s order by "Nome"'      
        
    rs=con.consultar_tree(sql_txt, (var_codigo,))
    
    if rs:
    
        limpar()
    
        txtcodigo.insert(0, rs[0][0])
        txtnome.insert(0, rs[0][1])
        txtestoque.insert(0,rs[0][2])
        txtlocalizacao.insert(0,rs[0][3])
    
    else:
        tk.messagebox.showwarning("Aviso", "Código não Encontrado",parent = tela_pesquisa)
        limpar()
        txtcodigo.focus_set()

    con.fechar()  
    
def duplo_click(event):
    limpar()
    item = tree.item(tree.selection())
    codigo_expedicao = item['values'][0]
    codigo_interno = item['values'][4]   
    
    txtcodigo.insert(0,codigo_expedicao )
    buscar()

   # Carrega a imagem com base no item selecionado
    image_path = f"{caminhoImagensProdutos}{codigo_interno}.png"
    if image_path:
        load_image(image_path)    
    
  
    
def visualizar():
    con=cn.Conexao()

    sql_txt = 'SELECT "CodigoExpedicao", "Nome", "Estoque", "Localizacao", "CodigoInterno" FROM "Produtos" order by "Nome"'
    
    rs=con.consultar_tree(sql_txt)

    tree.bind("<Double-1>", duplo_click)
    
    for linha in tree.get_children():
        tree.delete(linha)
    
    for linha in rs:
        tree.insert("", tk.END, values=linha)

    con.fechar()    
    
def pesquisar_produto(p):
    con=cn.Conexao()
    condicao = f"like lower('{p}%')"

    sql_txt = f'SELECT "CodigoExpedicao", "Nome", "Estoque", "Localizacao", "CodigoInterno" FROM "Produtos" WHERE lower("Nome") {condicao} order by "Nome"'  
    
    rs=con.consultar_tree(sql_txt)

    tree.bind("<Double-1>", duplo_click)
    
    for linha in tree.get_children():
        tree.delete(linha)
    
    for linha in rs:
        tree.insert("", tk.END, values=linha)

    con.fechar()   

    return True    

def load_image(image_path):
    global current_image_path  # Salva o caminho da imagem atual para uso posterior
    current_image_path = image_path
    # Abre a imagem
    image = Image.open(image_path)
    image = image.resize((500, 500), Image.LANCZOS)  # Redimensiona a imagem
    photo = ImageTk.PhotoImage(image)

    # Exibe a imagem em um Label
    image_label.config(image=photo)
    image_label.image = photo
    image_label.pack(side="right", anchor="n")
    
def open_image_in_zoom(event):
    if current_image_path:
        # # Cria uma nova janela
        # zoom_window = tk.Toplevel(tela_pesquisa)
        # zoom_window.title("Imagem em Zoom")

        # Abre a imagem original
        image = Image.open(current_image_path)
        image = image.resize((845, 845), Image.LANCZOS)  # Redimensiona a imagem
        photo = ImageTk.PhotoImage(image)
        
        image_label.config(image=photo)
        image_label.image = photo
        image_label.pack(side="right", anchor="n")        

        # # Cria um Label para exibir a imagem em zoom
        # zoom_label = tk.Label(zoom_window, image=photo)
        # zoom_label.image = photo
        # zoom_label.pack()    
        
def gravar():
    # var_codigo = txtcodigo.get()
    # var_nome = txtnome.get()
    # var_telefone = txttelefone.get()
    # var_email = txtemail.get()
    # var_observacao = txtobservacao.get("1.0","end")


    # con=cn.conexao()
    # sql_txt = f"select codigo,nome,telefone,email,observacao from clientes where codigo = {var_codigo}"

    # rs=con.consultar(sql_txt)

    # if rs:
    #     sql_text = f"update clientes set nome='{var_nome}',telefone='{var_telefone}',email='{var_email}',observacao='{var_observacao}' where codigo = '{var_codigo}'"
    # else:
    #     sql_text = f"insert into clientes(codigo,nome,telefone,email,observacao) values ({var_codigo},'{var_nome}','{var_telefone}','{var_email}','{var_observacao}')"

    # print(sql_text)
    # if con.gravar(sql_text):
    #     messagebox.showinfo("Aviso", "Item Gravado com Sucesso", parent = tela_pesquisa)
    #     limpar()
    # else:
    #     messagebox.showerror("Erro", "Houve um Erro na Gravação", parent = tela_pesquisa)

    # con.fechar()

    visualizar()    
        
cor = "black"
largura_caixa = 100
posicao_vertical = 50

def menu():
    tela_pesquisa.destroy()
        
tela_pesquisa = MontaTela(cor, "Listagem Estoque", False)
pes_nome = tela_pesquisa.register(func=pesquisar_produto)

# Insere um Label - anchor w= esquerda, e=direita, c=centralizada
lblcodigo = tk.Label(tela_pesquisa, text ="Codigo:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lblcodigo.place(x = posicao_vertical, y = 60, width = largura_caixa,  height = 25)
txtcodigo = tk.Entry(tela_pesquisa, width = 35, font=('Roboto', 12))
txtcodigo.place(x = 150, y = 60, width = 100, height = 25)
txtcodigo.place(x = 150, y = 60, width = 100, height = 25)

buscabtn = tk.Button(tela_pesquisa, text ="Pesquisar", 
                     bg ='white',foreground='black', font=('Roboto', 12, 'bold'), command = buscar)
buscabtn.place(x = 280, y = 60, width = 90, height = 25)

lblnome = tk.Label(tela_pesquisa, text ="Nome:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lblnome.place(x = posicao_vertical, y = 100, width = largura_caixa, height = 25)
txtnome = tk.Entry(tela_pesquisa, width = 35, font=('Roboto', 12))
txtnome.place(x = 150, y = 100, width = 375, height = 25)

lblestoque = tk.Label(tela_pesquisa, text ="Estoque:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lblestoque.place(x = posicao_vertical, y = 140, width = largura_caixa, height = 25)
txtestoque = tk.Entry(tela_pesquisa, width = 35, font=('Roboto', 12))
txtestoque.place(x = 150, y = 140, width = 375, height = 25)

lbllocalizacao = tk.Label(tela_pesquisa, text ="Localização:", bg="black", fg="WhiteSmoke", font=('Roboto', 12), anchor = "e")
lbllocalizacao.place(x = posicao_vertical, y = 180, width = largura_caixa, height = 25)
txtlocalizacao = tk.Entry(tela_pesquisa, width = 35, font=('Roboto', 12))
txtlocalizacao.place(x = 150, y = 180, width = 375, height = 25)

lbl_pes_nome = tk.Label(tela_pesquisa, text ="Pesquisar por Nome :", font=('Roboto', 12, 'bold'), anchor = "w")
lbl_pes_nome.place(x = 150, y = 220, width=200, height = 25)
txt_pes_nome = tk.Entry(tela_pesquisa, width = 35, font=('Roboto', 12),validate='key', validatecommand=(pes_nome,'%P'))
txt_pes_nome.place(x = 315, y = 220, width = 360, height = 25)

style = tk.ttk.Style()
style.configure("mystyle.Treeview", font=("Roboto", 10))
style.configure("mystyle.Treeview.Heading", font=("Roboto", 12, "bold"))

tree = tk.ttk.Treeview(tela_pesquisa, column=("c1", "c2", "c3", "c4"), show='headings', style="mystyle.Treeview")

tree.column("#1")
tree.heading("#1", text="Código")
tree.column("#1", width = 100, anchor ='c')

tree.column("#2")
tree.heading("#2", text="Nome")
tree.column("#2", width = 400, anchor ='w')

tree.column("#3")
tree.heading("#3", text="Estoque")
tree.column("#3", width = 200, anchor ='c')

tree.column("#4")
tree.heading("#4", text="Localização")
tree.column("#4", width = 200, anchor ='c')

tree.place(x=150,y=260,height=590)

scrollbar = tk.ttk.Scrollbar(tela_pesquisa, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.place(x = 1050, y = 260,height=590)

#Botão Menu
imagem = Image.open(icone_voltar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnmenu = tk.Button(tela_pesquisa, text ="Menu",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=menu, underline=0)
btnmenu.image = tkimage
btnmenu.pack(pady=20)
btnmenu.place(x = 980, y = 860, width = 90)

tela_pesquisa.bind_all("<Alt-m>", lambda e: menu())
tela_pesquisa.bind_all("<Alt-l>", lambda e: limpar())
tela_pesquisa.bind_all("<Alt-g>", lambda e: gravar())
# tela_pesquisa.bind('<Alt-M>', lambda event: menu())
#Botão Menu

#Botão Limpar
imagem = Image.open(icone_limpar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btnlimpar = tk.Button(tela_pesquisa, text ="Limpar",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=limpar, underline=0)
btnlimpar.image = tkimage
btnlimpar.pack(pady=20)
PosicionaBotao(tela_pesquisa, btnmenu, btnlimpar)
#Botão Limpar

#Botão Gravar
imagem = Image.open(icone_gravar)
imagem = imagem.resize((30, 30))
tkimage = ImageTk.PhotoImage(imagem)
btngravar = tk.Button(tela_pesquisa, text ="Gravar",image=tkimage, compound='left', foreground='black', font=('Roboto', 12), command=gravar, underline=0)
btngravar.image = tkimage
btngravar.pack(pady=20)
PosicionaBotao(tela_pesquisa, btnlimpar, btngravar)
#Botão Gravar

visualizar()

txtcodigo.focus_set()

image_label = tk.Label(tela_pesquisa)

# Vincula o evento de clique à função open_image_in_zoom
image_label.bind("<Button-1>", open_image_in_zoom)

# Variável global para armazenar o caminho da imagem atual
current_image_path = None

# tela_pesquisa.bind('<Escape>', lambda event: sair(tela_pesquisa))
tela_pesquisa.bind('<Escape>', lambda event: fechar_tela(tela_pesquisa))

#Mantêm a tela_pesquisa em Execução
tela_pesquisa.mainloop()

