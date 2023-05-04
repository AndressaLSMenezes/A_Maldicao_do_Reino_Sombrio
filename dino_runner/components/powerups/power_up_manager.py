#Importando os módulos random e pygame
import random
import pygame
#Importando a classe Shield do módulo shield dentro do pacote powerups do projeto dino_runner
from dino_runner.components.powerups.shield import Shield

#Definindo uma nova classe PowerUpManager
class PowerUpManager:
    # Construtor da classe PowerUpManager, que define as propriedades do objeto
    def __init__(self):
        # Inicializando uma lista vazia para os power-ups
        self.power_ups = []
        # Inicializando o contador de pontuação para quando um power-up aparecer na tela
        self.when_appears = 0

    # Método que gera um power-up na tela
    def generate_power_up (self, score):
         # Adicionando um novo power-up à lista de power-ups se a lista estiver vazia e a pontuação for igual ao contador de pontuação
        if len(self.power_ups) == 0 and self.when_appears == score:
             # Gerando uma nova pontuação para o próximo power-up
            self.when_appears += random.randint(200, 300)
            # Adicionando um novo power-up do tipo Shield à lista de power-ups
            self.power_ups.append(Shield())
    # Método que atualiza os power-ups na tela
    def update(self, score, game_speed, player):
        # Gerando um novo power-up na tela
        self.generate_power_up(score)
         # Atualizando cada power-up na lista de power-ups
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            # Verificando se houve colisão entre o jogador e o power-up
            if player.dino_rect.colliderect(power_up.rect):
                # Iniciando o tempo de duração do power-up
                power_up.start_time = pygame.time.get_ticks()
                # Ativando o escudo do jogador
                player.shield = True
                player.has_power_up = True
                # Definindo o tipo do jogador como o tipo do power-up
                player.type = power_up.type
                # Definindo o tempo de duração do power-up
                player.power_up_time = power_up.start_time + (power_up.duration * 1000)
                # Removendo o power-up da lista de power-ups
                self.power_ups.remove(power_up)
    # Método que desenha os power-ups na tela
    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
    # Método que reseta a lista de power-ups
    def reset_power_ups(self):
        self.power_ups = []
        # Gerando uma nova pontuação para o próximo power-up
        self.when_appears = random.randint(200, 300)
    
