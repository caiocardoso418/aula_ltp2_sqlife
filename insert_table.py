import sqlite3

conexao = sqlite3.connect("mercado.db")
cursor = conexao.cursor()

def inserir_funcionario(id, nome, cpf, telefone, sexo=None, idade=None):
    cursor.execute('''
    INSERT INTO funcionarios (id, nome, cpf, telefone, sexo, idade)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (id, nome, cpf, telefone, sexo, idade))
    conexao.commit()
    print(f"Funcionário {nome} inserido com sucesso.")

inserir_funcionario = (82, 'Caio Peliz', 8427495622, 998002705)


cursor.close
conexao.close
print("FECHOU O BANCO DE DADOS")

