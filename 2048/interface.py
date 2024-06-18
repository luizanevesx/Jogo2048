import tkinter as tk
from tkinter import messagebox, simpledialog
from jogador import Jogador, salvar_jogadores
from util import carregar_pontuacoes, salvar_pontuacao
from ranking import RankingWindow
from historico import HistoricoWindow

class InterfaceDeUsuario:
    def __init__(self, jogo, jogador, jogadores):
        self.jogo = jogo
        self.jogador = jogador
        self.jogadores = jogadores

        self.root = tk.Tk()
        self.root.title("2048")

        self.criar_menu()

        self.labels = [[tk.Label(self.root, text="", width=4, height=2, font=("Arial", 24, "bold"), bg="lightgray", relief="ridge") for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for j in range(4):
                self.labels[i][j].grid(row=i, column=j, padx=5, pady=5)

        self.root.bind("<KeyPress-w>", lambda event: self.movimento("w"))
        self.root.bind("<KeyPress-s>", lambda event: self.movimento("s"))
        self.root.bind("<KeyPress-a>", lambda event: self.movimento("a"))
        self.root.bind("<KeyPress-d>", lambda event: self.movimento("d"))

        messagebox.showinfo("Bem-vindo", f"Bem-vindo {self.jogador.nome}, idade {self.jogador.idade}! Boa sorte!")

        self.atualizar_interface()

        self.root.mainloop()

    def criar_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        menu_jogo = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Jogo", menu=menu_jogo)
        menu_jogo.add_command(label="Novo Jogo", command=self.novo_jogo)
        menu_jogo.add_separator()
        menu_jogo.add_command(label="Sair", command=self.sair)

        menu_opcoes = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Opções", menu=menu_opcoes)
        menu_opcoes.add_command(label="Ver Histórico", command=self.ver_historico)
        menu_opcoes.add_command(label="Cadastro de Jogador", command=self.cadastro_jogador)
        menu_opcoes.add_command(label="Ranking de Pontuações", command=self.ranking_pontuacoes)

    def movimento(self, direcao):
        self.jogo.realizar_movimento(direcao)
        self.jogo.inserir_novo_numero()
        self.atualizar_interface()
        if self.jogo.verificar_fim_de_jogo():
            self.jogador.pontuacao = self.calcular_pontuacao()
            salvar_pontuacao(self.jogador)
            messagebox.showinfo("Fim de jogo", f"Fim de jogo! Sua pontuação: {self.jogador.pontuacao}")
            self.root.destroy()

    def atualizar_interface(self):
        for i in range(4):
            for j in range(4):
                valor = self.jogo.matriz[i][j]
                self.labels[i][j].config(text=str(valor) if valor != 0 else "", bg=self.definir_cor(valor))

    def definir_cor(self, valor):
        cores = {
            0: "lightgray",
            2: "#eee4da",
            4: "#ede0c8",
            8: "#f2b179",
            16: "#f59563",
            32: "#f67c5f",
            64: "#f65e3b",
            128: "#edcf72",
            256: "#edcc61",
            512: "#edc850",
            1024: "#edc53f",
            2048: "#edc22e",
        }
        return cores.get(valor, "black")

    def calcular_pontuacao(self):
        return sum(sum(linha) for linha in self.jogo.matriz)

    def novo_jogo(self):
        self.root.destroy()
        from main import menu_principal
        menu_principal()

    def ver_historico(self):
        HistoricoWindow()

    def cadastro_jogador(self):
        nome = simpledialog.askstring("Cadastro de Jogador", "Digite o nome/apelido do jogador:")
        idade = simpledialog.askinteger("Cadastro de Jogador", "Digite a idade do jogador:")
        jogador = Jogador(nome, idade)
        self.jogadores.append(jogador)
        salvar_jogadores(self.jogadores)
        messagebox.showinfo("Cadastro de Jogador", "Jogador cadastrado com sucesso!")

    def ranking_pontuacoes(self):
        RankingWindow()

    def sair(self):
        self.root.quit()