# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 2

# Import Musicas
import pygame
import os
import sys

# Import
import random
from os import system, name


# Inicializar o Pygame
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()

# Diretório onde suas músicas estão armazenadas
caminho_das_musicas = r"C:\Users\Jose Angelo\Documents\Python\Projeto-Python-1-DSA"

# Lista de músicas
lista_de_começo = ["abertura-roda-roda-jequiti.mp3", "among.mp3", "all-my-fellas.mp3"]
lista_de_final_ruim = ["ninguem-acertou.mp3", "elost-a-life-game-over-sound-effect-8-bits.mp3" "quepena.mp3"]
lista_de_final_bom = ["resposta-certa-roda-roda.mp3", "acertou_By4HwUh.mp3"]
lista_de_erro = ["nao-se-preocupe-nada-vai-dar-certo.mp3", "ce-vai-morre-faustao.mp3", "errou_T6fvucS.mp3", "erro1_xwwXzUN.mp3", "roda-a-roda-errou.mp3", "perdeu-tudo-roda-roda-jequiti.mp3"]
lista_de_acerto = ["letra-roda-a-roda.mp3"]

# Função para tocar música
def tocar_musica(lista_de_musicas):
    musica_escolhida = random.choice(lista_de_musicas)
    caminho_da_musica = os.path.join(caminho_das_musicas, musica_escolhida)
    pygame.mixer.music.load(caminho_da_musica)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def comeco():
    tocar_musica(lista_de_começo)

def finalruim():
    tocar_musica(lista_de_final_ruim)

def finalbom():
    tocar_musica(lista_de_final_bom)

def errou():
    tocar_musica(lista_de_erro)

def acertou():
    tocar_musica(lista_de_acerto)

# Função para limpar a tela a cada execução
def limpa_tela():
 
    # Windows
    if name == 'nt':
        _ = system('cls')

# Função que desenha a forca na tela
def display_hangman(chances):

    # Lista de estágios da forca
    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[chances]

# Função do jogo
def game():

    limpa_tela()
    print("\nBem vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")
    comeco()
    # Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    
    # Escolhe randomicamente uma palavra
    palavra = random.choice(palavras)
    
    # Lista  de letras  da palavra
    lista_letras_palavras = [letra for letra in palavra]
    
    # Cria o tabuleiro com o caracter "_" multiplicado pelo comprimento da palavra
    tabuleiro = ["_"]* len(palavra)
    
    # Número de chances
    chances = 6
    
    # Lista para as letras digitadas
    letras_tentativas = []
    
    # Loop enquanto número de chances for maior do que zero
    while chances > 0:
        
        print(display_hangman(chances))
        print("Palavra: ", tabuleiro)
        print("\n")
        
        # Tentativa
        tentativa = input("\nDigite uma letra: ")
        
        # Condicional
        if tentativa in letras_tentativas:
            print("Você já tentou essa letra. Escolha outra!")
            continue
        
        # Lista de tentativas (letras)
        letras_tentativas.append(tentativa)
        
        # Condicional
        if tentativa in lista_letras_palavras:
            
            print("Você acertou a letra!")
            
            # Loop
            for indice in range(len(lista_letras_palavras)):

                # Condicional
                if lista_letras_palavras[indice] == tentativa:
                    tabuleiro[indice] = tentativa
                    acertou()
            # Se todos os espaços foram preenchidos, o jogo acabou
            if "_" not in tabuleiro:
                print("\nVocê venceu! A palavra era: {}".format(palavra))
                finalbom()
                break
        else:
            print("Ops. Essa letra não está na palavra!")
            errou()
            # Decremento
            chances -= 1
    
    # Condicional
    if "_" in tabuleiro:
        print("\nVocê perdeu! A palavra era: {}.".format(palavra))
        finalruim()

# Bloco main
if __name__ == "__main__":
    game()
    print("\nParabéns. Você está aprendendo programação em Python com a DSA. :)\n")

# Encerrar o Pygame
pygame.quit()
