import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from vars import QuebraLinha, nome_aplicacao, celular_suporte, email_suporte

def boletos_planilha():
    exec(open("G:\\Meu Drive\\TI Oficial\\Projetos\\Cobranca\\Envio_Whatsapp\\BOT\\main.py", encoding="utf-8").read(),locals())
    
def suporte():
    messagebox.showinfo("Contatos de Suporte", f"{QuebraLinha}Whatsapp: {celular_suporte}{QuebraLinha}E-Mail: {email_suporte}")
    
def sobre():
    messagebox.showinfo("Sobre", nome_aplicacao)
    
def sair(tela):
    var_sair = messagebox.askyesno("Sair", "Tem certeza que deseja sair?")
    if var_sair:
        tela.destroy()    
  