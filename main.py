from typing import List, Tuple
import copy
from random import choice

Matriz = List[List]
Cordenada = Tuple[int, int]

simbolos = {
    0: ' ',
    1: 'X',
    2: 'O'
}


def gerar_matriz(x:int = 3) -> Matriz:
    """Cria uma matriz x por x
    Args:
        x: Tamanho da matriz
    Returns:
        Uma Matriz
    """
    
    return [[0]*x for _ in range(x)]


def print_matriz(matriz: Matriz):
    """Exibe na tela uma matriz
    Args:
        matriz: matriz a ser exibida
    """
    
    for l in matriz:
        print([simbolos[j] for j in l])


def print_board(matriz: Matriz):
    """Exibe na tela o campo
    Args:
        matriz: matriz a ser exibida
    """
    print('\n')

    for i, line in enumerate(matriz):
        print(*[simbolos[l] for l in line], sep=' | ')

        if i != len(line) - 1:
            print('--+---+--')

    print('\n')


def realizar_jogada(matriz: Matriz, pos: Cordenada, jogador_key:int) -> Matriz:
    """Realiza uma jogada na matriz
    Args:
        matriz: matriz a ser realizada  a jogada
        pos: Cordenada da jogada (x, y)
        jogador_key: numero do jogador
    Returns:
        uma nova matriz com a jogada realizada
    """

    if jogador_key not in simbolos.keys():
        raise ValueError('Chave de jogador Invalida')
    
    x, y = pos
    
    if matriz[y][x] != 0:
        raise ValueError('Posicao de jogada Invalida')
    
    n_matriz = copy.deepcopy(matriz)
    n_matriz[y][x] = jogador_key
    return n_matriz
    

def possiveis_jogadas(matriz: Matriz) -> List[Cordenada]:
    """Calcula todas as possiveis jogadas
    Args: 
        matriz: matriz a ser verificada
    Returns: 
        Lista contendo as cordenadas das possiveis jogadas
    """
    tamanho = len(matriz)
    return [(x,y) for y in range(tamanho) for x in range(tamanho) if matriz[y][x] == 0]


def verificar_ganhador(matriz: Matriz) -> int:
    """Verifica se existe algum ganhador
    Args: 
        matriz: Matriz a ser verificada
    Returns:
        key do ganhador ou 0
    """

    n = len(matriz)

    # Linhas
    for linha in matriz:
        if linha[0] != 0 and all(x == linha[0] for x in linha):
            return linha[0]

    # Colunas
    for col in range(n):
        val = matriz[0][col]
        if val != 0 and all(matriz[lin][col] == val for lin in range(n)):
            return val

    # Diagonal principal
    val = matriz[0][0]
    if val != 0 and all(matriz[i][i] == val for i in range(n)):
        return val

    # Diagonal secundária
    val = matriz[n - 1][0]
    if val != 0 and all(matriz[n - 1 - i][i] == val for i in range(n)):
        return val

    return 0


def verificar_empate(matriz: Matriz) -> bool:
    """Verifia se todas as casas já foram preenchidas 
    Args: 
        matriz: matriz a ser verificada
    Returns: 
        Verdadeiro caso todas as casas preenchidas
    """

    return all([all(l) for l in matriz])


def game_terminado(matriz: Matriz) -> bool:
    """Verifia se o jogo terminou 
    Args: 
        matriz: matriz a ser verificada
    Returns: 
        Verdadeiro caso jogo finalizada
    """
    if verificar_empate(matriz) or verificar_ganhador(matriz):
        return True
    return False


if __name__ == '__main__':
    campo = gerar_matriz()

    while not game_terminado(campo):
        print_board(campo)
        player_jogada = int(input('Qual casa voce quer jogar? [1 - 9]'))-1
        pos_player = player_jogada % len(campo), player_jogada // len(campo)
        campo = realizar_jogada(campo, pos_player, 1)

        pos_cpu = choice(possiveis_jogadas(campo))
        campo = realizar_jogada(campo, pos_cpu, 2)


    print_board(campo)
    gg = verificar_ganhador(campo)
    if gg == 1:
        print('Voce ganhou')
    elif gg == 2:
        print('Voce perdeu')
    else:
        print('Empate')