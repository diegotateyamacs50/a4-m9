NPLAYER = 0
higher_point = 0
highest_player = 0

# Decide o vencedor 
def player_score(word):
    # Tabela de pontos de Scrabble
    char_points = {
        'a': 1,'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
        'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
        'u': 4, 'v': 4, 'w': 8, 'x': 4, 'y': 10, 'z': 10
    }

    # Inicializa a pontuação do jogador
    score = 0

    # Contagem de pontos
    for char in word:
        if char in char_points:
            score += char_points[char]

    return score

# Verifica se há somente uma palavra na entrada do usuário
def one_word(word):
    # Retira os espaços iniciais e finais da string()
    word = word.strip()
    for i in word:
        if i == ' ':
            print("Insira somente uma palavra por jogador!")
            return False
    return True

