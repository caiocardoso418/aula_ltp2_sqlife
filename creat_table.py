import sqlite3

conexao = sqlite3.connect("mercado.db")
cursor = conexao.cursor()

sql = ''' create table IF NOT EXISTS tb_funcionarios(
          id integer primary key,
          nome text not null,
          cpf integer not null,
          telefone text not null,
          sexo text null,
          idade text null)
'''
cursor.execute(sql)
cursor.close
conexao.close
print("FECHADO A BASE DE DADOS")