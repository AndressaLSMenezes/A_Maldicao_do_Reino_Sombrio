# Importando biblioteca pygame e os
import pygame
import os

# Global Constants
# Título da janela do jogo
TITLE = "A Maldição do Reino Sombrio: A Saga do Cálice da Luz"
# Altura da tela do jogo
SCREEN_HEIGHT = 600
# Largura da tela do jogo
SCREEN_WIDTH = 1100
# Número de quadros por segundo
FPS = 30

#define a variável IMG_DIR como o caminho absoluto para o diretório "assets" do jogo
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

# Assets Constants
# Constantes de Assets
ICON = pygame.image.load(os.path.join(IMG_DIR, "DinoWallpaper.png"))

# Lista de imagens do dinossauro correndo normalmente
new_size = (120, 120)
RUNNING = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Eleonor/Run/Run1.png")), new_size),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Eleonor/Run/Run2.png")), new_size),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Eleonor/Run/Run3.png")), new_size),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Eleonor/Run/Run4.png")), new_size),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Eleonor/Run/Run5.png")), new_size),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Eleonor/Run/Run6.png")), new_size),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Eleonor/Run/Run7.png")), new_size),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Eleonor/Run/Run8.png")), new_size),
]
# Lista de imagens do dinossauro correndo com escudo
RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]
# Lista de imagens do dinossauro correndo com martelo
RUNNING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoRun2.png")),
]

# Imagens do dinossauro pulando em diferentes situações
JUMPING = pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Eleonor/Jump/Jump2.png")), new_size)
JUMPING_SHIELD = pygame.image.load(
    os.path.join(IMG_DIR, "Dino/DinoJumpShield.png"))
JUMPING_HAMMER = pygame.image.load(
    os.path.join(IMG_DIR, "Dino/DinoJumpHammer.png"))
# Imagens do dinossauro agachado em diferentes situações
DUCKING = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Eleonor/Duck/1.png")), new_size),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Eleonor/Duck/1.png")), new_size),
]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Shield.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]

DUCKING_HAMMER = [
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck1Hammer.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Dino/DinoDuck2.png")),
]
# Imagens dos goblins de diferentes tamanhos
enemy_size = (80, 80)
SMALL_CACTUS = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemy/Goblin/1.png")), enemy_size),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemy/Goblin/2.png")), enemy_size),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemy/Goblin/3.png")), enemy_size),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemy/Goblin/4.png")), enemy_size),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemy/Goblin/5.png")), enemy_size),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemy/Goblin/6.png")), enemy_size),
]
LARGE_CACTUS = [
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus1.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus2.png")),
    pygame.image.load(os.path.join(IMG_DIR, "Cactus/LargeCactus3.png")),
]
# Imagens do pássaro
BIRD = [
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemy/EyeEnemy/1.png")), enemy_size),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemy/EyeEnemy/2.png")), enemy_size),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemy/EyeEnemy/3.png")), enemy_size),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemy/EyeEnemy/4.png")), enemy_size),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemy/EyeEnemy/5.png")), enemy_size),
    pygame.transform.scale(pygame.image.load(os.path.join(IMG_DIR, "Enemy/EyeEnemy/6.png")), enemy_size),
]
# Imagens de nuvens, escudo, martelo, fundo e coração
CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png'))
HAMMER = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png'))

# Tipos de dino
DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
