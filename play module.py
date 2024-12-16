import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_SIZE = 50
OBSTACLE_WIDTH, OBSTACLE_HEIGHT = 50, 50
OBSTACLE_SPEED = 10


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Избегай препятствий")

player_pos = [WIDTH // 2, HEIGHT - PLAYER_SIZE]

obstacles = []

score = 0
font = pygame.font.Font(None, 36)  # Шрифт для отображения счета

def main():
    global obstacles, score
    clock = pygame.time.Clock()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_pos[0] > 0:
            player_pos[0] -= 10
        if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - PLAYER_SIZE:
            player_pos[0] += 10

        if random.randint(1, 20) == 1:
            obstacle_x = random.randint(0, WIDTH - OBSTACLE_WIDTH)
            obstacles.append([obstacle_x, 0])

        for obstacle in obstacles:
            obstacle[1] += OBSTACLE_SPEED

        obstacles = [obs for obs in obstacles if obs[1] < HEIGHT]

        for obstacle in obstacles:
            if (player_pos[0] < obstacle[0] + OBSTACLE_WIDTH and
                    player_pos[0] + PLAYER_SIZE > obstacle[0] and
                    player_pos[1] < obstacle[1] + OBSTACLE_HEIGHT and
                    player_pos[1] + PLAYER_SIZE > obstacle[1]):
                game_over = True

        score += 1

        screen.fill(WHITE)
        pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE))

        for obstacle in obstacles:
            pygame.draw.rect(screen, RED, (obstacle[0], obstacle[1], OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

        score_text = font.render(f"Счет: {score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()