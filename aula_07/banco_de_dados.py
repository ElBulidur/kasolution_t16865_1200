

import mysql.connector


def pegar_conexao():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="kasolution"
        )

        # print("Conexão estabelecida com sucesso.")
        return conn

    except mysql.connector.Error as e:
        print(f"Erro na conexão: {e}")


# CRUD => CREATE(Criar), READ(Ler), UPDATE(Atualizar) e DELETE(Deletar)

#CREATE
dados = ["Julio", "julio@gmail.com"]

def cadastrar_aluno(nome, email):

    conn = pegar_conexao()

    sql = "INSERT INTO alunos(nome, email) VALUES (%s, %s)"

    cursor = conn.cursor()

    cursor.execute(sql, [nome, email])

    conn.commit()

    conn.close()

    print("Aluno cadastrado com sucesso!")


# cadastrar_aluno("Ana", "ana@email.com")


def pegar_alunos():
    conn = pegar_conexao()

    sql = "SELECT * FROM alunos"

    cursor = conn.cursor()

    cursor.execute(sql)

    # for registro in cursor:
    #     print(registro)

    for id, nome, email in cursor:
        print(f"O aluno do id {id}, com nome {nome} e email {email}")

    conn.close()

dados = ["Julio Novo", "julio_novo@email.com"]

def atualizar_aluno(dados, id):

    conn = pegar_conexao()

    sql = "UPDATE alunos SET nome=%s, email=%s WHERE id=%s"

    cursor = conn.cursor()

    cursor.execute(sql, [dados[0], dados[1], id])

    conn.commit()

    conn.close()

    print("Aluno atualizado com sucesso!")