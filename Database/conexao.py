import mysql.connector

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'gabriel061294',
    database = 'banco_python'
)

cursor = conexao.cursor()
print(conexao)

'''cursor.execute('create database ')

cursor.execute('show databases')
for x in cursor:
    print(x)

cursor.execute('create table aluno(cod_aluno int(10) primary key AUTO_INCREMENT, nome varchar(40) not null, \
idade int(3), email varchar(50))')

cursor.execute('show tables')
for a in cursor:
    print(a)'''