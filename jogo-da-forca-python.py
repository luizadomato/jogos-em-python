import random

def jogar_forca():
    palavras = ['python', 'java', 'ruby', 'javascript', 'php']
    palavra_secreta = random.choice(palavras)
    letras_descobertas = []
    tentativas = 6

    print("Bem-vindo ao jogo da forca!")
    print("A palavra possui", len(palavra_secreta), "letras.")
    print("_ " * len(palavra_secreta))

    while True:
        letra = input("Digite uma letra: ").lower()

        if letra in letras_descobertas:
            print("Você já tentou essa letra antes. Tente novamente.")
            continue

        if letra in palavra_secreta:
            letras_descobertas.append(letra)
            print("Você acertou uma letra!")
        else:
            tentativas -= 1
            print("Você errou. Você tem", tentativas, "tentativas restantes.")

        palavra_atual = ""
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_descobertas:
                palavra_atual += letra_secreta + " "
            else:
                palavra_atual += "_ "

        print(palavra_atual)

        if tentativas == 0:
            print("Você perdeu! A palavra era:", palavra_secreta)
            break

        if set(palavra_secreta) == set(letras_descobertas):
            print("Parabéns! Você ganhou!")
            break

jogar_forca()