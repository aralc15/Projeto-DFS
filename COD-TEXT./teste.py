import random
from collections import deque

#Verifica os movimentos possiveis da peca
def movs(tabuleiro, pos):
    x, y = pos
    movimentos = []
    
    #Direções possíveis: cima diagonal esquerda, cima diagonal direita, baixo diagonal esquerda, baixo diagonal direita
    direcoes = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  

    for dx, dy in direcoes:
        nova_x, nova_y = x + dx, y + dy
        #Ve se tem posicoes vazias no tabuleiro
        if 0 <= nova_x < 8 and 0 <= nova_y < 8 and tabuleiro[nova_x][nova_y] == 0:
            movimentos.append((nova_x, nova_y))
    
    return movimentos

#Faz a dama se mover de forma aleatoria pelo tabuleiro
def movimento_aleatorio(tabuleiro, pos):
    x, y = pos
    caminho = [pos]
    visitado = set([pos])  #Regras brasileiras, a dama nao pode voltar, entao faz ela nao visitar lugares ja passados
    
    while x != 0:  #Continua até atingir a linha 0
        movimentos = movs(tabuleiro, (x, y))
        
        #Faz com que apenas os movimentos para cima sejam considerados 
        movimentos_validos = [mov for mov in movimentos if mov[0] < x]
        
        if not movimentos_validos:
            break  #Se nao tiver mais movimentos para cima, entao acaba, pois chegou ao seu destino, no caso (0,y)
        
        #Seleciona de forma aleatória o próximo movimento
        movimento = random.choice(movimentos_validos)
        
        #Atualiza a posição
        x, y = movimento
        caminho.append(movimento)
        visitado.add(movimento)
        tabuleiro[x][y] = 1  #Marca a casa ocupada
        
    return caminho

#Funcao "bfs" que mostra o caminho mais curto
def bfs_dama(tabuleiro, inicio, destino):
    fila = deque([inicio])
    visitado = set([inicio])
    caminho = {inicio: None}

    while fila:
        pos = fila.popleft()
        if pos == destino:
            break
        
        # movimentos possiveis
        for movimento in movs(tabuleiro, pos):
            if movimento not in visitado:
                fila.append(movimento)
                visitado.add(movimento)
                caminho[movimento] = pos

    #Refaz o caminho
    caminho_final = []
    pos = destino
    while pos != inicio:
        caminho_final.append(pos)
        pos = caminho[pos]
    caminho_final.append(inicio)
    caminho_final.reverse()
    
    return caminho_final

#Tabuleiro utilizado para exemplo foi o 8x8, se for necessaria alguma mudanca nas regras do tabuleiro, apenas trocar os numeros
tabuleiro = [[0 for _ in range(8)] for _ in range(8)]
inicio = (7, 1)  #Obriga a comecar sempre na ultima posicao

#Faz a dama ter movimento aleatorio
caminho_aleatorio = movimento_aleatorio(tabuleiro, inicio)

print("Resultado do caminho da dama:", caminho_aleatorio)
