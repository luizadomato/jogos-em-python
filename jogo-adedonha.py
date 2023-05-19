import time
import random

def jogar_adedonha():
    rodadas = 3
    letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    print("Bem-vindo ao jogo de Adedonha!")
    print("Cada jogador deve fornecer uma palavra que comece com a letra da rodada dentro de 10 segundos.")
    print("Pronto para começar?\n")
    
    for rodada in range(1, rodadas + 1):
        letra = random.choice(letras)
        print(f"Rodada {rodada}: Começando com a letra '{letra}'")
        
        palavra = input("Digite uma palavra: ").upper()
        
        tempo_inicial = time.time()
        while palavra[0] != letra:
            tempo_atual = time.time()
            if tempo_atual - tempo_inicial > 10:
                print("Tempo esgotado!")
                return
            
            print("A palavra deve começar com a letra correta.")
            palavra = input("Digite outra palavra: ").upper()
        
        print("Palavra válida!")
        print()
    
    print("O jogo acabou!")
    
jogar_adedonha()