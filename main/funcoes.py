import os 
import time
import dateutil.relativedelta
from datetime import datetime, timedelta
from telas.vars import *

# import pyperclip
# import html
# import re
# import pandas as pd
import shutil

# Data Atual
dtAtual = datetime.now() 
diaAtual = dtAtual.strftime("%d")
mesAtual = dtAtual.strftime("%m")
anoAtual = dtAtual.strftime("%Y")
horaAtual = dtAtual.strftime("%H")
minutoAtual = dtAtual.strftime("%M")
segundoAtual = dtAtual.strftime("%S")     

def FormataDataAtual():
    data = datetime.now() 
    dia = data.strftime("%d")
    mes = data.strftime("%m")
    ano = data.strftime("%Y")
    dataFormatada = '{}/{}/{}'.format(dia, mes, ano)
    return dataFormatada
    
def FormataHoraAtual():
    data = datetime.now() 
    hora = data.strftime("%H")
    minuto = data.strftime("%M")
    segundo = data.strftime("%S")
    horaFormatada = '{}:{}:{}'.format(hora, minuto, segundo)
    return horaFormatada

def DataHoraFormatada(): 
    data = FormataDataAtual()
    hora = FormataHoraAtual() 
    return f'{data} {hora}'

def LimpaLogs(caminho):
    mesAnterior = (dtAtual + dateutil.relativedelta.relativedelta(months=-1)).strftime("%m")
    mesAnterior = "-" + mesAnterior + "-"
    filelist = [ f for f in os.listdir(caminho)]

    for f in filelist:
        os.remove(os.path.join(caminho, f))    
        
def EscreveTerminal(mensagem):
    data = datetime.now() 
    dia = data.strftime("%d")
    mes = data.strftime("%m")
    ano = data.strftime("%Y")
    dataFormatada = '{}/{}/{}'.format(dia, mes, ano)
    
    hora = data.strftime("%H")
    minuto = data.strftime("%M")
    segundo = data.strftime("%S")
    horaFormatada = '{}:{}:{}'.format(hora, minuto, segundo)
        
    texto = f'{dataFormatada} {horaFormatada} - {mensagem}'
    print(texto) 

def Log(arquivo, mensagem):
    fileLog = open(arquivo, 'r')
    conteudo = fileLog.readlines()
    conteudo.append(f'\n {mensagem}')
    fileLog = open(arquivo, 'w')
    fileLog.writelines(conteudo)
    fileLog.close()     
    
def RegistraAcao (mensagem, arquivoLog):
    data = datetime.now() 
    dia = data.strftime("%d")
    mes = data.strftime("%m")
    ano = data.strftime("%Y")
    dataFormatada = '{}/{}/{}'.format(dia, mes, ano)
    
    hora = data.strftime("%H")
    minuto = data.strftime("%M")
    segundo = data.strftime("%S")
    horaFormatada = '{}:{}:{}'.format(hora, minuto, segundo)
    
    msgLog = f'{dataFormatada} {horaFormatada} - {mensagem}'
    
    EscreveTerminal(mensagem)
    Log(arquivoLog, msgLog)          

class Error(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)
      
def CriaPasta(caminho, arquivoLog):
    try:
        # Verifica se o diretório não existe
        if not os.path.exists(caminho):
            # Cria o diretório
            os.makedirs(caminho)
            mensagem = f"Pasta '{caminho}' criada com sucesso!"
            RegistraAcao (mensagem, arquivoLog)       
        else:
            mensagem = f"A pasta '{caminho}' já existe."
            RegistraAcao (mensagem, arquivoLog)       
    except Exception as e:
        mensagem = f"Erro ao criar a pasta '{caminho}': {e}"
        RegistraAcao (mensagem, arquivoLog)
        
def VerificarArquivo(caminho_arquivo, arquivoLog):
    if os.path.exists(caminho_arquivo):
        return True
    else:
        return False   
        
def ApagarArquivo(caminho_arquivo, arquivoLog):
    if VerificarArquivo(caminho_arquivo, arquivoLog):
        os.remove(caminho_arquivo) 
          
def TrataTelefone (telefone):
    numeros = "1,2,3,4,5,6,7,8,9,0"

    telefone = telefone.replace("+55 ", "")
    telefone = telefone.replace("(", "")
    telefone = telefone.replace(")", "")
    telefone = telefone.replace(" ", "")
    telefone = telefone.replace("-", "")
    telefone = telefone.split("/")  
    telefone = telefone[0]
    
    for posicao in telefone:
        if posicao not in numeros:
            telefone = telefone.replace(posicao, "")
            
    return telefone      
                  
def formatarValorReal(valor):
    valor = '{:,.2f}'.format(float(valor))
    valor = valor.replace(',','v')
    valor = valor.replace('.',',')    
    valor = valor.replace('v','.')
    return valor  

def RenomeaArquivo (nomeAntigo, nomeNovo):
    os.rename(nomeAntigo, nomeNovo)
    
def MoverArquivo (origem, destino):
    try:
        # Verifica se a pasta de origem existe
        if not os.path.exists(origem):
            print(f"A pasta de origem {origem} não existe.")
            return
                
        shutil.move(origem, destino)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    
def LimparConsole():
    os.system('cls')


def AjustaData(periodo):
    periodo = int(periodo)
    data = datetime.now() + timedelta(days=periodo)
    dia = data.strftime("%d") # Somente dia
    mes = data.strftime("%m") # Somente mês
    ano = data.strftime("%Y") # Somente ano
    return '{}/{}/{}'.format(dia, mes, ano)    