import pygame
import sys
import random

# Defina constantes
WIDTH, HEIGHT = 600, 600
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
BOLINHA_RADIUS = 5

# Inicialize o Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man")
clock = pygame.time.Clock()

# Defina o Pac-Man e outros personagens
class PacMan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20  # Raio do Pac-Man
        self.color = YELLOW  # Amarelo
        self.direction = "right"  # Direção inicial do Pac-Man
        self.angle = 0  # Ângulo inicial da boca

    def move(self):
        # Implemente a lógica de movimento do Pac-Man aqui
        if self.direction == "right":
            self.x += 5  # Movimento para a direita
        elif self.direction == "left":
            self.x -= 5  # Movimento para a esquerda
        elif self.direction == "up":
            self.y -= 5  # Movimento para cima
        elif self.direction == "down":
            self.y += 5  # Movimento para baixo

    def draw(self):
        # Desenhe o Pac-Man na tela
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
        if self.direction == "right":
            pygame.draw.arc(screen, WHITE, (self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2), self.angle, 360 - self.angle, 0)
            self.angle += 5  # Aumenta o ângulo para simular a abertura e o fechamento da boca
            if self.angle >= 45:
                self.angle = 0

# Crie uma classe para representar as bolinhas
class Bolinha:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.radius = BOLINHA_RADIUS
        self.color = color

    def draw(self):
        # Desenhe a bolinha na tela
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Crie uma lista de bolinhas vermelhas em locais aleatórios
bolinhas_vermelhas = []
for _ in range(100):  # Você pode ajustar a quantidade de bolinhas vermelhas aqui
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    bolinhas_vermelhas.append(Bolinha(x, y, (255, 0, 0)))

# Crie algumas bolinhas azuis em locais aleatórios
bolinhas_azuis = []
for _ in range(10):  # Você pode ajustar a quantidade de bolinhas azuis aqui
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    bolinhas_azuis.append(Bolinha(x, y, (0, 0, 255)))

# Defina a função principal do jogo
def main():
    pac_man = PacMan(WIDTH // 2, HEIGHT // 2)  # Crie uma instância do Pac-Man

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pac_man.direction = "left"
                elif event.key == pygame.K_RIGHT:
                    pac_man.direction = "right"
                elif event.key == pygame.K_UP:
                    pac_man.direction = "up"
                elif event.key == pygame.K_DOWN:
                    pac_man.direction = "down"

        # Atualize a lógica do jogo aqui
        pac_man.move()

        # Verifique se o Pac-Man colidiu com alguma bolinha
        for bolinha in bolinhas_vermelhas + bolinhas_azuis:
            if pygame.Rect(bolinha.x - BOLINHA_RADIUS, bolinha.y - BOLINHA_RADIUS, BOLINHA_RADIUS * 2, BOLINHA_RADIUS * 2).colliderect(pygame.Rect(pac_man.x - pac_man.radius, pac_man.y - pac_man.radius, pac_man.radius * 2, pac_man.radius * 2)):
                if bolinha in bolinhas_vermelhas:
                    bolinhas_vermelhas.remove(bolinha)  # Remova a bolinha vermelha
                elif bolinha in bolinhas_azuis:
                    bolinhas_azuis.remove(bolinha)  # Remova a bolinha azul

        # Desenhe os personagens e as bolinhas na tela
        screen.fill(BLACK)  # Fundo preto

        for bolinha in bolinhas_vermelhas + bolinhas_azuis:
            bolinha.draw()

        pac_man.draw()

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
