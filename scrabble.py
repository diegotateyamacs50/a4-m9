# Verifica se há somente uma palavra na entrada do usuário
def one_word(word):
    # Retira os espaços iniciais e finais da string()
    word = word.strip()
    for i in word:
        if i == ' ':
            print("Insira somente uma palavra por jogador!")
            return False
    return True

