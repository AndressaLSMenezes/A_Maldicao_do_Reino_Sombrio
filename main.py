# Essas últimas linhas de código criam uma instância da classe Game e chamam o método execute() para iniciar a execução do jogo

from dino_runner.components.game import Game

# expressão condicional que verifica se o módulo atual está sendo executado como um programa (ao invés de ser importado como um módulo em outro programa).
if __name__ == "__main__":
    game = Game()  
    game.execute()