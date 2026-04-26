from typing import List, Tuple
from random import choice

Matriz = List[List[int]]
Cordenada = Tuple[int, int]

jogadores = {    
    1: 'X',
    2: 'O'
    }

simbolos = {
    0: ' ',
} | jogadores


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
            print(*['-']*len(matriz), sep='-+-')

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

    if jogador_key not in jogadores.keys():
        raise ValueError('Chave de jogador Invalida')
    
    x, y = pos
    
    if matriz[y][x] != 0:
        raise ValueError('Posicao de jogada Invalida')
    
    matriz[y][x] = jogador_key
    return matriz
    

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
        key do ganhador ou None
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

    return None


def verificar_empate(matriz: Matriz) -> bool:
    """Verifia se todas as casas já foram preenchidas 
    Args: 
        matriz: matriz a ser verificada
    Returns: 
        Verdadeiro caso todas as casas preenchidas
    """

    return all((all(l) for l in matriz))


def game_terminado(matriz: Matriz) -> bool:
    """Verifia se o jogo terminou 
    Args: 
        matriz: matriz a ser verificada
    Returns: 
        Verdadeiro caso jogo finalizada
    """
    return verificar_empate(matriz) or verificar_ganhador(matriz) is not None


def jogada_aleatoria(matriz: Matriz) -> Cordenada:
    """Escolhe aleatoriamente uma jogada"""
    return choice(possiveis_jogadas(matriz))


def avaliar(matriz: Matriz) -> int:
    """Avalia se a jogada é boa ou nao para a cpu
    Args: 
        matriz: matriz a ser analizada
    Returns: 
        1 vitoria, 0 empate, -1 derrota
    """
    ganhador = verificar_ganhador(matriz)
    
    if ganhador == 1: return -1
    if ganhador == 2: return 1
    return 0


def minimax(matriz: Matriz, maximizar: bool, alfa: float=-float('inf'), beta: float=float('inf')) -> float:
    if game_terminado(matriz):
        return avaliar(matriz)

    if maximizar:
        value = -float('inf')
        for jogada in possiveis_jogadas(matriz):
            x, y = jogada
            
            matriz[y][x] = 2
            value = max(value, minimax(matriz, False, alfa, beta))
            alfa = max(alfa, value)
            matriz[y][x] = 0

            if beta <= alfa:
                break
    else:
        value = float('inf')
        for jogada in possiveis_jogadas(matriz):
            x, y = jogada
            
            matriz[y][x] = 1
            value = min(value, minimax(matriz, True, alfa, beta))
            beta = min(beta, value)
            matriz[y][x] = 0

            if beta <= alfa:
                break

    return value


def jogada_minimax(matriz: Matriz) -> Cordenada:
    jogadas = possiveis_jogadas(matriz)
    results = []
    for j in jogadas:
        x, y = j
        matriz[y][x] = 2
        results.append((minimax(matriz, False), j))
        matriz[y][x] = 0
    return max(results, key=lambda x: x[0])[1]


if __name__ == '__main__':
    
    jogador_fase = input('Deseja comecar jogando? [s/n]').lower() == 's'
    
    campo = gerar_matriz(4)
    while not game_terminado(campo):
        print_board(campo)
        if jogador_fase:
            while True:
                try:
                    player_jogada = int(input('Qual casa voce quer jogar? [1 - 9] '))-1
                    pos_player = player_jogada % len(campo), player_jogada // len(campo)
                    realizar_jogada(campo, pos_player, 1)
                except ValueError:
                    print('Jogada Invalida')
                else: 
                    break
        else:
            pos_cpu = jogada_minimax(campo)
            realizar_jogada(campo, pos_cpu, 2)

        jogador_fase = not jogador_fase


    print_board(campo)
    gg = verificar_ganhador(campo)
    if gg == 1:
        print('Voce ganhou!')
    elif gg == 2:
        print('Voce perdeu!')
    else:
        print('Empate!')