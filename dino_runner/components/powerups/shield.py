#Importando as constantes SHIELD e SHIELD_TYPE do módulo constants dentro do pacote utils do projeto dino_runner
from dino_runner.utils.constants import SHIELD, SHIELD_TYPE
#Importando a classe PowerUp do módulo power_up dentro do pacote powerups do projeto dino_runner
from dino_runner.components.powerups.power_up import PowerUp

#Definindo uma nova classe Shield que herda da classe PowerUp
class Shield(PowerUp):
    # Construtor da classe Shield, que define as propriedades do objeto
    def __init__(self):
        self.image = SHIELD
        self.type = SHIELD_TYPE
        super().__init__(self.image, self.type)