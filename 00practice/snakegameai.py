import pygame
import sys
import random

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 20
SPEED = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.reset()
        self.font = pygame.font.Font(None, 36)

    def reset(self):
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.direction = "RIGHT"
        self.apple = self.generate_apple()
        self.score = 0

    def generate_apple(self):
        while True:
            x = random.randint(0, SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE
            y = random.randint(0, SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE
            apple = (x, y)
            if apple not in self.snake:
                return apple

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.direction != "DOWN":
                    self.direction = "UP"
                elif event.key == pygame.K_DOWN and self.direction != "UP":
                    self.direction = "DOWN"
                elif event.key == pygame.K_LEFT and self.direction != "RIGHT":
                    self.direction = "LEFT"
                elif event.key == pygame.K_RIGHT and self.direction != "LEFT":
                    self.direction = "RIGHT"

    def update(self):
        head = self.snake[-1]
        if self.direction == "UP":
            new_head = (head[0], head[1] - BLOCK_SIZE)
        elif self.direction == "DOWN":
            new_head = (head[0], head[1] + BLOCK_SIZE)
        elif self.direction == "LEFT":
            new_head = (head[0] - BLOCK_SIZE, head[1])
        elif self.direction == "RIGHT":
            new_head = (head[0] + BLOCK_SIZE, head[1])

        self.snake.append(new_head)
        if self.snake[-1] == self.apple:
            self.apple = self.generate_apple()
            self.score += 1
        else:
            self.snake.pop(0)

        if (self.snake[-1][0] < 0 or self.snake[-1][0] >= SCREEN_WIDTH or
            self.snake[-1][1] < 0 or self.snake[-1][1] >= SCREEN_HEIGHT or
            self.snake[-1] in self.snake[:-1]):
            self.reset()

    def draw(self):
        self.screen.fill(BLACK)
        for pos in self.snake:
            pygame.draw.rect(self.screen, GREEN, (pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(self.screen, RED, (self.apple[0], self.apple[1], BLOCK_SIZE, BLOCK_SIZE))
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(SPEED)

if __name__ == "__main__":
    game = SnakeGame()
    game.run()
