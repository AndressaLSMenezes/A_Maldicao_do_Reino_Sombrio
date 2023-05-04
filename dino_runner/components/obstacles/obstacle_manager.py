#Importando os módulo pygame 
import pygame
#Importando os módulo random
import random
#Importando as classes Cactus
from dino_runner.components.obstacles.cactus import Cactus
#Importando a Bird do módulo obstacles dentro do pacote components do projeto dino_runner
from dino_runner.components.obstacles.bird import Bird


#Definindo uma nova classe ObstacleManager
class ObstacleManager:
    # Construtor da classe ObstacleManager, que define as propriedades do objeto
    def __init__(self):
        # Inicializando uma lista vazia para os obstáculos
        self.obstacles = []
    # Método que atualiza os obstáculos na tela
    def update(self, game):
        # Lista de tipos de obstáculos possíveis (cacto e pássaro)
        obstacle_type = [
            Cactus(),
            Bird(),
        ]
        # Adicionando um obstáculo aleatório à lista de obstáculos se a lista estiver vazia
        if len(self.obstacles) == 0:
            self.obstacles.append(obstacle_type[random.randint(0,1)])
        # Atualizando cada obstáculo na lista de obstáculos
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            # Verificando se houve colisão entre o jogador e o obstáculo
            if game.player.dino_rect.colliderect(obstacle.rect):
                # Verificando se o jogador tem um power-up
                if not game.player.has_power_up:
                     # Aguardando 500ms antes de encerrar o jogo
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1 
                    break
                # Removendo o obstáculo da lista de obstáculos se o jogador tem um power-up
                else:
                    self.obstacles.remove(obstacle)
    # Método que reseta a lista de obstáculos
    def reset_obstacles(self):
        self.obstacles = []
    # Método que desenha os obstáculos na tela
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)