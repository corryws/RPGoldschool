import pygame

# Definizione della classe Enemy
class Enemy:
    def __init__(self, x, y, hp, mp, att, dif, spd):
        self.x = x
        self.y = y
        self.width = 16
        self.height = 16
        self.sprite = pygame.image.load('assets/sprites/enemy_1.png')
        self.hp = hp  # Punti vita
        self.mp = mp  # Punti mana
        self.att = att  # Attacco
        self.dif = dif  # Difesa
        self.spd = spd  # Velocità

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self, screen):
        screen.blit(self.sprite, (self.x, self.y))


    def take_damage(self, damage):
        self.hp -= damage

    def attack(self, target):
        damage = self.att - target.dif
        if damage > 0:
            target.take_damage(damage)