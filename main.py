
import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da janela
LARGURA, ALTURA = 640, 480
janela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Obstapulo")

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Configurações do jogador
tamanho_jogador = 30
posicao_x_jogador = 50
posicao_y_jogador = ALTURA - tamanho_jogador - 50
velocidade_y_jogador = 0
gravidade = 1
forca_pulo = -15

# Configurações dos obstáculos
obstaculos = []
velocidade_obstaculo = 5
intervalo_criacao_obstaculo = 100
ultimo_tempo_criacao_obstaculo = pygame.time.get_ticks()

# Função para criar obstáculos
def criar_obstaculo():
    tamanho = random.randint(20, 50)
    cor = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    obstaculo = {
        'retangulo': pygame.Rect(LARGURA, ALTURA - tamanho - 50, tamanho, tamanho),
        'cor': cor,
        'velocidade': random.randint(3, 8)
    }
    obstaculos.append(obstaculo)

# Loop principal do jogo
executando = True
relogio = pygame.time.Clock()

while executando:
    relogio.tick(60)
    tempo_atual = pygame.time.get_ticks()

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE and posicao_y_jogador == ALTURA - tamanho_jogador - 50:
                velocidade_y_jogador = forca_pulo

    # Atualização do jogador
    velocidade_y_jogador += gravidade
    posicao_y_jogador += velocidade_y_jogador
    if posicao_y_jogador >= ALTURA - tamanho_jogador - 50:
        posicao_y_jogador = ALTURA - tamanho_jogador - 50
        velocidade_y_jogador = 0

    # Atualização dos obstáculos
    if tempo_atual - ultimo_tempo_criacao_obstaculo > intervalo_criacao_obstaculo:
        criar_obstaculo()
        ultimo_tempo_criacao_obstaculo = tempo_atual

    for obstaculo in obstaculos:
        obstaculo['retangulo'].x -= obstaculo['velocidade']
        if obstaculo['retangulo'].x + obstaculo['retangulo'].width < 0:
            obstaculos.remove(obstaculo)

    # Colisão
    retangulo_jogador = pygame.Rect(posicao_x_jogador, posicao_y_jogador, tamanho_jogador, tamanho_jogador)
    for obstaculo in obstaculos:
        if retangulo_jogador.colliderect(obstaculo['retangulo']):
            executando = False

    # Desenho
    janela.fill(AZUL)
    pygame.draw.rect(janela, VERDE, (0, ALTURA - 50, LARGURA, 50))
    pygame.draw.rect(janela, PRETO, (posicao_x_jogador, posicao_y_jogador, tamanho_jogador, tamanho_jogador))
    for obstaculo in obstaculos:
        pygame.draw.polygon(janela, obstaculo['cor'], [
            (obstaculo['retangulo'].x, obstaculo['retangulo'].y + obstaculo['retangulo'].height),
            (obstaculo['retangulo'].x + obstaculo['retangulo'].width / 2, obstaculo['retangulo'].y),
            (obstaculo['retangulo'].x + obstaculo['retangulo'].width, obstaculo['retangulo'].y + obstaculo['retangulo'].height)
        ])

    pygame.display.flip()

pygame.quit()