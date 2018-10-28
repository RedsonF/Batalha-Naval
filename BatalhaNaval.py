#coding: utf-8
import random

tabuleiro = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for x in range(12)]

horizontal = 0
vertical = 1

def numeroRandom(fim):
    return random.randint(0, fim)

def alocaPortaAvioes():
    direcao = numeroRandom(1)
    tamanho = 5
    if (direcao == horizontal):
        linha = numeroRandom(11)
        coluna = numeroRandom(6)
        for i in range(tamanho):
            tabuleiro[linha][coluna] = 5
            coluna += 1
    else:
        linha = numeroRandom(6)
        coluna = numeroRandom(11)
        for i in range(tamanho):
            tabuleiro[linha][coluna] = 5
            linha += 1

alocaPortaAvioes()
for i in tabuleiro:
    print i
