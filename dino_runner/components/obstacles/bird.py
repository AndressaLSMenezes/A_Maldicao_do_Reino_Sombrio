# Importação da constante Bird do módulo constants dentro do pacote utils do projeto dino_runner
from dino_runner.utils.constants import BIRD
# Importação da classse obstacle do módulo obstacle dentro do pacote componets do projeto dino_runner
from dino_runner.components.obstacles.obstacle import Obstacle

#Definindo uma nova classe bird que herda a classe obstacle
class Bird(Obstacle):
    # Chamando o construtor da classe pai Obstacle e passando BIRD e 0 como argumentos
    def __init__(self):
         # Chamando o construtor da classe pai Obstacle e passando BIRD e 0 como argumentos
        super().__init__(BIRD, 0)
         # Definindo a posição vertical do objeto
        self.rect.y = 250
        # Definindo um contador de passos para controlar a animação do objeto
        self.step_index = 0
    # Método que desenha o objeto na tela
    def draw(self, screen):
         # Desenhando o objeto na posição especificada pela propriedade rect com a imagem na posição atual do contador de passos dividido por 5
        screen.blit(self.image[self.step_index // 5], self.rect)
         # Incrementando o contador de passos
        self.step_index += 1
         # Verificando se o contador de passos é maior ou igual a 10
        if self.step_index >= 10:
            # Redefinindo o contador de passos para 0
            self.step_index = 0