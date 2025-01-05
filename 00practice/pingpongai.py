import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_SIZE = 20
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set up title
pygame.display.set_caption("Ping Pong")

# Set up font
font = pygame.font.Font(None, 36)

# Set up clock
clock = pygame.time.Clock()

# Set up paddles
paddle1 = pygame.Rect(10, SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT / 2 - PADDLE_HEIGHT / 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Set up ball
ball = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, BALL_SIZE, BALL_SIZE)
ball_x_speed = 5
ball_y_speed = 5

# Set up scores
score1 = 0
score2 = 0

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1.y -= 5
    if keys[pygame.K_s]:
        paddle1.y += 5
    if keys[pygame.K_UP]:
        paddle2.y -= 5
    if keys[pygame.K_DOWN]:
        paddle2.y += 5

    # Move ball
    ball.x += ball_x_speed
    ball.y += ball_y_speed

    # Collision with walls
    if ball.y < 0 or ball.y > SCREEN_HEIGHT - BALL_SIZE:
        ball_y_speed *= -1

    # Collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_x_speed *= -1

    # Score points
    if ball.x < 0:
        score2 += 1
        ball.x = SCREEN_WIDTH / 2
        ball.y = SCREEN_HEIGHT / 2
    elif ball.x > SCREEN_WIDTH - BALL_SIZE:
        score1 += 1
        ball.x = SCREEN_WIDTH / 2
        ball.y = SCREEN_HEIGHT / 2

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT))

    # Display scores
    score_text = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(score_text, (SCREEN_WIDTH / 2 - 50, 10))

    # Update display
    pygame.display.flip()

    # Cap framerate
    clock.tick(FPS)
