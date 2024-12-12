import mysql.connector



def get_database_connection():
    try:
        cnx = mysql.connector.connect(
            host="exemploaulacaio.mysql.database.azure.com",
            port=3306,
            username="python",
            password="aula@123",
            database="escolasenac"
        )
        return cnx
    except mysql.connector.Error as err:
        print(f"Erro de conexão: {err}")
        return None


def registrar_usuario():
    try:
        
        cnx = get_database_connection()
        if not cnx:
            return

        cursor = cnx.cursor()

        
        usuario = input("Digite o nome do usuário: ")
        senha = input("Digite a senha: ") 

        
        query = """
        INSERT INTO usuario_secretaria (usuario, senha) 
        VALUES (%s, %s)
        """

        try:
            
            cursor.execute(query, (usuario, senha))
            cnx.commit()
            print("\nUsuário cadastrado com sucesso!")
        except mysql.connector.Error as err:
            print(f"\nErro ao cadastrar usuário: {err}")
            cnx.rollback()

        
        cursor.close()
        cnx.close()

    except Exception as e:
        print(f"Erro inesperado: {e}")


def fazer_login():
    try:
        
        cnx = get_database_connection()
        if not cnx:
            return False

        cursor = cnx.cursor()

        
        usuario = input("Digite o nome do usuário: ")
        senha = input("Digite a senha: ")  

        
        query = """
        SELECT * FROM usuario_secretaria 
        WHERE usuario = %s AND senha = %s
        """

        try:
            
            cursor.execute(query, (usuario, senha))
            resultado = cursor.fetchone()

            if resultado:
                print("\nLogin realizado com sucesso!")
                return True
            else:
                print("\n Usuário ou senha inválidos.")
                return False

        except mysql.connector.Error as err:
            print(f"\nErro durante o login: {err}")
            return False

        finally:
            
            cursor.close()
            cnx.close()

    except Exception as e:
        print(f"Erro inesperado: {e}")
        return False


def menu_principal():
    while True:
        print("\n==== SISTEMA DE GESTÃO ====")
        print("1. Registrar Usuário")
        print("2. Fazer Login")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            registrar_usuario()
        elif escolha == '2':
            fazer_login()
        elif escolha == '3':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu_principal()