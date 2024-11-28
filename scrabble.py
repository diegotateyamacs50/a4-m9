

# TODO: IMPLEMENTAR VERIFICAÇÃO DE EMPATES

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

# main
def main():
    NPLAYER = 0
    higher_point = 0
    highest_player = 0

    print("Bem vindo ao jogo de Scrabble!")
    # Número de jogadores que irão participar
    NPLAYER = int(input("Quantos jogadores irão participar? "))

    words = []
    scores = []

    # Pegar palavra do jogador 1 e 2
    for p in range(NPLAYER):
        input_player = input(f"Jodador {p + 1}, insira sua palavra: ")
        
        # Verifica se há somente uma palavra como entrada
        if not one_word(input_player):
            print(f"Jogador {p + 1} foi desqualificado dessa rodada por inserir mais de uma palavra.")
            continue

         # Transforma em minúscula (para a contagem de pontos)
        input_player = input_player.lower()
        words.append(input_player)
        scores.append(player_score(input_player))
        
    # Linha para separar mensagem de entrada e pontuação
    print('-' * 40)

    # Mostra as pontuações de todos os jogadores
    # Decide o vencedor
    for i in range(NPLAYER):
        print(f"Jogador {i + 1} - Palavra: {words[i]} - Pontuação: {scores[i]}")

        # Verifica a maior pontuação
        if scores[i] > higher_point:
            higher_point = scores[i]
            highest_player = i

    for t in range(NPLAYER):
        if scores[t] == higher_point:
            print("Houve um empate!")
            return


    print(f"O jogador {highest_player + 1} venceu com {higher_point} pontos!")


if __name__ == "__main__":
    main()