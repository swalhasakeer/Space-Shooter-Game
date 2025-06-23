import pygame
import random

pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🚀 Space Shooter")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Player settings
player_width = 50
player_height = 30
player_x = WIDTH // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Bullet settings
bullet_width = 5
bullet_height = 10
bullets = []

# Enemy settings
enemy_size = 30
enemies = []
enemy_speed = 2

# Score
score = 0
font = pygame.font.SysFont(None, 30)

# Clock
clock = pygame.time.Clock()

def draw_player(x, y):
    pygame.draw.rect(screen, GREEN, (x, y, player_width, player_height))

def draw_bullets(bullets):
    for b in bullets:
        pygame.draw.rect(screen, WHITE, b)

def draw_enemies(enemies):
    for e in enemies:
        pygame.draw.rect(screen, RED, e)

def show_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

# Game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        bullets.append(pygame.Rect(player_x + player_width // 2 - 2, player_y, bullet_width, bullet_height))

    # Move bullets
    for b in bullets:
        b.y -= 10
    bullets = [b for b in bullets if b.y > 0]

    # Spawn enemies
    if random.randint(1, 30) == 1:
        enemies.append(pygame.Rect(random.randint(0, WIDTH - enemy_size), 0, enemy_size, enemy_size))

    # Move enemies
    for e in enemies:
        e.y += enemy_speed
        if e.colliderect(pygame.Rect(player_x, player_y, player_width, player_height)):
            running = False  # Game over

    # Bullet-enemy collision
    new_enemies = []
    for e in enemies:
        hit = False
        for b in bullets:
            if e.colliderect(b):
                bullets.remove(b)
                score += 1
                hit = True
                break
        if not hit:
            new_enemies.append(e)
    enemies = new_enemies

    draw_player(player_x, player_y)
    draw_bullets(bullets)
    draw_enemies(enemies)
    show_score(score)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
