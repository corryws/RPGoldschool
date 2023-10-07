import pygame
from character import Character
from enemy import Enemy
import os
print("Directory di lavoro corrente:", os.getcwd())




pygame.init()

# Definizione delle costanti
screen_width = 500
screen_height = 500
red = (255, 0, 0)

# Inizializzazione di Pygame e creazione della finestra
def init_game():
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("RPG_old_school")
    return screen

# Funzione principale del gioco
def main():
    screen = init_game()

    character = Character(100, 100, hp=100, mp=50, att=20, dif=10, spd=0.2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_input(character)
        draw(screen, character)
    
    pygame.quit()

# Gestisce l'input del giocatore e restituisce le nuove coordinate
def handle_input(character):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        character.move(0, -character.spd)
    if keys[pygame.K_s]:
        character.move(0, character.spd)
    if keys[pygame.K_a]:
        character.move(-character.spd, 0)
    if keys[pygame.K_d]:
        character.move(character.spd, 0)

# Disegna il rettangolo
def draw(screen, character):
    screen.fill((107, 140, 52))
    character.draw(screen)
    pygame.display.update()

if __name__ == "__main__":
    main()