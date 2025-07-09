import os
import tkinter as tk
from tkinter import ttk, messagebox

def inicializar_arquivos():
    if not os.path.exists("usuarios.txt"):
        open("usuarios.txt", "w").close()
    if not os.path.exists("livros.txt"):
        open("livros.txt", "w").close()


def cadastrar_usuario(matricula, nome, senha):
    with open("usuarios.txt", "r") as f:
        for linha in f:
            if matricula == linha.split(",")[0]:
                return False 
    with open("usuarios.txt", "a") as f:
        f.write(f"{matricula},{nome},{senha}\n")
    return True

def validar_login(matricula, senha):
    with open("usuarios.txt", "r") as f:
        for linha in f:
            dados = linha.strip().split(",")
            if dados[0] == matricula and dados[2] == senha:
                return dados[1]  
    return None

def obter_livros(matricula):
    livros = []
    with open("livros.txt", "r") as f:
        for linha in f:
            dados = linha.strip().split(",")
            if dados[0] == matricula:
                livros.append(dados[1:])  
    return livros

def adicionar_livro(matricula, nome_do_livro, autor, codigo):
    with open("livros.txt", "a") as f:
        f.write(f"{matricula},{nome_do_livro},{autor},{codigo}\n")    


def tela_inicial():
    def abrir_tela_cadastro():
        janela_inicial.destroy()
        tela_cadastro()

    def abrir_tela_login():
        janela_inicial.destroy()
        tela_login()

    janela_inicial = tk.Tk()
    janela_inicial.title("Biblioteca - Início")
    janela_inicial.geometry("400x300")
    janela_inicial.configure(bg="#f0f0f0")

    ttk.Label(janela_inicial, text="Sistema da Biblioteca", font=("Helvetica", 16, "bold"), background="#f0f0f0").pack(pady=40)

    ttk.Button(janela_inicial, text="Cadastro", command=abrir_tela_cadastro).pack(pady=10)
    ttk.Button(janela_inicial, text="Login", command=abrir_tela_login).pack(pady=10)

    janela_inicial.mainloop()


def tela_cadastro():
    def realizar_cadastro():
        matricula = entrada_matricula.get()
        nome = entrada_nome.get()
        senha = entrada_senha.get()
        if matricula and nome and senha:
            try:
                matricula = int(matricula)
                if cadastrar_usuario(matricula, nome, senha):
                    messagebox.showinfo("Sucesso", "Usuário cadastrado!")
                    janela_cadastro.destroy()
                    tela_inicial()
                else:
                    messagebox.showerror("Erro", "Usuário já existe!")
            except ValueError:
                messagebox.showerror("ERRO", "Apenas números são permitidos na matrícula.")
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
    janela_cadastro = tk.Tk()
    janela_cadastro.title("Cadastro de Usuário")
    janela_cadastro.geometry("400x400")
    janela_cadastro.configure(bg="#f0f0f0")

    ttk.Label(janela_cadastro, text="Cadastro de Usuário", font=("Helvetica", 16, "bold"), background="#f0f0f0").pack(pady=20)

    frame_cadastro = ttk.Frame(janela_cadastro, padding=20)
    frame_cadastro.pack(pady=20)

    ttk.Label(frame_cadastro, text="Digite sua Matrícula:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entrada_matricula = ttk.Entry(frame_cadastro, width=30)
    entrada_matricula.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(frame_cadastro, text="Diga seu Nome:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entrada_nome = ttk.Entry(frame_cadastro, width=30)
    entrada_nome.grid(row=1, column=1, padx=5, pady=5)

    ttk.Label(frame_cadastro, text="Crie uma Senha:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    entrada_senha = ttk.Entry(frame_cadastro, width=30, show="*")
    entrada_senha.grid(row=2, column=1, padx=5, pady=5)

    ttk.Button(janela_cadastro, text="Cadastrar", command=realizar_cadastro).pack(pady=20)

    janela_cadastro.mainloop()


def tela_login():
    def realizar_login():
        matricula = entrada_matricula.get()
        senha = entrada_senha.get()
        nome_usuario = validar_login(matricula, senha)
        if nome_usuario:
                janela_login.destroy()
                tela_usuario(matricula, nome_usuario)
        else:
            messagebox.showerror("Erro", "Matrícula ou senha incorretas!")

    janela_login = tk.Tk()
    janela_login.title("Login")
    janela_login.geometry("400x300")
    janela_login.configure(bg="#f0f0f0")

    ttk.Label(janela_login, text="Login na Biblioteca", font=("Helvetica", 16, "bold"), background="#f0f0f0").pack(pady=20)

    frame_login = ttk.Frame(janela_login, padding=20)
    frame_login.pack(pady=20)

    ttk.Label(frame_login, text="Matrícula:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entrada_matricula = ttk.Entry(frame_login, width=30)
    entrada_matricula.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(frame_login, text="Senha:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entrada_senha = ttk.Entry(frame_login, width=30, show="*")
    entrada_senha.grid(row=1, column=1, padx=5, pady=5)

    ttk.Button(janela_login, text="Login", command=realizar_login).pack(pady=20)

    janela_login.mainloop()


def tela_usuario(matricula, nome_usuario):
    def atualizar_lista():
        lista_livros.delete(*lista_livros.get_children())
        livros = obter_livros(matricula)
        for livro in livros:
            lista_livros.insert("", "end", values=(livro[0], livro[1], livro[2]))

    def adicionar_novo_livro():
        nome = entrada_nome_livro.get()
        autor = entrada_autor.get()
        codigo = entrada_codigo.get()
        if nome and autor and codigo:
            adicionar_livro(matricula, nome, autor, codigo)
            atualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")

    janela_usuario = tk.Tk()
    janela_usuario.title(f"Usuário: {nome_usuario}")
    janela_usuario.geometry("600x550")
    janela_usuario.configure(bg="#f0f0f0")

    ttk.Label(janela_usuario, text=f"Livros de {nome_usuario}", font=("Helvetica", 16, "bold"), background="#f0f0f0").pack(pady=20)

    frame_livros = ttk.Frame(janela_usuario)
    frame_livros.pack(pady=10)

    colunas = ("Nome do Livro", "Autor", "Código")
    lista_livros = ttk.Treeview(frame_livros, columns=colunas, show="headings", height=10)
    for coluna in colunas:
        lista_livros.heading(coluna, text=coluna)
        lista_livros.column(coluna, width=150, anchor="center")
    lista_livros.pack(side="left")

    scroll = ttk.Scrollbar(frame_livros, orient="vertical", command=lista_livros.yview)
    lista_livros.configure(yscroll=scroll.set)
    scroll.pack(side="right", fill="y")

    atualizar_lista()

    frame_adicionar = ttk.Frame(janela_usuario, padding=20)
    frame_adicionar.pack(pady=20)

    ttk.Label(frame_adicionar, text="Adicionar Livro").grid(row=0, column=0, columnspan=2, pady=10)

    ttk.Label(frame_adicionar, text="Nome do Livro:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entrada_nome_livro = ttk.Entry(frame_adicionar, width=30)
    entrada_nome_livro.grid(row=1, column=1, padx=5, pady=5)

    ttk.Label(frame_adicionar, text="Autor:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    entrada_autor = ttk.Entry(frame_adicionar, width=30)
    entrada_autor.grid(row=2, column=1, padx=5, pady=5)

    ttk.Label(frame_adicionar, text="Código:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
    entrada_codigo = ttk.Entry(frame_adicionar, width=30)
    entrada_codigo.grid(row=3, column=1, padx=5, pady=5)

    ttk.Button(frame_adicionar, text="Adicionar", command=adicionar_novo_livro).grid(row=4, column=0, columnspan=2, pady=10)

    janela_usuario.mainloop()



inicializar_arquivos()
tela_inicial()