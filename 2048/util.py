import json

def carregar_pontuacoes():
    try:
        with open("pontuacoes.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_pontuacao(jogador):
    pontuacoes = carregar_pontuacoes()
    pontuacoes.append({
        "nome": jogador.nome,
        "idade": jogador.idade,
        "pontuacao": jogador.pontuacao
    })
    with open("pontuacoes.json", "w") as arquivo:
        json.dump(pontuacoes, arquivo, indent=4)