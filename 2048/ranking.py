import tkinter as tk
from util import carregar_pontuacoes

class RankingWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Ranking de Pontuações")

        pontuacoes = carregar_pontuacoes()
        ranking = sorted(pontuacoes, key=lambda x: x["pontuacao"], reverse=True)

        ranking_str = "\n".join([f"{i+1}. {p['nome']}, {p['idade']} anos: {p['pontuacao']} pontos" for i, p in enumerate(ranking)])

        tk.Label(self.root, text="Ranking de Pontuações", font=("Arial", 24)).pack(pady=10)
        tk.Label(self.root, text=ranking_str, font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Fechar", command=self.root.destroy).pack(pady=10)

        self.root.mainloop()