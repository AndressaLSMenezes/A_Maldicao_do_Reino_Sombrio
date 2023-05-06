#Importando o módulo random e a classe Sprite do módulo pygame.sprite
import random
#Importando a constante SCREEN_WIDTH do módulo constants dentro do pacote utils do projeto dino_runner
from pygame.sprite import Sprite
#Definindo uma nova classe PowerUp que herda da classe Sprite
from dino_runner.utils.constants import SCREEN_WIDTH

# Construtor da classe PowerUp, que define as propriedades do objeto
class PowerUp(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.rect.y = random.randint(265, 300)
        self.start_time = 0
        self.duration = random.randint(5, 10)
    # Método que atualiza a posição do power-up na tela
    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        # Removendo o power-up da lista de power-ups se ele sair da tela
        if self.rect.x < -self.rect.width:
            power_ups.pop()

    # Método que desenha o power-up na tela
    def draw(self, screen):
        screen.blit(self.image, self.rect)