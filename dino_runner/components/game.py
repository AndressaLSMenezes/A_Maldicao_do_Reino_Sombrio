# Importa a biblioteca Pygame
import pygame
# Importa as constantes
from dino_runner.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
# Importa a classe Dinosaur do módulo dino_runner.components.dinosaur
from dino_runner.components.dinosaur import Dinosaur
# Importa a classe ObstacleManager do módulo dino_runner.components.obstacles.obstacle_manager
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
# Importa a função draw_message_component do módulo dino_runner.utils.text_utils
from dino_runner.utils.text_utils import draw_message_component
# Importa a classe PowerUpManager do módulo dino_runner.components.powerups.power_up_manager
from dino_runner.components.powerups.power_up_manager import PowerUpManager

# Classe que representa o game
class Game:
    def __init__(self, image_index):
        # Inicializa a biblioteca Pygame
        pygame.init()
        # Define o título da janela do jogo
        pygame.display.set_caption(TITLE)
        # Define o ícone da janela do jogo
        pygame.display.set_icon(ICON)
        # Cria a tela do jogo com largura e altura definidos pelas constantes SCREEN_WIDTH e SCREEN_HEIGHT
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # Define o relógio do jogo
        self.clock = pygame.time.Clock()
        # Variável que indica se o jogo está em andamento
        self.playing = False
        # Variável que indica se o jogo está rodando
        self.running = False
        # Pontuação do jogador
        self.score = 0
        # Contagem de vidas
        self.death_count = 0
        # Velocidade do jogo
        self.game_speed = 20
        # Posição x do fundo
        self.x_pos_bg = 0
        # Posição y do fundo
        self.y_pos_bg = 380
        # Cria o dinossauro do jogo
        self.player = Dinosaur()
        # Cria o gerenciador de obstáculos do jogo
        self.obstacle_manager = ObstacleManager()
        # Cria o gerenciador de power-ups do jogo
        self.power_up_manager = PowerUpManager()
        # Toca música no jogo
        self.image_index = image_index
        pygame.mixer.music.load('dino_runner/assets/Music/Heroic.mp3')

    def execute(self):
        # Define que o jogo está rodando
        self.running = True
        while self.running:
            if not self.playing:
                # Mostra o menu do jogo
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
         # Define que o jogo está em andamento
        self.playing = True
        # Reseta os obstáculos
        self.obstacle_manager.reset_obstacles()
        # Reseta os power-ups
        self.power_up_manager.reset_power_ups()
        # Define a velocidade do jogo
        self.game_speed = 20
        # Define a pontuação do jogador
        self.score = 0
        # Diminui o volume do som
        pygame.mixer.music.set_volume(0.2)
        # Toca a música e a repete, tornando o som constante
        pygame.mixer.music.play(-1)

        while self.playing:
            # Trata os eventos do jogo
            self.events()
            # Atualiza o jogo
            self.update()
            # Desenha o jogo
            self.draw()
    #O método events trata os eventos do jogo, ou seja, eventos que podem ocorrer durante a execução do jogo, como o fechamento da janela do jogo.
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
    #O método events trata os eventos do jogo, ou seja, eventos que podem ocorrer durante a execução do jogo, como o fechamento da janela do jogo.
    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_score()
        self.power_up_manager.update(self.score, self.game_speed, self.player)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 5
    #draw desenha o jogo na tela, desenhando o fundo, o dinossauro, os obstáculos, a pontuação do jogador, o tempo restante do power-up e os power-ups.
    def draw(self):
        # Define a taxa de atualização da tela
        self.clock.tick(FPS)
        # Preenche a tela com uma cor branca
        self.screen.fill((255, 255, 255))
        # Desenha o fundo do jogo
        self.draw_background()
        # Desenha o dinossauro
        self.player.draw(self.screen)
        # Desenha os obstáculos
        self.obstacle_manager.draw(self.screen)
        # Desenha a pontuação do jogador
        self.draw_score()
        #senha o tempo restante do power-up
        self.draw_power_up_time()
        # Desenha os power-ups
        self.power_up_manager.draw(self.screen)
        # Atualiza a tela
        pygame.display.update()
        # Troca o buffer da tela
        pygame.display.flip()

    def draw_background(self):
        # Largura da imagem do fundo
        image_width = BG.get_width()
        # Desenha o fundo na tela na posição (self.x_pos_bg, self.y_pos_bg)
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        # Desenha o fundo na tela novamente, desta vez com o início da imagem no final da primeira imagem desenhada
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        # Se a posição do fundo for menor ou igual à largura da imagem, desenha a imagem novamente para preencher o espaço
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            # Define a posição x do fundo como zero
            self.x_pos_bg = 0
            # Move o fundo para a esquerda com base na velocidade do jogo
            self.x_pos_bg -= self.game_speed

    def draw_score(self):
        # Usa a função "draw_message_component" para desenhar uma mensagem na tela, que exibe a pontuação atual do jogador.
        draw_message_component(
            # Texto da mensagem que será exibida na tela.
            f"pontos: {self.score}", 
            # Superfície na qual a mensagem será desenhada.
            self.screen,
            # Posição centralizada no eixo x da mensagem na tela.
            pos_x_center=1000,
            # Posição centralizada no eixo y da mensagem na tela.
            pos_y_center=50
        )

    def draw_power_up_time(self):
         # Verifica se o jogador possui um power-up ativo
        if self.player.has_power_up:
            # Calcula o tempo restante do power-up em segundos
            time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)
             # Se ainda houver tempo para exibir, mostra a mensagem na tela
            if time_to_show >= 0:
                draw_message_component(
                     # Mensagem a ser exibida
                    f"{self.player.type.capitalize()} enable for {time_to_show} seconds",
                    # Superfície na qual a mensagem será desenhada
                    self.screen,
                    # Tamanho da fonte da mensagem
                    font_size=18,
                    # Posição x centralizada da mensagem na tela
                    pos_x_center=500,
                    # Posição y centralizada da mensagem na tela
                    pos_y_center=40
                )
             # Se o tempo expirou, desativa o power-up do jogador e redefine seu tipo
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE

    def handle_events_on_menu(self):
        # Verifica todos os eventos na fila de eventos do Pygame
        for event in pygame.event.get():
            # Se o evento for QUIT (clicar no X da janela), define "playing" e "running" como False para encerrar o jogo
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            # Se o evento for KEYDOWN (apertar uma tecla), executa a função "run"
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        # Preenche a tela com branco
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        # Se a contagem de mortes for zero, exibe a mensagem de início do jogo
        if self.death_count == 0:
            draw_message_component(
                "pressione qualquer tecla para iniciar o jogo", self.screen)
        # Se houver contagem de mortes, exibe a mensagem de reinício do jogo
        else:
            draw_message_component("Pressione qualquer tecla para reiniciar o jogo",
                                   self.screen, pos_y_center=half_screen_height + 140)
            draw_message_component(
                 # Mensagem que exibe a pontuação atual do jogador
                f"sua pontuação: {self.score}",
                 # Superfície na qual a mensagem será desenhada
                self.screen,
                # Posição y centralizada da mensagem na tela
                pos_y_center=half_screen_height - 150
            )
            draw_message_component(
                # Mensagem que exibe a contagem de vidas restantes do jogador
                f"Contagem de vida: {self.death_count}",
                # Superfície na qual a mensagem será desenhada
                self.screen,
                # Posição y centralizada da mensagem na tela
                pos_y_center=half_screen_height - 100
            )
            # Desenha o ícone do jogo na tela
            self.screen.blit(ICON, (half_screen_width -40, half_screen_height - 30))
        # Atualiza a tela do Pygame para exibir as mudanças realizadas
        pygame.display.flip()
        # Verifica se o usuário realizou algum evento no menu do jogo
        self.handle_events_on_menu()
