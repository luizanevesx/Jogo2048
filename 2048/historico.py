import tkinter as tk
from util import carregar_pontuacoes

class HistoricoWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Histórico de Jogos")

        pontuacoes = carregar_pontuacoes()
        historico_str = "\n".join([f"{p['nome']}, {p['idade']} anos: {p['pontuacao']} pontos" for p in pontuacoes])

        tk.Label(self.root, text="Histórico de Jogos", font=("Arial", 24)).pack(pady=10)
        tk.Label(self.root, text=historico_str, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Fechar", command=self.root.destroy).pack(pady=10)

        self.root.mainloop()