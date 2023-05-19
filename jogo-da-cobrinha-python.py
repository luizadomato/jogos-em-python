import pygame
import time
import random

# Inicialização do Pygame
pygame.init()

# Definição das cores
cor_fundo = (0, 0, 0)
cor_cobra = (0, 255, 0)
cor_comida = (255, 0, 0)

# Tamanho da janela
largura_janela = 800
altura_janela = 600

# Criação da janela
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption('Jogo da Cobrinha')

# Variáveis de controle
clock = pygame.time.Clock()
tamanho_cobra = 20
velocidade = 8

# Função para desenhar a cobra
def desenhar_cobra(tamanho_cobra, lista_cobra):
    for posicao in lista_cobra:
        pygame.draw.rect(janela, cor_cobra, (posicao[0], posicao[1], tamanho_cobra, tamanho_cobra))

# Função principal do jogo
def jogo():
    game_over = False
    fim_do_jogo = False

    # Posição inicial da cobra
    posicao_cobra_x = largura_janela / 2
    posicao_cobra_y = altura_janela / 2

    # Movimento inicial da cobra
    movimento_cobra_x = 0
    movimento_cobra_y = 0

    # Lista para armazenar o corpo da cobra
    lista_cobra = []
    comprimento_cobra = 1

    # Posição inicial da comida
    posicao_comida_x = round(random.randrange(0, largura_janela - tamanho_cobra) / 20.0) * 20.0
    posicao_comida_y = round(random.randrange(0, altura_janela - tamanho_cobra) / 20.0) * 20.0

    while not game_over:
        while fim_do_jogo == True:
            janela.fill(cor_fundo)
            fonte = pygame.font.Font('freesansbold.ttf', 40)
            texto = fonte.render("Fim do Jogo! Pressione Q para sair ou C para jogar novamente.", True, cor_cobra)
            janela.blit(texto, (largura_janela / 6, altura_janela / 3))
            pygame.display.update()

            # Tratamento de eventos
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        fim_do_jogo = False
                    if event.key == pygame.K_c:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movimento_cobra_x = -tamanho_cobra
                    movimento_cobra_y = 0
                elif event.key == pygame.K_RIGHT:
                    movimento_cobra_x = tamanho_cobra
                    movimento_cobra_y = 0
                elif event.key == pygame.K_UP:
                    movimento_cobra_y = -tamanho_cobra
                    movimento_cobra_x = 0
                elif event.key == pygame.K_DOWN:
                    movimento_cobra_y = tamanho_cobra
                    movimento_cobra_x = 0

        if posicao_cobra_x >= largura_janela or posicao_cobra_x < 0 or posicao_cobra_y >= altura_janela or posicao_cobra_y < 0:
            fim_do_jogo = True
        posicao_cobra_x += movimento_cobra_x
        posicao_cobra_y += movimento_cobra_y
        janela.fill(cor_fundo)
        pygame.draw.rect(janela, cor_comida, (posicao_comida_x, posicao_comida_y, tamanho_cobra, tamanho_cobra))
        cobra_cabeca = []
        cobra_cabeca.append(posicao_cobra_x)
        cobra_cabeca.append(posicao_cobra_y)
        lista_cobra.append(cobra_cabeca)
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        for segmento in lista_cobra[:-1]:
            if segmento == cobra_cabeca:
                fim_do_jogo = True

        desenhar_cobra(tamanho_cobra, lista_cobra)

        pygame.display.update()

        if posicao_cobra_x == posicao_comida_x and posicao_cobra_y == posicao_comida_y:
            posicao_comida_x = round(random.randrange(0, largura_janela - tamanho_cobra) / 20.0) * 20.0
            posicao_comida_y = round(random.randrange(0, altura_janela - tamanho_cobra) / 20.0) * 20.0
            comprimento_cobra += 1

        clock.tick(velocidade)

    pygame.quit()

# Início do jogo
jogo()
