import mysql.connector


cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaulacaio.mysql.database.azure.com",
    port=3306,
    database="escolasenac"
)

cursor = cnx.cursor()
print("sistema de cadastro")
usuarionovo = input("digite o seu usuario desejado: ")
senhanova = input("digite sua senha para integrar ao usuario: ")

# Consulta de parametrização, agora considerando a faixa de idades
query = "insert into usuario_secretaria (usuario,senha ) values (%s, %s);"
cursor.execute(query,(usuarionovo, senhanova,))
cnx.commit 


# Fechando o cursor e a conexão
cursor.close()
cnx.close()