import mysql.connector


cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaulacaio.mysql.database.azure.com",
    port=3306,
    database="escolasenac"
)

cursor = cnx.cursor()
idade= input("digite a idade para buscar: ")


#consulta de parametrização
query = "SELECT nome, CPF FROM aluno WHERE idade =%s;"
cursor.execute(query,(idade,))

resultados = cursor.fetchall()
if resultados:
    for cpf, endereco, in resultados:
        print(f"cpf:{cpf} idade:{idade}, endereco: {endereco}")

else: 
    print("nunhum aluno encontrado encontrado com esse nome")

    cursor.close()
    cnx.close()