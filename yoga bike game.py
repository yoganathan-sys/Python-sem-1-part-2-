# Yoga Bike Game - Python (Pygame Prototype)
# Note: This is a SAFE prototype. No real celebrity faces are used.
# Characters are represented with simple shapes/icons.

import pygame
import sys
import math

pygame.init()

# ---------------- CONFIG ----------------
WIDTH, HEIGHT = 1000, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Yoga Bike Game")

CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont("arial", 20)
BIGFONT = pygame.font.SysFont("arial", 36, bold=True)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
GRAY = (120, 120, 120)
YELLOW = (255, 215, 0)
RED = (200, 0, 0)

# ---------------- GAME RULES ----------------
MAX_BIKES = 20
START_BIKE_COST = 1_000_000
LIVES_PER_LEVEL = 2
SUB_LEVELS = 20

# ---------------- GAME STATE ----------------
money = 5_000_000
owned_bikes = 1
bike_cost = START_BIKE_COST
level = 1
sub_level = 1
lives = LIVES_PER_LEVEL
speed = 5
master_mode = False

# Player
player_x = WIDTH // 2
player_y = HEIGHT - 120

# ---------------- FUNCTIONS ----------------

def draw_road():
    pygame.draw.rect(SCREEN, BLACK, (300, 0, 400, HEIGHT))
    for y in range(0, HEIGHT, 40):
        pygame.draw.line(SCREEN, WHITE, (500, y), (500, y + 20), 2)


def draw_trees():
    for x in range(0, 300, 80):
        pygame.draw.rect(SCREEN, GREEN, (x + 20, HEIGHT - 150, 30, 80))
        pygame.draw.circle(SCREEN, GREEN, (x + 35, HEIGHT - 170), 40)

    for x in range(700, WIDTH, 80):
        pygame.draw.rect(SCREEN, GREEN, (x + 20, HEIGHT - 150, 30, 80))
        pygame.draw.circle(SCREEN, GREEN, (x + 35, HEIGHT - 170), 40)


def draw_bike(x, y):
    pygame.draw.circle(SCREEN, GRAY, (x - 15, y + 30), 15)
    pygame.draw.circle(SCREEN, GRAY, (x + 15, y + 30), 15)
    pygame.draw.rect(SCREEN, YELLOW, (x - 20, y, 40, 20))
    pygame.draw.circle(SCREEN, RED, (x, y - 10), 10)  # helmet


def show_ui():
    ui = FONT.render(f"Money: ₹{money} | Bikes: {owned_bikes} | Lives: {lives}", True, WHITE)
    lvl = FONT.render(f"Level: {level}  Sub-Level: {sub_level}", True, WHITE)
    SCREEN.blit(ui, (10, 10))
    SCREEN.blit(lvl, (10, 40))


def buy_bike():
    global money, owned_bikes, bike_cost
    if owned_bikes < MAX_BIKES and money >= bike_cost:
        money -= bike_cost
        owned_bikes += 1
        bike_cost *= 2


# ---------------- GAME LOOP ----------------
running = True
while running:
    CLOCK.tick(60)
    SCREEN.fill((20, 20, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                buy_bike()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 320:
        player_x -= speed
    if keys[pygame.K_RIGHT] and player_x < 680:
        player_x += speed

    # Difficulty scaling
    speed = 5 + level

    draw_road()
    draw_trees()
    draw_bike(player_x, player_y)
    show_ui()

    # Progression
    if pygame.time.get_ticks() % 3000 < 20:
        sub_level += 1
        if sub_level > SUB_LEVELS:
            sub_level = 1
            level += 1
            lives = LIVES_PER_LEVEL
            if level > 3:
                master_mode = True

    if master_mode:
        msg = BIGFONT.render("MASTER MODE: UNLIMITED RIDING", True, YELLOW)
        SCREEN.blit(msg, (250, 100))

    pygame.display.update()

pygame.quit()
