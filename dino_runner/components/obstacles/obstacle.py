#Importando os módulos pygame e pygame.sprite
import pygame
from pygame.sprite import Sprite
#Importando a constante SCREEN_WIDTH do módulo constants dentro do pacote utils do projeto dino_runner
from dino_runner.utils.constants import SCREEN_WIDTH

#Definindo uma nova classe Obstacle que herda da classe Sprite
class Obstacle(Sprite):
    # Construtor da classe Obstacle, que define as propriedades do objeto
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
    # Método que atualiza a posição do obstáculo na tela
    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        # Removendo o obstáculo da lista de obstáculos se ele sair da tela
        if self.rect.x < -self.rect.width:
            obstacles.pop()
            
    # Método que desenha o obstáculo na tela
    def draw(self, screen):
        screen.blit(self.image[self.type], (self.rect.x, self.rect.y))
