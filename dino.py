import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chrome Dino Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Dino settings
dino_width, dino_height = 50, 50
dino_x, dino_y = 50, SCREEN_HEIGHT - dino_height - 30
dino_jump = False
jump_speed = 10
gravity = 0.5

# Cactus settings
cactus_width, cactus_height = 20, 50
cactus_x = SCREEN_WIDTH
cactus_y = SCREEN_HEIGHT - cactus_height - 30
cactus_speed = 5

# Game settings
clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont(None, 36)

def draw_dino(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, dino_width, dino_height))

def draw_cactus(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, cactus_width, cactus_height))

def show_score(score):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not dino_jump:
                dino_jump = True
                jump_velocity = jump_speed

    # Dino jump mechanics
    if dino_jump:
        dino_y -= jump_velocity
        jump_velocity -= gravity
        if dino_y >= SCREEN_HEIGHT - dino_height - 30:
            dino_y = SCREEN_HEIGHT - dino_height - 30
            dino_jump = False

    # Move cactus
    cactus_x -= cactus_speed
    if cactus_x < 0:
        cactus_x = SCREEN_WIDTH
        score += 1  # Increase score when cactus resets

    # Collision detection
    dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)
    cactus_rect = pygame.Rect(cactus_x, cactus_y, cactus_width, cactus_height)
    if dino_rect.colliderect(cactus_rect):
        running = False  # End game if collision occurs

    # Draw dino and cactus
    draw_dino(dino_x, dino_y)
    draw_cactus(cactus_x, cactus_y)

    # Display score
    show_score(score)

    # Update screen and control frame rate
    pygame.display.flip()
    clock.tick(30)

# Quit the game
pygame.quit()
