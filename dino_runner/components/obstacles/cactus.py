#Importando o módulo random para gerar número aleatórios
import random
#Importando as constantes LARGE_CACTUS e SMALL_CACTUS do módulo constants dentro do pacote utils do projeto dino_runner
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS
#Importando a classe Obstacle do módulo obstacle dentro do pacote components do projeto dino_runner
from dino_runner.components.obstacles.obstacle import Obstacle

#Definindo uma nova classe Cactus que herda da classe Obstacle
class Cactus(Obstacle):
    # Lista de tuplas que contém as imagens e posições possíveis do cacto
    CACTUS = [
        (LARGE_CACTUS, 420),
        #goblins
        (SMALL_CACTUS, 440),
    ]
    
    # Construtor da classe Cactus, que define as propriedades do objeto
    def __init__(self):
        # Selecionando uma imagem e posição aleatórias da lista CACTUS
        image, cactus_pos = self.CACTUS[random.randint(0, 1)]
        # Selecionando um tipo aleatório para o cacto
        self.type = random.randint(0, 2)
        # Chamando o construtor da classe pai Obstacle e passando a imagem selecionada e o tipo selecionado como argumentos
        super().__init__(image, self.type)
        # Definindo a posição vertical do objeto como a posição do cacto selecionado
        self.rect.y = cactus_pos