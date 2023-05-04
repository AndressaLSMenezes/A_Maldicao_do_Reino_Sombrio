# Importando biblioteca pygame
import pygame
#Importando constantes
from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
# Cores, tamanho e estilo da fonte utilizada nas mensagens
FONT_COLOR = (0, 0, 0)
FONT_SIZE = 22
FONT_STYLE = "freesansbold.ttf"

#A função utiliza a biblioteca Pygame para renderizar a mensagem com a fonte e cor especificadas e desenha a mensagem na posição central especificada na tela.
def draw_message_component(
    # mensagem a ser exibida
    message,
    # tela do jogo onde a mensagem será exibida
    screen,
    # cor da fonte da mensagem (preto por padrão)
    font_color=FONT_COLOR,
    # tamanho da fonte da mensagem (22 por padrão)
    font_size=FONT_SIZE,
    # coordenada y da posição central da mensagem na tela (metade da altura da tela por padrão)
    pos_y_center=SCREEN_HEIGHT // 2,
    # coordenada x da posição central da mensagem na tela (metade da largura da tela por padrão)
    pos_x_center=SCREEN_WIDTH // 2
):
    # Define a fonte utilizada nas mensagens
    font = pygame.font.Font(FONT_STYLE, font_size)
     # Renderiza a mensagem na tela com a fonte e cor especificadas
    text = font.render(message, True, font_color)
    # Obtém o retângulo que circunscreve a mensagem renderizada
    text_rect = text.get_rect()
    # Define a posição central da mensagem na tela
    text_rect.center = (pos_x_center, pos_y_center)
    # Desenha a mensagem na tela
    screen.blit(text, text_rect)