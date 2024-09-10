import hashlib
import sqlite3
db = sqlite3.connect("db.db")
cursor = db.cursor()
cursor.execute(f"CREATE TABLE IF NOT EXISTS Alunos (Aluno TEXT, Matricula INTEGER, CPF TEXT, Curso TEXT, Periodo INTEGER)")

def AdicionarAluno(Tabela, Aluno, Matricula, CPF, Curso, Periodo):
    cursor.execute(f"INSERT INTO {Tabela} VALUES ('{Aluno}', {Matricula}, '{CPF}', '{Curso}', '{Periodo}')")
    print(f"{Aluno} adicionado na tabela '{Tabela}' com sucesso.")

def BuscarAluno(NomeMatricula):
    busca = cursor.execute(f"SELECT * FROM Alunos WHERE Aluno LIKE '{NomeMatricula}' OR Matricula LIKE '{NomeMatricula}'").fetchall()
    print(busca)

AdicionarAluno("Alunos", "João", "10001", "184184184-18", "CienciaComputacao", "3")
AdicionarAluno("Alunos", "Maria", "10002", "184184184-18", "ADS", "4")

BuscarAluno("João")