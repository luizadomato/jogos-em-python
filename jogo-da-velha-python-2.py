def Velha():
  tabuleiro = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  acabou = False
  QuadradoMagico = [4, 9, 2, 3, 5, 7, 8, 1, 6]

  def Design():
    print()
    print('', tabuleiro[0], "|", tabuleiro[1], "|", tabuleiro[2])
    print("---|---|---")
    print('', tabuleiro[3], "|", tabuleiro[4], "|", tabuleiro[5])
    print("---|---|---")
    print('', tabuleiro[6], "|", tabuleiro[7], "|", tabuleiro[8])
    print()

  def PegarNumero():
    while True:
      numero = input()
      try:
        numero  = int(numero)
        if numero in range(1, 10):
          return numero
        else:
          print("Este número não está no tabuleiro, lerdo!!", "\U0001f620")
      except ValueError:
        print("Isso não é um número, seu lesado !!", "\U0001f624")
        continue

  def Turno(jogador):
    espaco_colocado = PegarNumero() - 1
    if tabuleiro[espaco_colocado] == "X" or tabuleiro[espaco_colocado] == "O":
      print("Esse espaço já foi preenchido, tente outro.")
      Turno(jogador)
    else:
      tabuleiro[espaco_colocado] = jogador

  def ChecaVitoria(jogador):
    jogadas = 0

    for x in range(9):
      for y in range(9):
        for z in range(9):
          if x != y and y != z and z != x:
            if tabuleiro[x] == jogador and tabuleiro[y] == jogador and tabuleiro[z] == jogador:
              if QuadradoMagico[x] + QuadradoMagico[y] + QuadradoMagico[z] == 15:
                print("Jogador", jogador ,"ganhou!\n")
                return True

    for a in range(9):
      if tabuleiro[a] == "X" or tabuleiro[a] == "O":
        jogadas += 1
      if jogadas == 9:
        print("O jogo acabou em um empate.")
        return True

  while not acabou:
    Design()
    acabou = ChecaVitoria("O")
    if acabou == True:
      break
    print("Jogador X, escolha um espaço.")
    Turno("X")
   
    Design()
    acabou = ChecaVitoria("X")
    if acabou == True:
      break
    print("Jogador O, escolha um espaço.")
    Turno("O")


Velha()