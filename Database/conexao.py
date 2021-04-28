import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'banco_python'
)

cursor = conexao.cursor()
print(conexao)

#CREATE DATABASE
'''cursor.execute('create database ')

cursor.execute('show databases')
for x in cursor:
    print(x)
#CREATE TABLE
cursor.execute('create table aluno(cod_aluno int(10) primary key AUTO_INCREMENT, nome varchar(40) not null, \
idade int(3), email varchar(50))')

cursor.execute('show tables')
for a in cursor:
    print(a)
]
#INSERT
sql = 'INSERT into aluno (nome, idade, email) values ("Gabriel", "27", "gabriel.teste@gmail.com")'
cursor.execute(sql)
conexao.commit()
print(cursor.rowcount, 'registro(s) inserido(s)')

#INSERT em multiplas linhas
sql = 'INSERT into aluno (nome, idade, email) values(%s, %s, %s)'
val = [
    ("Daiana", "28", "teste1@gmail.com"),
    ("Lucas", "25", "teste2@gmail.com"),
    ("Vitor", "21", "teste3@gmail.com"),
    ("Josiane", "29", "teste4@gmail.com"),
    ("Amanda", "33", "teste5@gmail.com"),
    ("Alessandra", "22", "teste6@gmail.com"),
    ("Lorenna", "35", "teste7@gmail.com")
]

cursor.executemany(sql, val)
conexao.commit()
print(cursor.rowcount, 'registro(s) inserido(s)')

#DELETE
sql = 'DELETE from aluno where nome = "Lorenna"'
cursor.execute(sql)
conexao.commit()
print(cursor.rowcount, 'Registo(s) deletado(s)')


#Apagar a tabela inteira
cursor.execute('drop table aluno')


#UPDATE
sql = 'UPDATE aluno set nome = "Gabriel da Silva Carvalho" where cod_aluno = 2'
cursor.execute(sql)
conexao.commit()
print(cursor.rowcount, 'Registo(s) atualizados(s)')


#UPDATE ALTERNATIVO
sql = 'UPDATE aluno set nome = %s where cod_aluno = %s'
cursor.execute(sql,('Vitor Taffarel', 5))
conexao.commit()
print(cursor.rowcount, 'Registo(s) atualizado(s)')

#SELECT
cursor.execute('SELECT * from aluno')
result = cursor.fetchall()
for x in result:
    print(x)


#SELECT com condição
cursor.execute('SELECT nome from aluno where idade > 25')
result = cursor.fetchall()
for x in result:
    print(x)
'''