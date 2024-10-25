import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mars Lander - Episode 2")

# Couleurs
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Variables de l'atterrisseur
lander_x = screen_width // 2
lander_y = 50
lander_speed = 0
gravity = 0.5

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Logique de mouvement
    lander_speed += gravity
    lander_y += lander_speed

    # Effacer l'écran
    screen.fill(black)

    # Dessiner l'atterrisseur
    pygame.draw.rect(screen, green, (lander_x, lander_y, 50, 30))

    # Vérifier si l'atterrisseur touche le sol
    if lander_y >= screen_height - 30:
        lander_y = screen_height - 30
        lander_speed = 0  # Arrêter l'atterrisseur

    # Mettre à jour l'affichage
    pygame.display.flip()
    pygame.time.delay(30)