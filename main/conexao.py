import psycopg2

class Conexao(object):
    def __init__(self):
        # Conexão Máquina Local
        try:
            self.db = psycopg2.connect(
                host="192.168.1.183",
                user="postgres",
                password="150215",
                dbname="gestao"
            )
            # print("Conexão bem-sucedida!")
        except Exception as e:
            print(f"Erro na conexão: {e}")

    def gravar(self, sql):
        try:
            cur = self.db.cursor()
            cur.execute(sql)
            self.db.commit()
            cur.close()
        except Exception as e:
            print(f"Erro ao executar gravação: {e}")
            return False
        return True

    def consultar(self, sql):
        rs = None
        try:
            cur = self.db.cursor()
            cur.execute(sql)
            rs = cur.fetchone()
            cur.close()
        except Exception as e:
            print(f"Erro ao consultar: {e}")
            return None
        return rs

    def consultar_tree(self, sql, params=None):
        rs = None
        try:
            cur = self.db.cursor()
            cur.execute(sql, params)
            rs = cur.fetchall()
            cur.close()
        except Exception as e:
            print(f"Erro ao consultar (tree): {e}")
            return None
        return rs

    def fechar(self):
        self.db.close()

# # Exemplo de uso
# if __name__ == "__main__":
#     conn = Conexao()
#     sql_insert = "INSERT INTO sua_tabela (coluna1, coluna2) VALUES (valor1, valor2)"
#     if conn.gravar(sql_insert):
#         print("Dados inseridos com sucesso!")
#     else:
#         print("Falha ao inserir dados.")
    
#     sql_select = "SELECT * FROM sua_tabela"
#     resultado = conn.consultar_tree(sql_select)
#     if resultado:
#         for linha in resultado:
#             print(linha)
#     else:
#         print("Nenhum dado encontrado.")
    
#     conn.fechar()
