CEUB - FATECS
Bacharelado em Ciência da Computação - BCC
Linguagem e Técnicas de Programação II - Prof. Barbosa


- Avaliação prática individual 4


- Prazo para entrega no Moodle: 10/10, até 23h59


- Envio:
Envie os arquivos na sala on-line da disciplina.


- Resolva os programas usando a linguagem de programação Python e o banco de dados SQLite.


- Implemente:

1. Desenvolva um programa em Python para criar uma base de dados com o SQLite e uma tabela com uma chave primária, pelo menos uma coluna obrigatória e pelo menos duas colunas opcionais.

2. Implemente um programa em Python para inserir dados na tabela criada.

3. Faça um programa em Python para consultar os registros inseridos na tabela criada. Mostre os registros na vertical. E inclua a mensagem de “Tabela vazia.”

Obs.: crie a tabela e as colunas diferentes das desenvolvidas nas aulas.



	
Obs.: atenção, entregue a avaliação prática dentro do prazo definido acima.

Prof. Barbosa.

------------------------------------------------------------------------------------------------------

CEUB - FATECS
Bacharelado em Ciência da Computação - BCC
Banco de Dados em Python com SQLite
Linguagem e Técnicas de Programação II - Prof. Barbosa

SQLite3

Uma biblioteca em linguagem C que implementa um banco de dados SQL embutido.

Programas que usam a biblioteca SQLite podem ter acesso a banco de dados SQL sem executar um processo SGBD separado.

Não é uma biblioteca cliente usada para conectar com um grande servidor de banco de dados, mas sim o próprio servidor.

A biblioteca SQLite lê e escreve diretamente no arquivo de banco de dados no disco.

- Passos para implementação em Python e acesso a banco de dados SQLite:

1°) Importe a biblioteca sqlite3
import sqlite3

2°) Cria o banco de dados e faz a conexão com o banco de dados
database = "nome_database.db"				# Solução 1
conexao = sqlite3.connect(database)

conexao = sqlite3.connect("nome_database.db")		# Solução 2
Obs.: se o banco de dados não existir o Python cria um novo banco.

3°) Crie um cursor:
cursor = conexao.cursor()
Obs.: o cursor é usado para executar os comandos SQL dentro do programa Python.

4°) Crie uma tabela
- Sintaxe:
sql = ''' create table tb_nome_tabela(
        nome_coluna1 tipo primary key,
        nome_coluna2 tipo not null,			# Obrigatório
        nome_coluna3 tipo [null]) '''			# Opcional
Obs.:
Os colchetes [ ] dentro de uma sintaxe em TI, significa a parte opcional do comando

cursor.execute(sql)                    			# Executa o comando sql

4°) Crie uma tabela, faça um banco de álbum de músicas.
- Exemplo 1:
sql =""" CREATE TABLE tb_nome_tabela			# Solução 1
                 	(nome_coluna tipo primary key, 
artist text not null, 		# Obrigatório
release_date text null, 	# Opcional
publisher text, 
media_type text)  """
cursor.execute(sql)
- Exemplo 2:
cursor.execute(""" CREATE TABLE tb_nome_tabela		# Solução 2
                 	(nome_coluna tipo primary key, 
artist text not null, 
release_date text null, 
publisher text, 
media_type text)  """)

5°) Insira dados no banco (insert)
sql = ””” INSERT INTO tb_nome_tabela 				# Solução 1
                VALUES ('Glow', 'Andy Hunter', '7/24/2012', 'Xplore Records', 'MP3') ”””
cursor.execute(sql)

cursor.execute("INSERT INTO tb_nome_tabela 			# Solução 2
VALUES ('Glow', 'Andy Hunter', '7/24/2012', 'Xplore Records', 'MP3')")

Obs.: não se salva dados num banco, mas os dados persistem. 
Use o seguinte comando para persistir os dados no banco:
conexao.commit()


Prof. Barbosa
