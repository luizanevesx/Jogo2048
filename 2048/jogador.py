import json

class Jogador:
    def __init__(self, nome, idade, pontuacao=0):
        self.nome = nome
        self.idade = idade
        self.pontuacao = pontuacao

def carregar_jogadores():
    try:
        with open("jogadores.json", "r") as arquivo:
            jogadores_data = json.load(arquivo)
            return [Jogador(**jogador) for jogador in jogadores_data]
    except FileNotFoundError:
        return []

def salvar_jogadores(jogadores):
    with open("jogadores.json", "w") as arquivo:
        json.dump([j.__dict__ for j in jogadores], arquivo, indent=4)