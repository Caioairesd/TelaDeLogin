import mysql.connector #Importa conector para poder realizar conexão com banco de dados

class Database:
    def __init__(self):
    #Conceta ao banco de dados MySql com as credenciais fornecidas
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "caiosilva_db",
        )

        self.cursor = self.conn.cursor() #Cria um cursor para executar comandos SQL
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS usuario1(
                idUsuario INT AUTO_INCREMENT PRIMARY KEY,
                nome TEXT(255), 
                email TEXT(255), 
                usuario TEXT(255), 
                senha TEXT(255)
             );""")
        self.conn.commit()

        print("Conectando ao banco de dados...")

    def RegistrarNoBanco(self,nome,email,usuario,senha):
        self.cursor.execute("INSERT INTO usuario1 (nome,email,usuario,senha)VALUES(%s,%s,%s,%s)",(nome,email,usuario,senha))#Insere os dados do usuário na tabela
        self.conn.commit() #Confirma a inserção dos dados

    def Alterar(self,idUsuario,nome,email,usuario,senha):
        self.cursor.execute("UPDATE usuario1 SET nome = %s,email = %s,usuario = %s,senha = %s WHERE idUsuario =%s",(nome,email,usuario,senha,idUsuario)) #Atualiza o usuário com o id fornecido
        self.conn.commit()

    def Excluir(self,idUsuario):
        self.cursor.execute("DELETE FROM usuario1 WHERE idUsuario = %s ",(idUsuario,))
        self.conn.commit()
        
    def buscar(self,idUsuario):
        self.cursor.execute("SELECT * FROM usuario1 WHERE idUsuario = %s",(idUsuario,))
        return self.conn.fetchone()
    
    def __del__(self):
        self.conn.close()


                        
