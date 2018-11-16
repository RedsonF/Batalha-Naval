#coding: utf-8
import random

tabuleiro = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for x in range(14)]

horizontal = 0
vertical = 1

def numeroRandom(fim):
    return random.randint(0, fim)

def verificaPosicao(linha, coluna, direcao, tamanho):
    if (direcao == horizontal):
        for i in range(tamanho):
            if (tabuleiro[linha][coluna] != 0):
                return False
            coluna += 1
        return True
    else:
        for i in range(tamanho):
            if (tabuleiro[linha][coluna] != 0):
                return False
            linha += 1
        return True

def alocaPortaAvioes():
    direcao = numeroRandom(1)
    tamanho = 6
    if (direcao == horizontal):
        linha = numeroRandom(13)
        coluna = numeroRandom(7)
        for i in range(tamanho):
            tabuleiro[linha][coluna] = 6
            tabuleiro[linha+1][coluna] = 6
            coluna += 1
    else:
        linha = numeroRandom(7)
        coluna = numeroRandom(13)
        for i in range(tamanho):
            tabuleiro[linha][coluna] = 6
            tabuleiro[linha][coluna+1] = 6
            linha += 1

def alocarCruzador():
    direcao = numeroRandom(1)
    tamanho = 5
    if (direcao == horizontal):
        linha = numeroRandom(13)
        coluna = numeroRandom(8)
        if (verificaPosicao(linha, coluna, direcao, tamanho) == True):
            for i in range(tamanho):
                tabuleiro[linha][coluna] = 5
                coluna += 1
        else:
            alocarCruzador()
    else:
        linha = numeroRandom(8)
        coluna = numeroRandom(13)
        if (verificaPosicao(linha, coluna, direcao, tamanho) == True):
            for i in range(tamanho):
                tabuleiro[linha][coluna] = 5
                linha += 1
        else:
            alocarCruzador()

alocaPortaAvioes()
alocarCruzador()
alocarCruzador()
alocarCruzador()
alocarCruzador()
alocarCruzador()
for i in tabuleiro:
    print i
