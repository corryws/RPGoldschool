import pygame
from character import Character
from enemy import Enemy
import os

pygame.init()

# Definizione delle costanti
screen_width = 500
screen_height = 500

# Definizione character and other
character = Character(100, 100, hp=100, mp=50, att=20, dif=10, spd=0.1)
enemy = Enemy(50, 50, hp=100, mp=50, att=20, dif=10, spd=0.2)

# Inizializzazione di Pygame e creazione della finestra
def init_game():
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("RPG_old_school")
    return screen

# Funzione principale del gioco
def main():
    screen = init_game()
    in_battle = False
    tot_passi = 0  # contatore passi

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not in_battle:
            handle_input()
            tot_passi += 1

            # Dopo tot passi eseguiti dal giocatore
            if tot_passi >= 20:
                in_battle = True
        else:
            while in_battle:
                clock = pygame.time.Clock()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                # Disegna i riquadri e il testo con l'immagine del mostro e le voci di menu
                # Disegna l'immagine del mostro e il menu di combattimento
                # Esegui altre operazioni di combattimento qui

                pygame.display.update()
                clock.tick(60)  # Limita il framerate a 60 FPS durante la lotta

                # Gestisci l'input del giocatore
                keys = pygame.key.get_pressed()
                if keys[pygame.K_a]:
                    # Esegui l'azione di attacco
                    pass
                elif keys[pygame.K_d]:
                    # Esegui l'azione di difesa
                    pass
                elif keys[pygame.K_f]:
                    # Esegui l'azione di fuga
                    pass

                # Condizione per uscire dalla lotta
                #if combattimento_terminato:
                 #   in_battle = False

    draw(screen)
    pygame.quit()

# Gestisce l'input del giocatore e restituisce le nuove coordinate
def handle_input():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        character.move(0, -character.spd)
    if keys[pygame.K_s]:
        character.move(0, character.spd)
    if keys[pygame.K_a]:
        character.move(-character.spd, 0)
    if keys[pygame.K_d]:
        character.move(character.spd, 0)

# Disegna a Schermo
def draw(screen):
    screen.fill((107, 140, 52))
    character.draw(screen)
    enemy.draw(screen)
    pygame.display.update()

if __name__ == "__main__":
    main()
