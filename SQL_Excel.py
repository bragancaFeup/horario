# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2021)
#objective: SQL 2 Excel and Excel 2 SQL

"""""
import pandas as pd
import sqlite3

# ler uma tabela SQL para uma pandas dataframe
def SQLTable2df(baseDados,tabela):
    conexao = sqlite3.connect(baseDados)
    df = pd.read_sql_query("SELECT * from " + tabela, conexao)  
    conexao.close()
    return df
    

# Escrever pandas dataframe numa tabela SQL
def df2SQL(df,baseDados,tabela):
    conexao = sqlite3.connect(baseDados)
    df.to_sql(tabela, conexao, if_exists="replace")  
    conexao.close()

# escrever uma uma pandas dataframe num ficheiro Excel
def pd2Excel(df,excelfile,sheetname):
    with pd.ExcelWriter(excelfile) as writer:
        df.to_excel(writer, sheet_name=sheetname, index=False)

# escrever várias pandas dataframe num ficheiro Excel em diferentes folhas
def dfs2Excel(dfs,excelfile):
    with pd.ExcelWriter(excelfile) as writer:
        for dft in dfs:
            dft[0].to_excel(writer, sheet_name=dft[1], index=False)
        
# Ler folha Excel para  pandas dataframe
def sheet2pd(excelfile,sheetname):
    df = pd.read_excel(excelfile,sheet_name=sheetname, index_col=0)
    return df

#%%

baseDados = 'data/horario.db'
#%%
#Copiar uma tabela do SQL para o Excel

df = SQLTable2df(baseDados,"Docentes")
pd2Excel(df,"dataImp/Docentes.xlsx","Docentes")

#%%
# Obter o nome das tabelas do SQL

tabela = "sqlite_schema"
temp =SQLTable2df(baseDados,tabela)
tabelas = temp[temp.type == 'table']['name']
#print(tabelas)
for tabelaname in tabelas:
    print(tabelaname)
    
#%%
#Copiar todas as tabelas do SQL para um ficheiro Excel com várias folhas

dfs = []

tabela = "sqlite_schema"
temp =SQLTable2df(baseDados,tabela)
tabelas = temp[temp.type == 'table']['name']
for tabelaname in tabelas:
    df =SQLTable2df(baseDados,tabelaname)
    dfs.append([df,tabelaname])
    
dfs2Excel(dfs,"dataimp/todastabelas.xlsx")

#%%
# Copiar tabela do Excel para SQL

df = sheet2pd("dataimp/todastabelasparaSQL.xlsx","Docentes")
df2SQL(df,baseDados,"Docentes")

