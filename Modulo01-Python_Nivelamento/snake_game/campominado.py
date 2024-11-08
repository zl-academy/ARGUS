import random
import sys
import time

class CampoMinadoCLI:
    def __init__(self, linhas, colunas, minas):
        self.linhas = linhas
        self.colunas = colunas
        self.minas = minas
        self.pontuacao = 0
        self.posicoes_minadas = set()
        self.tabuleiro = [[' ' for _ in range(colunas)] for _ in range(linhas)]
        self.tabuleiro_visivel = [['*' for _ in range(colunas)] for _ in range(linhas)]
        self.criar_tabuleiro()
        self.colocar_minasc()
        self.calcular_minass_vizinhas()
        self.tempo_inicial = None

    def criar_tabuleiro(self):
        for linha in range(self.linhas):
            for coluna in range(self.colunas):
                self.tabuleiro[linha][coluna] = 0

    def colocar_minasc(self):
        while len(self.posicoes_minadas) < self.minas:
            linha = random.randint(0, self.linhas - 1)
            coluna = random.randint(0, self.colunas - 1)
            if (linha, coluna) not in self.posicoes_minadas:
                self.posicoes_minadas.add((linha, coluna))
                self.tabuleiro[linha][coluna] = -1

    def calcular_minass_vizinhas(self):
        for linha in range(self.linhas):
            for coluna in range(self.colunas):
                if self.tabuleiro[linha][coluna] == -1:
                    continue
                contagem_minasc = 0
                for i in range(max(0, linha - 1), min(self.linhas, linha + 2)):
                    for j in range(max(0, coluna - 1), min(self.colunas, coluna + 2)):
                        if self.tabuleiro[i][j] == -1:
                            contagem_minasc += 1
                self.tabuleiro[linha][coluna] = contagem_minasc

    def imprimir_tabuleiro(self):
        # Imprimir números das colunas com alinhamento correto
        print("    ", end="")
        for coluna in range(self.colunas):
            print(f"{coluna:2} ", end=" ")
        print()

        # Imprimir linha superior do tabuleiro
        print("   +" + "---+" * self.colunas)

        # Imprimir linhas do tabuleiro
        for linha in range(self.linhas):
            print(f"{linha:2} |", end="")  # Imprimir número da linha
            for celula in self.tabuleiro_visivel[linha]:
                print(f" {celula} |", end="")
            print(f" {linha:2}")  # Imprimir número da linha do lado direito
            print("   +" + "---+" * self.colunas)

        # Imprimir números das colunas na parte inferior
        print("    ", end="")
        for coluna in range(self.colunas):
            print(f"{coluna:2} ", end=" ")

        # Imprimir pontuação atual
        print(f"\nPontuação: {self.pontuacao}")

        # Imprimir tempo decorrido
        if self.tempo_inicial:
            tempo_decorrido = int(time.time() - self.tempo_inicial)
            minutos = tempo_decorrido // 60
            segundos = tempo_decorrido % 60
            print(f"Tempo decorrido: {minutos} minutos e {segundos} segundos")

    def clicar(self, linha, coluna):
        if self.tabuleiro[linha][coluna] == -1:
            self.tabuleiro_visivel[linha][coluna] = 'X'
            self.fim_de_jogo()
        else:
            self.revelar_celula(linha, coluna)
            if self.checar_vitoria():
                self.mostrar_mensagem_vitoria()

    def revelar_celula(self, linha, coluna):
        if self.tabuleiro_visivel[linha][coluna] != '*':
            return
        if self.tabuleiro[linha][coluna] == 0:
            self.tabuleiro_visivel[linha][coluna] = ' '
            self.pontuacao += 1
            self.revelar_celulas_vizinhas(linha, coluna)
        else:
            self.tabuleiro_visivel[linha][coluna] = str(self.tabuleiro[linha][coluna])
            self.pontuacao += 1

    def revelar_celulas_vizinhas(self, linha, coluna):
        for i in range(max(0, linha - 1), min(self.linhas, linha + 2)):
            for j in range(max(0, coluna - 1), min(self.colunas, coluna + 2)):
                if self.tabuleiro_visivel[i][j] == '*':
                    self.revelar_celula(i, j)

    def fim_de_jogo(self):
        for linha, coluna in self.posicoes_minadas:
            self.tabuleiro_visivel[linha][coluna] = 'X'
        self.imprimir_tabuleiro()
        print("\n\nVocê encontrou uma mina! Fim de jogo.\n")
        tempo_decorrido = int(time.time() - self.tempo_inicial)
        minutos = tempo_decorrido // 60
        segundos = tempo_decorrido % 60
        print(f"\nPontuação final: {self.pontuacao} pontos")
        print(f"Tempo decorrido: {minutos} minutos e {segundos} segundos\n")
        self.perguntar_para_continuar()

    def mostrar_mensagem_vitoria(self):
        self.imprimir_tabuleiro()
        print("\n\nParabéns, você venceu!")
        tempo_decorrido = int(time.time() - self.tempo_inicial)
        minutos = tempo_decorrido // 60
        segundos = tempo_decorrido % 60
        print(f"\nPontuação final: {self.pontuacao}")
        print(f"Tempo decorrido: {minutos} minutos e {segundos} segundos\n")
        self.perguntar_para_continuar()

    def checar_vitoria(self):
        for linha in range(self.linhas):
            for coluna in range(self.colunas):
                if self.tabuleiro[linha][coluna] != -1 and self.tabuleiro_visivel[linha][coluna] == '*':
                    return False
        return True

    def perguntar_para_continuar(self):
        while True:
            escolha = input("Deseja jogar novamente? (S/N): ").strip().upper()
            if escolha == 'S':
                self.escolher_dificuldade()
                break
            elif escolha == 'N':
                print("Obrigado por jogar!")
                sys.exit()
            else:
                print("Entrada inválida. Digite 'S' para sim ou 'N' para não.")

    def reiniciar_jogo(self, linhas, colunas, minas):
        self.posicoes_minadas.clear()
        self.linhas = linhas
        self.colunas = colunas
        self.minas = minas
        self.tabuleiro = [[' ' for _ in range(colunas)] for _ in range(linhas)]
        self.tabuleiro_visivel = [['*' for _ in range(colunas)] for _ in range(linhas)]
        self.pontuacao = 0
        self.tempo_inicial = time.time()
        self.criar_tabuleiro()
        self.colocar_minasc()
        self.calcular_minass_vizinhas()
        self.jogar()

    def jogar(self):
        self.tempo_inicial = time.time()
        while True:
            self.imprimir_tabuleiro()
            try:
                linha, coluna = map(int, input("Digite a linha e coluna (separados por espaço): ").split())
                if 0 <= linha < self.linhas and 0 <= coluna < self.colunas:
                    self.clicar(linha, coluna)
                else:
                    print("\nEntrada inválida. Tente novamente.")
            except ValueError:
                print("\nEntrada inválida. Por favor, insira números inteiros.")

    def escolher_dificuldade(self):
        while True:
            dificuldade = input("\nEscolha o nível de dificuldade:\n1 - Fácil\n2 - Médio\n3 - Difícil\n")
            if dificuldade == '1':
                self.reiniciar_jogo(10, 10, 10)
                break
            elif dificuldade == '2':
                self.reiniciar_jogo(20, 20, 40)
                break
            elif dificuldade == '3':
                self.reiniciar_jogo(30, 30, 90)
                break
            else:
                print("Dificuldade inválida!\nEscolha entre Fácil(1), Médio(2) ou Difícil(3).")

if __name__ == "__main__":
    jogo = CampoMinadoCLI(10, 10, 10)
    jogo.escolher_dificuldade()
