# Importa a biblioteca Pygame
import pygame
# Importa a classe Sprite da biblioteca Pygame
from pygame.sprite import Sprite
# Importa as constantes RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD e RUNNING_SHIELD da biblioteca dino_runner.utils.constants
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD

# Dicionários que mapeiam o tipo do dinossauro para a imagem correspondente
DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}
# Posição inicial do dinossauro na tela e velocidade do seu pulo
X_POS = 80
Y_POS = 400
Y_POS_DUCK = 420
JUMP_VEL = 8.5


# Classe que representa o dinossauro
class Dinosaur(Sprite):
    def __init__(self):
         # Define o tipo do dinossauro como o tipo padrão e sua imagem como a imagem de correr
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.dino_jump_vel = JUMP_VEL
        self.setup_state()
    # Define o estado inicial do dinossauro
    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.show_text = False
        self.shield_time_up = 0
    # Atualiza o estado do dinossauro de acordo com a entrada do usuário
    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()
        # Verifica se o usuário pressionou a tecla de seta para cima    
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = True
            self.dino_duck = False
        # Verifica se o usuário pressionou a tecla de seta para baixo
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_run = False
            self.dino_jump = False
            self.dino_duck = True
        # Caso contrário, o dinossauro corre
        elif not self.dino_jump and not self.dino_duck:
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False
        # Atualiza o índice do passo do dinossauro (usado para alternar as imagens das pernas do dinossauro)
        if self.step_index >= 9:
            self.step_index = 0
    # Método que atualiza a imagem e posição do dinossauro quando ele está correndo
    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS
        self.step_index += 1
    # Método que atualiza a imagem e posição do dinossauro quando ele está pulando
    def jump(self):
        # Atualiza a posição do dinossauro no eixo y de acordo com a velocidade do pulo
        self.image = JUMP_IMG[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.dino_jump_vel * 4
            self.dino_jump_vel -= 0.8
        # Quando o dinossauro atinge a altura máxima do pulo, ele volta à posição inicial e para de pular
        if self.dino_jump_vel < -JUMP_VEL:
            self.dino_rect_y = Y_POS
            self.dino_jump = False
            self.dino_jump_vel = JUMP_VEL
    # Método que atualiza a imagem e posição do dinossauro quando ele está agachado
    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = X_POS
        self.dino_rect.y = Y_POS_DUCK
        self.step_index += 1
        self.dino_duck = False
    # Método que desenha o dinossauro na tela
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))
