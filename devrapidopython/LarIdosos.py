import tkinter
import webbrowser
import hashlib
import sqlite3
from tkinter import messagebox as mb
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk

root = tkinter.Tk()
root.geometry("200x300")
root.title("Login")
root.resizable(False, False)

connection = sqlite3.connect("login.db")
cursor = connection.cursor()

def callback(url):
   webbrowser.open_new_tab(url)

def funclogin():
    login = str(EntradaCPF.get())
    tentalogin = cursor.execute(f"SELECT nome FROM Abrigo WHERE cpf = {login}").fetchall()
    mb.showinfo("Sucesso", "Bem-vindo.")
    telaprincipal()


def funcregistro():
    limpartela()
    label = tkinter.Label(root, text="Registro")
    label.pack()

    label = tkinter.Label(root, text="  Nome", anchor="w")
    label.pack(fill='both')
    global RegistroNome
    global RegistroCPF
    RegistroNome = tkinter.Entry(root, width=30)
    RegistroNome.pack()
    label = tkinter.Label(root, text="  CPF", anchor="w")
    label.pack(fill='both')
    RegistroCPF = tkinter.Entry(root, width=30)
    RegistroCPF.pack()

    botaoregistrosql = tkinter.Button(root, text="Registrar",command=lambda: funcregistroSQL())
    botaoregistrosql.pack()

def funcregistroSQL():
    inputregnome = str(RegistroNome.get())
    inputregcpf = str(RegistroCPF.get())
    cursor.execute(f"INSERT INTO Abrigo VALUES ('{inputregnome}', '{inputregcpf}', 0)")
    connection.commit()
    mb.showinfo("Sucesso", "Seu cadastro foi feito com sucesso. :)")
    telalogin()


def limpartela():
    for tirar in root.winfo_children():
        tirar.destroy()

def telalogin():
    limpartela()
    label = tkinter.Label(root, text="\n\n")
    label.pack()

    label = tkinter.Label(root, text="  CPF", anchor="w")
    label.pack(fill='both')
    global EntradaCPF
    EntradaCPF = tkinter.Entry(root, width=30)
    EntradaCPF.pack()

    botaologin = tkinter.Button(root, text="Entrar",command=lambda: funclogin())
    botaologin.pack()

    label = tkinter.Label(root, text="\n\n")
    label.pack()

    botaoregistro = tkinter.Button(root, text="Registrar",command=lambda: funcregistro())
    botaoregistro.pack()

    label = tkinter.Label(root, text="\n")
    label.pack()

def telaprincipal():
        # Funções de banco de dados
    def connect_to_db(db_name):
        """Conecta ao banco de dados SQLite e retorna a conexão."""
        conn = sqlite3.connect(db_name)
        return conn

    def create_table(conn):
        """Cria a tabela 'perguntas' se não existir."""
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS perguntas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pergunta TEXT NOT NULL,
                resposta1 TEXT
                
            )
        ''')
        conn.commit()

    def insert_data(conn, pergunta, resposta1):
        """Insere dados na tabela 'perguntas'."""
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO perguntas (pergunta, resposta1)
            VALUES (?, ?)
        ''', (pergunta, resposta1))
        conn.commit()

    def query_data(conn):
        """Consulta todos os dados da tabela 'perguntas'."""
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM perguntas')
        rows = cursor.fetchall()
        return rows

    # Funções da interface gráfica
    def submit():
        """Lê os dados dos campos e insere no banco de dados."""
        pergunta = pergunta_entry.get()
        resposta1 = resposta1_entry.get()
        #resposta2 = resposta2_entry.get()
        #resposta3 = resposta3_entry.get()
        
        if not pergunta or not resposta1:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos")
            return

        conn = connect_to_db('example.db')
        insert_data(conn, pergunta, resposta1)
        conn.close()
        update_table()

    def update_table():
        """Atualiza o conteúdo da tabela na interface gráfica com dados do banco de dados."""
        conn = connect_to_db('example.db')
        rows = query_data(conn)
        conn.close()
        
        for row in tree.get_children():
            tree.delete(row)
            
        for row in rows:
            tree.insert('', 'end', values=row)

    # Configuração da interface gráfica
    root = tk.Tk()
    root.title("Cadastro de Perguntas")

    # Conectar e criar tabela no banco de dados
    conn = connect_to_db('example.db')
    create_table(conn)
    conn.close()

    # Layout da interface
    tk.Label(root, text="Pergunta").grid(row=0, column=0, padx=10, pady=5)
    pergunta_entry = tk.Entry(root, width=50)
    pergunta_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Resposta 1").grid(row=1, column=0, padx=10, pady=5)
    resposta1_entry = tk.Entry(root, width=50)
    resposta1_entry.grid(row=1, column=1, padx=10, pady=5)

    #tk.Label(root, text="Resposta 2").grid(row=2, column=0, padx=10, pady=5)
    #resposta2_entry = tk.Entry(root, width=50)
    #resposta2_entry.grid(row=2, column=1, padx=10, pady=5)

    #tk.Label(root, text="Resposta 3").grid(row=3, column=0, padx=10, pady=5)
    #resposta3_entry = tk.Entry(root, width=50)
    #resposta3_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Button(root, text="Submit", command=submit).grid(row=4, column=0, columnspan=2, pady=10)

    # Tabela para exibir dados
    columns = ("ID", "Pergunta", "Resposta 1")
    tree = ttk.Treeview(root, columns=columns, show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Pergunta", text="Pergunta")
    tree.heading("Resposta 1", text="Resposta 1")
    #tree.heading("Resposta 2", text="Resposta 2")
    #tree.heading("Resposta 3", text="Resposta 3")

    tree.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    update_table()

    root.mainloop()

telalogin()
root.iconify() #Minimiza a tela
root.update()
root.deiconify() #Maximiza a tela
root.mainloop()  #loop principal, impede o código de seguir e permite capturar inputs
