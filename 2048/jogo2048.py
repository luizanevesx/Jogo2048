import random

class Jogo2048:
    def __init__(self):
        self.matriz = [[0]*4 for _ in range(4)]
        self.iniciar_jogo()

    def iniciar_jogo(self):
        for _ in range(2):
            self.inserir_novo_numero()

    def inserir_novo_numero(self):
        if any(0 in linha for linha in self.matriz):
            linha, coluna = random.choice([(i, j) for i in range(4) for j in range(4) if self.matriz[i][j] == 0])
            self.matriz[linha][coluna] = random.choice([2, 4])

    def realizar_movimento(self, direcao):
        if direcao == 'w':
            self.mover_para_cima()
        elif direcao == 's':
            self.mover_para_baixo()
        elif direcao == 'a':
            self.mover_para_esquerda()
        elif direcao == 'd':
            self.mover_para_direita()
        else:
            print("Direção inválida!")

    def mover_para_cima(self):
        self.matriz = self.transpor(self.matriz)
        self.mover_para_esquerda()
        self.matriz = self.transpor(self.matriz)

    def mover_para_baixo(self):
        self.matriz = self.transpor(self.matriz)
        self.mover_para_direita()
        self.matriz = self.transpor(self.matriz)

    def mover_para_esquerda(self):
        self.matriz = [self.combinar(linha) for linha in self.matriz]

    def mover_para_direita(self):
        self.matriz = [self.combinar(linha[::-1])[::-1] for linha in self.matriz]

    def combinar(self, linha):
        nova_linha = [num for num in linha if num != 0]
        for i in range(len(nova_linha) - 1):
            if nova_linha[i] == nova_linha[i + 1]:
                nova_linha[i] *= 2
                nova_linha[i + 1] = 0
        nova_linha = [num for num in nova_linha if num != 0]
        nova_linha += [0] * (4 - len(nova_linha))
        return nova_linha

    def transpor(self, matriz):
        return [list(linha) for linha in zip(*matriz)]

    def verificar_fim_de_jogo(self):
        if any(0 in linha for linha in self.matriz):
            return False
        for i in range(4):
            for j in range(3):
                if self.matriz[i][j] == self.matriz[i][j + 1]:
                    return False
                if self.matriz[j][i] == self.matriz[j + 1][i]:
                    return False
        return True

class Jogo2048Avancado(Jogo2048):
    def __init__(self):
        super().__init__()

    def inserir_novo_numero(self):
        super().inserir_novo_numero()
        print("Novo número inserido!")

    def realizar_movimento(self, direcao):
        super().realizar_movimento(direcao)
        print("Movimento realizado:", direcao)