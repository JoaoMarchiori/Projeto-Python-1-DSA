# Projeto 1 - Desenvolvendo um jogo (Hangman Game - Jogo da Forca) -Versão 1

# import 
import random
from os import system, name

# Função para limpar a tela e remover o histórico
def limpa_tela():

    # Windows
    if name == 'nt':
        _= system('cls') # Mac or Linux - 'clear'


# Função do game
def game():

    limpa_tela()
    print("\nWelcome to Hangman Game!")
    print("\nGuess the word below:\n")

    # Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    # Escolher a palavra
    palavra = random.choice(palavras)

    # List comprehesion
    letras_descobertas = ['_' for letra in palavra]

    # Número de chances
    chances = 6

    # Lista palabras erradas
    letras_erradas = []

    # Loop enquanto número de chances for maior do que zero

    while chances > 0:
        # Print
        print(" ".join(letras_descobertas))
        print("\nChances restantes: ", chances)
        print("Letras erradas: "," ".join(letras_erradas))

        # Tentativa
        tentativa = input("\nDigite uma letra: ").lower()

        # Condicional
        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index  += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
        
        # Condicional
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era: ", palavra)
            break

    # Condicional
    if "_" in letras_descobertas:
        print("\nVocê Perdeu, a palavra era: ", palavra)

# Bloco main
if __name__ == "__main__":
    game()
    print("\nParabéns, você está aprendendo a programação em Python com a DSA. :)\n")