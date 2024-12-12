import mysql.connector


cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaulacaio.mysql.database.azure.com",
    port=3306,
    database="escolasenac"
)

cursor = cnx.cursor()

# Obtendo as idades e convertendo para inteiros
idade_menor = (input("Digite a menor idade: "))
idade_maior = (input("Digite a maior idade: "))

# Consulta de parametrização, agora considerando a faixa de idades
query = "SELECT nome, idade, idturma,alergias FROM aluno WHERE idade BETWEEN %s AND %s;"
cursor.execute(query, (idade_menor, idade_maior))

# Recuperando os resultados
resultados = cursor.fetchall()
if resultados:
    for nome, idade, idturma, alergias in resultados:
        if (alergias != "leite"):
            print(f"Nome: {nome}, Idade: {idade}, Turma: {idturma}")

# Fechando o cursor e a conexão
cursor.close()
cnx.close()
