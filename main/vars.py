import os
from datetime import datetime, timedelta

# Variáveis de Datas
# Data Atual
dtAtual = datetime.now() 
diaAtual = dtAtual.strftime("%d")
mesAtual = dtAtual.strftime("%m")
anoAtual = dtAtual.strftime("%Y")
horaAtual = dtAtual.strftime("%H")
minutoAtual = dtAtual.strftime("%M")
segundoAtual = dtAtual.strftime("%S")
dtLog = '{}/{}/{} {}:{}:{}'.format(diaAtual, mesAtual, anoAtual, horaAtual, minutoAtual, segundoAtual)
dtAtualFormatadaTela = '{}/{}/{}'.format(diaAtual, mesAtual, anoAtual)
dtAtualFormatadaArquivo = '{}-{}-{}'.format(diaAtual, mesAtual, anoAtual)                                        
horaAtualFormatadaTela = '{}:{}:{}'.format(horaAtual, minutoAtual, segundoAtual)
horaAtualFormatadaArquivo = '{}-{}-{}'.format(horaAtual, minutoAtual, segundoAtual)

# Data Anterior
dtAnterior = datetime.now() + timedelta(days=-1) # Subtrai um dia 
diaAnterior = dtAnterior.strftime("%d%m%y") # Formata data
fdia = dtAnterior.strftime("%d") # Dia anterior somente dia
fmes = dtAnterior.strftime("%m") # Mes somente mês
fano = dtAnterior.strftime("%Y") # Ano somente ano
dtOntem = '{}/{}/{}'.format(fdia, fmes, fano)

# Data Amanhã
dtM1 = datetime.now() + timedelta(days=+1) # Soma um dia 
diaAnterior = dtM1.strftime("%d%m%y") # Formata data
fdiaM1 = dtM1.strftime("%d") # Somente dia
fmesM1 = dtM1.strftime("%m") # Somente mês
fanoM1 = dtM1.strftime("%Y") # Somente ano
dtAmanha = '{}/{}/{}'.format(fdiaM1, fmesM1, fanoM1)

# Data Quinzena
dtQuinzena = datetime.now() + timedelta(days=+15) # Adiciona 15 Dias 
diaQuinzena = dtQuinzena.strftime("%d%m%y") # Formata data
qdia = dtQuinzena.strftime("%d") # Dia anterior somente dia
qmes = dtQuinzena.strftime("%m") # Mes somente mês
qano = dtQuinzena.strftime("%Y") # Ano somente ano
dtQuinzena = '{}/{}/{}'.format(qdia, qmes, qano)

# Data Dia +3
dt_3 = datetime.now() + timedelta(days=+3) # Soma 3 Dias 
qdia_3 = dt_3.strftime("%d") # Somente dia
qmes_3 = dt_3.strftime("%m") # Somente mês
qano_3 = dt_3.strftime("%Y") # Somente ano
dtMais3 = '{}/{}/{}'.format(qdia_3, qmes_3, qano_3)

# Data Dia -3
dtM3 = datetime.now() + timedelta(days=-3) # Exclui 3 Dias 
qdia = dtM3.strftime("%d") # Dia anterior somente dia
qmes = dtM3.strftime("%m") # Mes somente mês
qano = dtM3.strftime("%Y") # Ano somente ano
dtMenos3 = '{}/{}/{}'.format(qdia, qmes, qano)

# Primeiro dia do mês atual
dt_Inicio_Mes = datetime(dtAtual.year, dtAtual.month, 1)
diaInicio_Mes = dt_Inicio_Mes.strftime("%d%m%y") # Formata data
idia = dt_Inicio_Mes.strftime("%d") # Dia anterior somente dia
imes = dt_Inicio_Mes.strftime("%m") # Mes somente mês
iano = dt_Inicio_Mes.strftime("%Y") # Ano somente ano
dtInicio_Mes = '{}/{}/{}'.format(idia, imes, iano)

# -- Variáveis de Caminhos ---    ############################
caminhoInstalacao = os.getcwd() + "\\"
caminhoAplicacao = f"{caminhoInstalacao}OficialGestor\\"
caminhoArquivos = caminhoAplicacao.replace(r'/', "\\") + 'arquivos\\'
caminhoImagens = caminhoInstalacao.replace(r'/', "\\") + 'imagens\\'


QuebraLinha = "\n"

nome_aplicacao = "Gestor de Aplicações 1.0"  
celular_suporte = "62 9 8322-0264"
email_suporte = "ti@oficialsport.com.br"


