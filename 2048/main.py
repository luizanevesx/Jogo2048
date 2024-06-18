import tkinter as tk
from tkinter import messagebox, simpledialog
from jogador import Jogador, carregar_jogadores, salvar_jogadores
from jogo2048 import Jogo2048Avancado
from interface import InterfaceDeUsuario
from historico import HistoricoWindow
from ranking import RankingWindow

jogadores = carregar_jogadores()

def menu_principal():
    root = tk.Tk()
    root.title("2048 - Menu Principal")

    frame = tk.Frame(root)
    frame.pack(pady=20)

    tk.Label(frame, text="Menu Principal", font=("Arial", 24)).pack(pady=10)
    tk.Button(frame, text="Iniciar Jogo", font=("Arial", 16), command=lambda: iniciar_jogo(root)).pack(fill=tk.X, pady=5)
    tk.Button(frame, text="Ver Histórico", font=("Arial", 16), command=lambda: HistoricoWindow()).pack(fill=tk.X, pady=5)
    tk.Button(frame, text="Cadastro de Jogador", font=("Arial", 16), command=cadastro_jogador).pack(fill=tk.X, pady=5)
    tk.Button(frame, text="Ranking de Pontuações", font=("Arial", 16), command=lambda: RankingWindow()).pack(fill=tk.X, pady=5)
    tk.Button(frame, text="Sair", font=("Arial", 16), command=root.quit).pack(fill=tk.X, pady=5)

    root.mainloop()

def iniciar_jogo(root):
    if not jogadores:
        messagebox.showinfo("Erro", "Nenhum jogador cadastrado! Faça o cadastro primeiro.")
    else:
        root.destroy()
        selecao_jogador()

def selecao_jogador():
    root = tk.Tk()
    root.title("2048 - Seleção de Jogador")

    frame = tk.Frame(root)
    frame.pack(pady=20)

    tk.Label(frame, text="Selecione o Jogador", font=("Arial", 24)).pack(pady=10)
    for i, jogador in enumerate(jogadores, 1):
        tk.Button(frame, text=f"{i}. {jogador.nome}, {jogador.idade} anos", font=("Arial", 16), command=lambda j=i-1: iniciar_interface(root, jogadores[j])).pack(fill=tk.X, pady=5)

    root.mainloop()

def iniciar_interface(root, jogador):
    root.destroy()
    jogo = Jogo2048Avancado()
    InterfaceDeUsuario(jogo, jogador, jogadores)

def cadastro_jogador():
    nome = simpledialog.askstring("Cadastro de Jogador", "Digite o nome/apelido do jogador:")
    idade = simpledialog.askinteger("Cadastro de Jogador", "Digite a idade do jogador:")
    if nome and idade:
        jogador = Jogador(nome, idade)
        jogadores.append(jogador)
        salvar_jogadores(jogadores)
        messagebox.showinfo("Cadastro de Jogador", "Jogador cadastrado com sucesso!")
    else:
        messagebox.showwarning("Cadastro de Jogador", "Nome ou idade inválidos!")

if __name__ == "__main__":
    menu_principal()